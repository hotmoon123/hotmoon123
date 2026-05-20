# Glassmorphism Implementation Guide
## RentFlow CRM Template Pattern Reference

**Status:** Foundation complete. This guide documents how to apply glassmorphism to the remaining 25+ templates.

---

## Quick Reference: Glass Component Classes

Every template uses these reusable classes from `main.css`:

### Containers
- `.glass` — Base glass panel with blur + border
- `.glass-card` — Card with padding, shadow, hover effect
- `.glass-sidebar` — Sidebar with strong blur (40px)
- `.glass-navbar` — Top navigation bar
- `.glass-modal` — Fullscreen modal with backdrop
- `.glass-form` — Form container with card styling

### Inputs
- `.glass-input` — Text input with glass effect + focus glow
- `.glass-select` — Select dropdown with glass styling

### Buttons
- `.btn-glass-primary` — Blue gradient button with shimmer
- `.btn-glass-secondary` — Outlined button
- `.btn-glass-success` — Green success button
- `.btn-glass-danger` — Red danger button

### Data Display
- `.glass-table` — Table with glass header + hover rows
- `.glass-stat-card` — Metric card with icon + number + trend
- `.badge-success|warning|danger|info|muted` — Status badges

### Layout
- `.grid-4` / `.grid-3` / `.grid-2` — CSS Grid layouts
- `.page-header` — Page title + subtitle
- `.page-content` — Main content area
- `.form-group` — Form field wrapper
- `.form-label` — Form label styling

### Utilities
- `.glass-alert` (+ `.alert-success|warning|danger|info`) — Alert banners
- `.glass-divider` — Separator line
- `.skeleton` — Loading animation
- `.empty-state` — Empty state message
- `.avatar` — User avatar circle

---

## Pattern 1: Dashboard Page (Landlord/Tenant)

### HTML Structure
```html
{% extends "base_landlord.html" %}

{% block page_title %}Dashboard{% endblock %}

{% block content %}
<div class="page-header" data-aos="fade-up">
    <h1 class="page-title">Dashboard</h1>
    <p class="page-subtitle">Welcome back! Here's your property overview.</p>
</div>

<!-- 4-Column Stat Cards -->
<div class="grid-4" data-aos="fade-up" data-aos-delay="100">
    <div class="glass-stat-card stat-blue" data-aos="fade-up" data-aos-delay="0">
        <div class="stat-icon icon-blue">📊</div>
        <div class="stat-number" id="total-properties">0</div>
        <div class="stat-label">Total Properties</div>
        <div class="stat-trend trend-up">
            <i class="ph ph-arrow-up" style="font-size: 12px;"></i>
            +12%
        </div>
    </div>
    <!-- Repeat for other stats -->
</div>

<!-- Table Section -->
<div class="glass-card" data-aos="fade-up" data-aos-delay="200">
    <h2 style="margin: 0 0 20px 0; font-size: 18px; font-weight: 600; color: var(--text-primary);">
        Recent Activity
    </h2>
    <table class="glass-table">
        <thead>
            <tr>
                <th>Property</th>
                <th>Tenant</th>
                <th>Status</th>
                <th>Amount</th>
                <th>Due Date</th>
            </tr>
        </thead>
        <tbody>
            <!-- Add rows from context data -->
        </tbody>
    </table>
</div>

<!-- Chart Section (uses Chart.js) -->
<div class="grid-2" data-aos="fade-up" data-aos-delay="300">
    <div class="glass-card">
        <h3 style="margin: 0 0 20px 0;">Revenue Trend</h3>
        <canvas id="revenueChart"></canvas>
    </div>
    <div class="glass-card">
        <h3 style="margin: 0 0 20px 0;">Payment Status</h3>
        <canvas id="statusChart"></canvas>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
    // Initialize stat counters (CountUp.js)
    new CountUp('total-properties', 0, {{ total_properties }}, 0, 2.5,
        { useEasing: true }).start();

    // Chart.js configuration
    const chartDefaults = {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: { labels: { color: 'rgba(255,255,255,0.70)' } }
        },
        scales: {
            x: {
                grid: { color: 'rgba(255,255,255,0.06)' },
                ticks: { color: 'rgba(255,255,255,0.50)' }
            },
            y: {
                grid: { color: 'rgba(255,255,255,0.06)' },
                ticks: { color: 'rgba(255,255,255,0.50)' }
            }
        }
    };

    // Revenue Line Chart
    const revenueCtx = document.getElementById('revenueChart').getContext('2d');
    new Chart(revenueCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            datasets: [{
                label: 'Revenue (₵)',
                data: [{{ revenue_data }}],
                borderColor: '#0052A3',
                backgroundColor: 'rgba(0, 82, 163, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: chartDefaults
    });

    // Payment Status Pie Chart
    const statusCtx = document.getElementById('statusChart').getContext('2d');
    new Chart(statusCtx, {
        type: 'doughnut',
        data: {
            labels: ['Paid', 'Pending', 'Overdue'],
            datasets: [{
                data: [{{ paid }}, {{ pending }}, {{ overdue }}],
                backgroundColor: ['#34D399', '#FCD34D', '#F87171'],
                borderColor: 'rgba(255,255,255,0.15)'
            }]
        },
        options: chartDefaults
    });
</script>
{% endblock %}
```

