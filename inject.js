const fs = require('fs');

let hopzie_html = fs.readFileSync('projects/hopzie.html', 'utf8');
let index_html = fs.readFileSync('index.html', 'utf8');

// Extract Performance Reach section
const start_marker = '<!-- 4. Impact (Stats & Partners) -->';
const end_marker = '<!-- Dedicated Creator Marquee -->';

const start_idx = hopzie_html.indexOf(start_marker);
const end_idx = hopzie_html.indexOf(end_marker);

if (start_idx === -1 || end_idx === -1) {
    console.error('Could not find markers in hopzie.html');
    process.exit(1);
}

let impact_html = hopzie_html.substring(start_idx, end_idx);

// --- Redesign adaptations ---
// 1. Margins and padding
impact_html = impact_html.replace('mb-24 max-w-6xl mx-auto px-4 mt-64', 'mt-32 mb-12 max-w-[1100px] mx-auto');

// 2. Section Headings
impact_html = impact_html.replace('text-[#d97706] text-xs font-mono uppercase tracking-widest mb-4 block', 'text-[12px] font-bold text-zinc-500 uppercase tracking-widest mb-3 block');
impact_html = impact_html.replace('text-4xl md:text-5xl font-bold tracking-tight text-zinc-900', 'text-[24px] md:text-[32px] text-black font-normal tracking-tight leading-[1.4]');
impact_html = impact_html.replace('text-zinc-500 text-sm md:text-base font-light mx-auto mt-4 whitespace-nowrap', 'font-sans text-zinc-600 text-[14px] md:text-[15px] font-normal mt-4');

// 3. Card styles
impact_html = impact_html.replace(/glass-card p-8 bg-[a-z]+-500\/\[0\.03\] border-[a-z]+-500\/10 group hover:border-[a-z]+-500\/30/g, 'p-8 bg-zinc-50/50 border border-zinc-200 rounded-[12px] group hover:border-zinc-300 hover:shadow-sm');

// 4. Icon backgrounds
impact_html = impact_html.replace(/bg-[a-z]+-500\/10/g, 'bg-white border border-zinc-200 shadow-sm');

// 5. Text adjustments
impact_html = impact_html.replace(/text-emerald-400/g, 'text-emerald-600');

// 6. Gradients
impact_html = impact_html.replace(/opacity-50 flex-shrink-0/g, 'opacity-30 flex-shrink-0');

// Fix Media Coverage title style
impact_html = impact_html.replace('text-zinc-500 text-xs font-mono uppercase tracking-[0.3em]', 'text-[12px] font-bold text-zinc-500 uppercase tracking-widest block');

// Insert into index.html
const section_end_marker = '<!-- Lectures Section -->';
const section_end_idx = index_html.indexOf(section_end_marker);

if (section_end_idx === -1) {
    console.error('Could not find Lectures Section marker in index.html');
    process.exit(1);
}

const target_str = '</div>\n    </section>';
const insert_idx = index_html.lastIndexOf(target_str, section_end_idx);

if (insert_idx === -1) {
    console.error('Could not find insert position in index.html');
    process.exit(1);
}

const new_index_html = index_html.substring(0, insert_idx) + '\n            ' + impact_html + '\n        ' + index_html.substring(insert_idx);

fs.writeFileSync('index.html', new_index_html, 'utf8');
console.log('Successfully injected Performance Reach section into index.html');
