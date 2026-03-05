# Pattern Library
> Proven, reusable solutions indexed by problem type. Pull from here before re-inventing.

As you build projects, add your patterns here. Each pattern should include:
- **Stack**: What tech it applies to
- **Problem**: What you're solving
- **Solution**: The approach or code pattern
- **Gotchas**: What to watch out for
- **First used in**: Which project

---

## Starter Patterns

### File Uploads
<!-- Add your file upload patterns as you discover them -->
<!-- Example:
#### Laravel + Inertia
- Use `router.post` with `forceFormData: true` + `_method: 'PUT'` for updates
- Old file cleanup: delete previous file on re-upload
- Storage link: `php artisan storage:link`
-->

### Authentication & Roles
<!-- Add your auth patterns -->

### Payment Gateways
<!-- Add your payment patterns -->
<!-- Important: Always CSRF-exempt callback routes -->
<!-- Important: Never set status to "paid" before payment confirms -->

### Database Patterns
<!-- Add your DB patterns -->
<!-- Example: Always use type:'num' for DataTable ID columns -->

### Deployment
<!-- Add your deployment patterns -->

### UI Components
<!-- Add your UI patterns -->

### Notifications
<!-- Add your notification patterns -->

### API Integration
<!-- Add your API patterns -->

---

## How to Add Patterns

After completing a significant feature, ask yourself:
1. Would I use this approach again in another project?
2. Did I discover a gotcha that others should know about?
3. Is there a specific code pattern that solved a tricky problem?

If yes to any, add it here under the appropriate category. Create new categories as needed.

Format:
```markdown
### [Category Name]

#### [Pattern Name]
- **Stack**: [e.g. Laravel + React]
- **Problem**: [What you're solving]
- **Solution**: [Code pattern or approach]
- **Gotchas**: [What to watch out for]
- **First used in**: [Project name]
```