---

## Pattern 2: List Page (Properties, Leases, Tenants)

```html
{% extends "base_landlord.html" %}

{% block page_title %}Properties{% endblock %}

{% block content %}
<div class="page-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 class="page-title">Properties</h1>
            <p class="page-subtitle">Manage your rental units and buildings</p>
        </div>
        <a href="/landlord/properties/create/" class="btn-glass-primary" style="text-decoration: none;">
            <i class="ph ph-plus" style="margin-right: 8px;"></i>
            Add Property
        </a>
    </div>
</div>

<!-- Search Bar -->
<div class="glass-card" style="margin-bottom: 24px;">
    <input type="text" id="searchInput" class="glass-input" placeholder="Search properties by name or address...">
</div>

<!-- Properties Table -->
<div class="glass-card" data-aos="fade-up">
    <table class="glass-table">
        <thead>
            <tr>
                <th>Unit</th>
                <th>Address</th>
                <th>Type</th>
                <th>Rent (₵)</th>
                <th>Tenant</th>
                <th>Status</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for property in properties %}
            <tr data-aos="fade-in" data-aos-delay="100">
                <td>{{ property.unit_number }}</td>
                <td>{{ property.address }}</td>
                <td>{{ property.get_property_type_display }}</td>
                <td>₵{{ property.rent_amount }}</td>
                <td>{{ property.tenant_name|default:"Unoccupied" }}</td>
                <td>
                    <span class="badge badge-{% if property.status == 'occupied' %}success{% elif property.status == 'available' %}info{% else %}warning{% endif %}">
                        {{ property.get_status_display }}
                    </span>
                </td>
                <td>
                    <a href="/landlord/properties/{{ property.id }}/" style="color: var(--primary-light); text-decoration: none; font-size: 13px; margin-right: 10px;">View</a>
                    <a href="/landlord/properties/{{ property.id }}/edit/" style="color: var(--text-secondary); text-decoration: none; font-size: 13px;">Edit</a>
                </td>
            </tr>
            {% empty %}
            <tr>
                <td colspan="7">
                    <div class="empty-state">
                        <div class="empty-state-icon">🏠</div>
                        <div class="empty-state-title">No Properties Yet</div>
                        <div class="empty-state-text">Create your first property to get started</div>
                        <a href="/landlord/properties/create/" class="btn-glass-primary" style="text-decoration: none;">Add Property</a>
                    </div>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
```

---

