#!/usr/bin/env python3
"""
MemoryCore Stats - Token usage & session analytics across all projects.
Usage: python3 ~/.claude/agent-stats.py
"""

import json
import os
import glob
from datetime import datetime
from collections import defaultdict

CLAUDE_DIR = os.path.expanduser("~/.claude")
PROJECTS_DIR = os.path.join(CLAUDE_DIR, "projects")
STATS_FILE = os.path.join(CLAUDE_DIR, "agent-usage-log.json")
LABELS_FILE = os.path.join(CLAUDE_DIR, "project-labels.json")


def load_labels():
    if os.path.exists(LABELS_FILE):
        try:
            with open(LABELS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def save_labels(labels):
    with open(LABELS_FILE, "w") as f:
        json.dump(labels, f, indent=2)


def auto_label(dirname):
    name = dirname
    home_user = os.path.expanduser("~").replace("/", "-")
    prefix = f"-{home_user[1:]}-"
    for p in [prefix + "Desktop-", prefix]:
        if name.startswith(p):
            name = name[len(p):]
            break
    return name.replace("-", " ").title()


def get_project_label(dirname, labels):
    if dirname in labels:
        return labels[dirname]
    label = auto_label(dirname)
    labels[dirname] = label
    save_labels(labels)
    return label


def parse_session(filepath):
    totals = {
        "input_tokens": 0, "output_tokens": 0,
        "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0,
        "messages": 0, "tool_calls": 0, "user_messages": 0,
        "files_edited": set(), "files_read": set(),
    }
    first_ts = None
    last_ts = None

    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                ts = obj.get("timestamp")
                if ts:
                    if first_ts is None:
                        first_ts = ts
                    last_ts = ts

                msg_type = obj.get("type")
                if msg_type == "user":
                    totals["messages"] += 1
                    totals["user_messages"] += 1
                if msg_type == "assistant":
                    totals["messages"] += 1
                    msg = obj.get("message", {})
                    if isinstance(msg, dict):
                        usage = msg.get("usage", {})
                        totals["input_tokens"] += usage.get("input_tokens", 0)
                        totals["output_tokens"] += usage.get("output_tokens", 0)
                        totals["cache_read_input_tokens"] += usage.get("cache_read_input_tokens", 0)
                        totals["cache_creation_input_tokens"] += usage.get("cache_creation_input_tokens", 0)
                        content = msg.get("content", [])
                        if isinstance(content, list):
                            for block in content:
                                if isinstance(block, dict) and block.get("type") == "tool_use":
                                    totals["tool_calls"] += 1
                                    name = block.get("name", "")
                                    inp = block.get("input", {})
                                    if name in ("Edit", "Write"):
                                        fp = inp.get("file_path", "")
                                        if fp:
                                            totals["files_edited"].add(fp)
                                    elif name == "Read":
                                        fp = inp.get("file_path", "")
                                        if fp:
                                            totals["files_read"].add(fp)
    except Exception:
        pass

    duration_min = 0
    if first_ts and last_ts:
        try:
            t1 = datetime.fromisoformat(first_ts.replace("Z", "+00:00"))
            t2 = datetime.fromisoformat(last_ts.replace("Z", "+00:00"))
            duration_min = max(0, int((t2 - t1).total_seconds() / 60))
        except Exception:
            pass

    return {
        **{k: v for k, v in totals.items() if k not in ("files_edited", "files_read")},
        "first_timestamp": first_ts, "last_timestamp": last_ts,
        "duration_min": duration_min,
        "files_edited_count": len(totals["files_edited"]),
        "files_read_count": len(totals["files_read"]),
        "files_edited_list": list(totals["files_edited"]),
    }


def scan_all_projects():
    results = {}
    if not os.path.isdir(PROJECTS_DIR):
        return results
    labels = load_labels()
    for project_dir in os.listdir(PROJECTS_DIR):
        project_path = os.path.join(PROJECTS_DIR, project_dir)
        if not os.path.isdir(project_path):
            continue
        label = get_project_label(project_dir, labels)
        stats = {
            "sessions": [], "total_input_tokens": 0, "total_output_tokens": 0,
            "total_cache_read": 0, "total_cache_creation": 0, "total_messages": 0,
            "total_tool_calls": 0, "total_files_edited": 0, "total_files_read": 0,
            "total_duration_min": 0, "session_count": 0, "hot_files": defaultdict(int),
        }
        for jsonl_file in glob.glob(os.path.join(project_path, "*.jsonl")):
            sd = parse_session(jsonl_file)
            if sd["messages"] == 0:
                continue
            date = "unknown"
            if sd["first_timestamp"]:
                try:
                    date = datetime.fromisoformat(sd["first_timestamp"].replace("Z", "+00:00")).strftime("%Y-%m-%d")
                except Exception:
                    pass
            stats["sessions"].append({"date": date, "output_tokens": sd["output_tokens"]})
            stats["total_input_tokens"] += sd["input_tokens"]
            stats["total_output_tokens"] += sd["output_tokens"]
            stats["total_cache_read"] += sd["cache_read_input_tokens"]
            stats["total_cache_creation"] += sd["cache_creation_input_tokens"]
            stats["total_messages"] += sd["messages"]
            stats["total_tool_calls"] += sd["tool_calls"]
            stats["total_files_edited"] += sd["files_edited_count"]
            stats["total_files_read"] += sd["files_read_count"]
            stats["total_duration_min"] += sd["duration_min"]
            stats["session_count"] += 1
            for fp in sd["files_edited_list"]:
                stats["hot_files"][fp.split("/")[-1] if "/" in fp else fp] += 1
        if stats["session_count"] > 0:
            stats["hot_files"] = dict(sorted(stats["hot_files"].items(), key=lambda x: -x[1])[:5])
            results[label] = stats
    return dict(sorted(results.items(), key=lambda x: -(
        x[1]["total_input_tokens"] + x[1]["total_output_tokens"]
        + x[1]["total_cache_read"] + x[1]["total_cache_creation"])))


def fmt(n):
    return f"{n:,}"


def dur(m):
    if m < 60:
        return f"{m}m"
    h, r = m // 60, m % 60
    return f"{h}h {r}m" if r else f"{h}h"


def print_stats(results):
    grand = {"input": 0, "output": 0, "cr": 0, "cc": 0, "msg": 0, "tools": 0,
             "sess": 0, "fe": 0, "fr": 0, "dur": 0}
    today = datetime.now().strftime("%Y-%m-%d")
    today_sess, today_tok = 0, 0

    print()
    print("=" * 62)
    print("  MemoryCore - Usage & Session Analytics")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 62)

    for project, s in results.items():
        tt = s["total_input_tokens"] + s["total_output_tokens"] + s["total_cache_read"] + s["total_cache_creation"]
        avg_t = tt // s["session_count"]
        avg_d = s["total_duration_min"] // s["session_count"]
        print(f"\n  >> {project}")
        print(f"  {'─' * 50}")
        print(f"  Sessions        : {s['session_count']}")
        print(f"  Messages        : {fmt(s['total_messages'])}")
        print(f"  Tool Calls      : {fmt(s['total_tool_calls'])}")
        print(f"  Files Edited    : {fmt(s['total_files_edited'])}")
        print(f"  Files Read      : {fmt(s['total_files_read'])}")
        print(f"  Total Time      : {dur(s['total_duration_min'])}")
        print(f"  Avg/Session     : {fmt(avg_t)} tokens, {dur(avg_d)}")
        print(f"  Input Tokens    : {fmt(s['total_input_tokens'])}")
        print(f"  Output Tokens   : {fmt(s['total_output_tokens'])}")
        print(f"  Cache Read      : {fmt(s['total_cache_read'])}")
        print(f"  Cache Creation  : {fmt(s['total_cache_creation'])}")
        print(f"  Total Tokens    : {fmt(tt)}")
        if s["hot_files"]:
            hot = ", ".join(f"{f}({c})" for f, c in list(s["hot_files"].items())[:3])
            print(f"  Hot Files       : {hot}")
        for sess in s["sessions"]:
            if sess.get("date") == today:
                today_sess += 1
                today_tok += sess.get("output_tokens", 0)
        grand["input"] += s["total_input_tokens"]
        grand["output"] += s["total_output_tokens"]
        grand["cr"] += s["total_cache_read"]
        grand["cc"] += s["total_cache_creation"]
        grand["msg"] += s["total_messages"]
        grand["tools"] += s["total_tool_calls"]
        grand["sess"] += s["session_count"]
        grand["fe"] += s["total_files_edited"]
        grand["fr"] += s["total_files_read"]
        grand["dur"] += s["total_duration_min"]

    gt = grand["input"] + grand["output"] + grand["cr"] + grand["cc"]
    print(f"\n{'=' * 62}")
    print("  GRAND TOTAL")
    print(f"  {'─' * 50}")
    print(f"  Projects        : {len(results)}")
    print(f"  Sessions        : {grand['sess']}")
    print(f"  Messages        : {fmt(grand['msg'])}")
    print(f"  Tool Calls      : {fmt(grand['tools'])}")
    print(f"  Files Edited    : {fmt(grand['fe'])}")
    print(f"  Files Read      : {fmt(grand['fr'])}")
    print(f"  Total Time      : {dur(grand['dur'])}")
    print(f"  Avg/Session     : {fmt(gt // grand['sess'] if grand['sess'] else 0)} tokens")
    print(f"  Total Tokens    : {fmt(gt)}")
    print("=" * 62)
    if today_sess:
        print(f"\n  TODAY ({today})")
        print(f"  {'─' * 50}")
        print(f"  Sessions        : {today_sess}")
        print(f"  Output Tokens   : {fmt(today_tok)}")
        print("=" * 62)
    print()

    # Save log
    log = {"timestamp": datetime.now().isoformat(), "grand_total": {
        "projects": len(results), "sessions": grand["sess"], "tokens": gt},
        "today": {"date": today, "sessions": today_sess}}
    history = []
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, "r") as f:
                history = json.load(f)
        except Exception:
            pass
    history.append(log)
    with open(STATS_FILE, "w") as f:
        json.dump(history, f, indent=2)


if __name__ == "__main__":
    results = scan_all_projects()
    if results:
        print_stats(results)
    else:
        print("\n  No session data found.\n")
