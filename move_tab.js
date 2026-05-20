const fs = require('fs');

const htmlPath = 'index.html';
let content = fs.readFileSync(htmlPath, 'utf8');

// 1. Add the new tab button
const tabButtonTarget = `<button
                    class="hopzie-tab-btn px-5 py-2 text-zinc-500 hover:bg-gray-100 hover:text-zinc-900 rounded-full text-[13px] md:text-[14px] font-semibold tracking-tight transition-colors"
                    data-target="tab-resilience">
                    Link Resilience
                </button>
            </div>`;

const newTabButtonStr = `<button
                    class="hopzie-tab-btn px-5 py-2 text-zinc-500 hover:bg-gray-100 hover:text-zinc-900 rounded-full text-[13px] md:text-[14px] font-semibold tracking-tight transition-colors"
                    data-target="tab-resilience">
                    Link Resilience
                </button>
                <button
                    class="hopzie-tab-btn px-5 py-2 text-zinc-500 hover:bg-gray-100 hover:text-zinc-900 rounded-full text-[13px] md:text-[14px] font-semibold tracking-tight transition-colors"
                    data-target="tab-youtube">
                    YouTube Description
                </button>
            </div>`;

content = content.replace(tabButtonTarget, newTabButtonStr);

// 2. Extract the YouTube Description Compare Section
const ytSectionStartStr = '<!-- YouTube Description Compare Section -->';
const ytSectionStartIdx = content.indexOf(ytSectionStartStr);

// Find the end of the style tag for this section
const styleEndStr = '</style>';
let styleEndIdx = content.indexOf(styleEndStr, ytSectionStartIdx);
styleEndIdx = content.indexOf(styleEndStr, styleEndIdx + 1); // wait, is there another style tag? 

// Let's be precise. The section starts with <!-- YouTube Description Compare Section -->
// And ends exactly before </div>\n    </section>\n\n    <!-- Lectures Section -->
// Let's find "<!-- Lectures Section -->"
const lecturesStartIdx = content.indexOf('<!-- Lectures Section -->');
// We need to cut from ytSectionStartStr up to right before "</div>\n    </section>\n\n    <!-- Lectures Section -->"
let cutEndIdx = content.lastIndexOf('</div>', lecturesStartIdx);
cutEndIdx = content.lastIndexOf('</div>', cutEndIdx - 1); // back up

// actually, let's just find "</style>" that follows "youtube-description-compare"
const ytStyleStr = '.youtube-description-compare';
const ytStyleIdx = content.indexOf(ytStyleStr, ytSectionStartIdx);
let ytStyleEndIdx = content.indexOf('</style>', ytStyleIdx);

let ytSectionBlock = content.substring(ytSectionStartIdx, ytStyleEndIdx + 8);
content = content.substring(0, ytSectionStartIdx) + content.substring(ytStyleEndIdx + 8);

// 3. Modify ytSectionBlock to add the grid background back and change styling
ytSectionBlock = ytSectionBlock.replace(
    '<section class="youtube-description-compare mt-4 mb-16">',
    `<div id="tab-youtube" class="hopzie-tab-content hidden mb-12">
      <div class="flex justify-center w-full">
        <section class="youtube-description-compare" style="zoom: 0.8; border-radius: 16px; overflow: hidden; width: 100%;">`
);

// Close the wrapper divs we just added at the end of ytSectionBlock (after </style>)
ytSectionBlock = ytSectionBlock + '\n        </div>\n      </div>\n';

// Replace CSS in ytSectionBlock
ytSectionBlock = ytSectionBlock.replace(
    /box-sizing: border-box;\s*\}/,
    `background: linear-gradient(#f1f1f1 1px, transparent 1px), linear-gradient(90deg, #f1f1f1 1px, transparent 1px);
                background-size: 28px 28px;
                box-sizing: border-box;
              }`
);

// 4. Insert ytSectionBlock before the <script> tag for tabs
const scriptTarget = '<script>\n                document.addEventListener(\'DOMContentLoaded\'';
const scriptIdx = content.indexOf(scriptTarget);

content = content.substring(0, scriptIdx) + ytSectionBlock + '\n            ' + content.substring(scriptIdx);

fs.writeFileSync(htmlPath, content, 'utf8');
console.log('done!');