## Pattern 3: Form Page (Create/Edit)

```html
{% extends "base_landlord.html" %}

{% block page_title %}Add Property{% endblock %}

{% block content %}
<div class="page-header">
    <h1 class="page-title">Add New Property</h1>
    <p class="page-subtitle">Register a new rental unit</p>
</div>

<div class="glass-form" style="max-width: 600px;" data-aos="fade-up">
    <form id="propertyForm">
        <div class="form-group">
            <label class="form-label" for="unit_number">Unit Number *</label>
            <input type="text" id="unit_number" name="unit_number" class="glass-input" placeholder="e.g., Apt 101" required>
        </div>

        <div class="form-group">
            <label class="form-label" for="address">Full Address *</label>
            <input type="text" id="address" name="address" class="glass-input" placeholder="Street address" required>
        </div>

        <div class="form-group">
            <label class="form-label" for="property_type">Property Type *</label>
            <select id="property_type" name="property_type" class="glass-select" required>
                <option value="">Select...</option>
                <option value="apartment">Apartment</option>
                <option value="house">House</option>
                <option value="studio">Studio</option>
                <option value="office">Office</option>
            </select>
        </div>

        <div class="form-group">
            <label class="form-label" for="rent_amount">Monthly Rent (₵) *</label>
            <input type="number" id="rent_amount" name="rent_amount" class="glass-input" placeholder="0.00" step="0.01" required>
        </div>

        <div class="form-group">
            <label class="form-label" for="description">Description</label>
            <textarea id="description" name="description" class="glass-input" style="resize: vertical; min-height: 120px; padding: 12px 16px;" placeholder="Property details..."></textarea>
        </div>

        <div id="errorMessage" class="glass-alert alert-danger" style="display: none; margin-bottom: 20px;">
            <i class="ph ph-warning-circle"></i>
            <span id="errorText"></span>
        </div>

        <div style="display: flex; gap: 12px;">
            <button type="submit" class="btn-glass-primary">Create Property</button>
            <a href="/landlord/properties/" class="btn-glass-secondary" style="text-decoration: none;">Cancel</a>
        </div>
    </form>
</div>

<script>
    document.getElementById('propertyForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const errorDiv = document.getElementById('errorMessage');
        errorDiv.style.display = 'none';

        const formData = {
            unit_number: document.getElementById('unit_number').value,
            address: document.getElementById('address').value,
            property_type: document.getElementById('property_type').value,
            rent_amount: parseFloat(document.getElementById('rent_amount').value),
            description: document.getElementById('description').value,
        };

        try {
            const response = await fetch('/properties/create/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(formData)
            });

            const data = await response.json();

            if (response.ok && data.success) {
                showToast('Property created successfully!', 'success');
                setTimeout(() => window.location.href = '/landlord/properties/', 1500);
            } else {
                document.getElementById('errorText').textContent = data.error || 'Failed to create property';
                errorDiv.style.display = 'flex';
            }
        } catch (error) {
            document.getElementById('errorText').textContent = 'An error occurred';
            errorDiv.style.display = 'flex';
        }
    });
</script>
{% endblock %}
```

---

## Applying to Remaining 25+ Templates

### Step 1: Choose Your Template Type
- **Dashboard**: Use Pattern 1 (stat cards + charts + tables)
- **List Page**: Use Pattern 2 (search + table + actions)
- **Form Page**: Use Pattern 3 (form inputs + validation)
- **Detail Page**: Mix of Pattern 1 + Pattern 2 (display data + action buttons)

### Step 2: Replace Old Classes
| Old Class | New Glass Class |
|-----------|-----------------|
| `.card` | `.glass-card` |
| `.button` | `.btn-glass-primary` |
| `.error` | `.glass-alert alert-danger` |
| `<input>` | `<input class="glass-input">` |
| `<select>` | `<select class="glass-select">` |
| `<table>` | `<table class="glass-table">` |

