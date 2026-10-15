# Landing Page Overrides

> **PROJECT:** Street Corner Eats
> **Generated:** 2026-10-15 16:58:56
> **Page Type:** Landing / Marketing

> ⚠️ **IMPORTANT:** Rules in this file **override** the Master file (`design-system/MASTER.md`).
> Only deviations from the Master are documented here. For all other rules, refer to the Master.

---

## Page-Specific Rules

### Layout Overrides

- **Max Width:** 1200px (standard)
- **Layout:** Full-width sections, centered content
- **Sections:** Hero > Step 1 (problem) > Step 2 (solution) > Step 3 (action) > CTA progression

### Spacing Overrides

- No overrides — use Master spacing

### Typography Overrides

- No overrides — use Master typography

### Color Overrides

- **Strategy:** Step colors: 1 (Red/Problem), 2 (Orange/Process), 3 (Green/Solution). CTA: Brand color

### Component Overrides

- Avoid: Ignore accessibility motion settings
- Avoid: Animate everything that moves
- Avoid: Force scroll effects

---

## Page-Specific Components

- No unique components for this page

---

## Recommendations

- Effects: @keyframes text animation, typing effect, background-clip: text, GSAP ScrollTrigger, split text
- Animation: Check prefers-reduced-motion media query
- Animation: Animate 1-2 key elements per view maximum
- Accessibility: Honor prefers-reduced-motion and present the final readable state without parallax or scroll-jacking
- CTA Placement: Each step: mini-CTA. Final: main CTA
