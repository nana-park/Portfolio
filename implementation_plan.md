# Refactoring Hopzie Project Plan

## Goal
Refactor `projects/hopzie.html` to follow the "Problem - Action - Result" (PAR) storytelling framework, matching the style of other portfolio projects.

## Proposed Changes

### Content Restructuring
- **Current Sections**: Overview, Key Responsibilities, Impact, Key Features.
- **New Sections**:
  - **Problem**: Challenge description (from Notion/PPT).
  - **Action**: What was done (Design, Logic, Dev).
  - **Result**: Outcome (Metrics, Success).

### Content Restructuring (Legend Style)
- **Hero**: Minimalist, high-impact title with "Problem" statement immediately visible.
- **Bento Grid Layout**: Use a bento-box grid for "Action" and "Features" to showcase the AI automated process.
- **Stats**: Large, bold numbers for "Result" section.
- **Visuals**: Placeholders for "Dashboard UI", "Process Flow", and "Mobile App View".

### File: `projects/hopzie.html`
- implement CSS Grid for Bento layout.
- Use `glass-panel` with different spans (col-span-2, row-span-2) for visual interest.
- Ensure responsive design (stack on mobile, grid on desktop).

## Verification
- **Manual**: Open `projects/hopzie.html` in browser.
- **Check**:
  - Sections "Problem", "Action", "Result" are visible.
  - Styling matches `style.css` variables.
  - Navigation works.
