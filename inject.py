import re

hopzie_html = open('projects/hopzie.html', 'r', encoding='utf-8').read()
index_html = open('index.html', 'r', encoding='utf-8').read()

# Extract Performance Reach section
start_marker = '<!-- 4. Impact (Stats & Partners) -->'
end_marker = '<!-- Dedicated Creator Marquee -->'

start_idx = hopzie_html.find(start_marker)
end_idx = hopzie_html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print('Could not find markers in hopzie.html')
    exit(1)

impact_html = hopzie_html[start_idx:end_idx]

# --- Redesign adaptations ---
# 1. Margins and padding
impact_html = impact_html.replace('mb-24 max-w-6xl mx-auto px-4 mt-64', 'mt-32 mb-12 max-w-[1100px] mx-auto')

# 2. Section Headings
impact_html = impact_html.replace('text-[#d97706] text-xs font-mono uppercase tracking-widest mb-4 block', 'text-[12px] font-bold text-zinc-500 uppercase tracking-widest mb-3 block')
impact_html = impact_html.replace('text-4xl md:text-5xl font-bold tracking-tight text-zinc-900', 'text-[24px] md:text-[32px] text-black font-normal tracking-tight leading-[1.4]')
impact_html = impact_html.replace('text-zinc-500 text-sm md:text-base font-light mx-auto mt-4 whitespace-nowrap', 'font-sans text-zinc-600 text-[14px] md:text-[15px] font-normal mt-4')

# 3. Card styles
# Replace glass-card and colored backgrounds with portfolio's clean zinc-50 borders
impact_html = re.sub(r'glass-card p-8 bg-[a-z]+-500/\[0\.03\] border-[a-z]+-500/10 group hover:border-[a-z]+-500/30', 'p-8 bg-zinc-50/50 border border-zinc-200 rounded-[12px] group hover:border-zinc-300 hover:shadow-sm', impact_html)

# 4. Icon backgrounds
impact_html = re.sub(r'bg-[a-z]+-500/10', 'bg-white border border-zinc-200 shadow-sm', impact_html)

# 5. Text adjustments
impact_html = impact_html.replace('text-emerald-400', 'text-emerald-600')

# 6. Gradients for vertical lines (keep them but maybe tone down)
impact_html = impact_html.replace('opacity-50 flex-shrink-0', 'opacity-30 flex-shrink-0')

# Insert into index.html
# Find the end of hopzie-oneclickbuilder section
section_end_marker = '<!-- Lectures Section -->'

section_end_idx = index_html.find(section_end_marker)

if section_end_idx == -1:
    print('Could not find Lectures Section marker in index.html')
    exit(1)

# Find the last closing tag of the container before section_end_marker
insert_idx = index_html.rfind('</div>\n    </section>', 0, section_end_idx)

if insert_idx == -1:
    print('Could not find insert position in index.html')
    exit(1)

new_index_html = index_html[:insert_idx] + impact_html + '\n        ' + index_html[insert_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index_html)

print('Successfully injected Performance Reach section into index.html')