### Step 3: Add Animations
```html
<!-- Fade in on scroll -->
<div class="glass-card" data-aos="fade-up" data-aos-delay="100">...</div>

<!-- Staggered animations -->
{% for item in items %}
<div class="glass-card" data-aos="fade-up" data-aos-delay="{{ forloop.counter0|mul:100 }}">...</div>
{% endfor %}
```

### Step 4: Add Charts (for analytics pages)
```html
<div class="glass-card">
    <h3>Revenue Chart</h3>
    <canvas id="myChart"></canvas>
</div>

<script>
    const ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: { /* ... */ },
        options: {
            responsive: true,
            plugins: { legend: { labels: { color: 'rgba(255,255,255,0.70)' } } },
            scales: {
                x: { grid: { color: 'rgba(255,255,255,0.06)' } },
                y: { grid: { color: 'rgba(255,255,255,0.06)' } }
            }
        }
    });
</script>
```

---

## CSS Variables Reference

Access these in your styles:

```css
/* Glass Effects */
--glass-bg              /* Base glass panel */
--glass-bg-hover        /* Hover state */
--glass-border          /* Border color */
--glass-blur            /* Blur amount (20px) */

/* Colors */
--primary: #003366
--primary-light: #0052A3
--secondary: #00A86B
--accent: #F0A500
--danger: #DC3545

/* Text */
--text-primary          /* White */
--text-secondary        /* Light gray (70%) */
--text-muted            /* Gray (45%) */

/* Spacing */
--space-1: 4px
--space-2: 8px
--space-4: 16px
--space-6: 24px
--space-8: 32px

/* Radius */
--radius-md: 12px
--radius-lg: 20px
--radius-full: 9999px
```

---

## Testing Checklist

Before considering a template complete:

- [ ] Glass effects render on all elements
- [ ] Hover states show `translateY(-2px)` + shadow increase
- [ ] Buttons have shimmer effect on hover
- [ ] Input focus shows glow effect
- [ ] Tables have proper hover highlighting
- [ ] Animations load with AOS (staggered delays)
- [ ] Toastify notifications work on form submit
- [ ] Empty states display when no data
- [ ] Mobile responsive (<768px sidebar hides)
- [ ] No console errors
- [ ] Form submissions work with CSRF token

---

## Remaining Templates to Implement

### Public (3 of 5 done)
- [ ] landing.html (with Particles.js) ✅
- [ ] login.html ✅
- [ ] register.html
- [ ] forgot_password.html
- [ ] reset_password.html

### Landlord (15 total)
- [ ] dashboard.html
- [ ] properties_list.html
- [ ] properties_create.html
- [ ] properties_detail.html
- [ ] properties_update.html
- [ ] buildings.html
- [ ] leases.html
- [ ] tenants.html
- [ ] financials.html
- [ ] analytics.html
- [ ] maintenance.html (kanban board)
- [ ] chat.html
- [ ] documents.html
- [ ] notices.html
- [ ] settings.html

### Tenant (10 total)
- [ ] dashboard.html
- [ ] payments.html
- [ ] lease.html
- [ ] maintenance.html
- [ ] chat.html
- [ ] notice_board.html
- [ ] compliance.html
- [ ] payment_methods.html
- [ ] profile.html
- [ ] history.html

---

## Performance Notes

- **Glass blur**: Uses `backdrop-filter: blur(20px)` — may be slow on older devices. Test on mobile.
- **Animations**: AOS library adds scroll listeners — limit to ~50 animated elements per page max
- **Charts**: Chart.js is loaded globally — use `type: 'doughnut'` or `'line'` depending on data
- **Particles.js**: Only use on landing page (single instance) — heavy on CPU

---

**Last Updated:** 2026-05-20  
**Implemented By:** Claude Haiku 4.5  
**Foundation Status:** ✅ Complete (CSS + Base Templates + 2 Auth Pages)
