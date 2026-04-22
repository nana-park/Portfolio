const fs = require('fs');

const dir = 'C:\\Users\\able2\\.gemini\\antigravity\\scratch\\Portfolio\\nahyun_imported\\image_source\\About_Life\\Culinary';
let files = fs.readdirSync(dir).filter(f => f.toLowerCase().endsWith('.jpg'));

// Required sequences
const top1 = 'KakaoTalk_20260422_235853863_06.jpg';
const top2 = 'KakaoTalk_20260422_235853863_07.jpg';
const top3 = 'KakaoTalk_20260422_235853863_08.jpg';
const row2_col1 = 'KakaoTalk_20260423_004121914.jpg';
const pair1 = 'KakaoTalk_20260422_235853863_10.jpg';
const pair2 = 'KakaoTalk_20260422_235853863_09.jpg';

const required = [top1, top2, top3, row2_col1, pair1, pair2];
// Remove them from general shuffle pool
files = files.filter(f => !required.includes(f));

// Shuffle remainder
files.sort(() => Math.random() - 0.5);

// Build 3 columns
let col1 = [top1, row2_col1];
let col2 = [top2, pair1];
let col3 = [top3, pair2];

// Distribute the remaining files evenly
files.forEach((f, index) => {
    if (index % 3 === 0) col1.push(f);
    else if (index % 3 === 1) col2.push(f);
    else col3.push(f);
});

function generateColHtml(imgArray) {
    let html = `                        <div class="flex flex-col gap-3">\n`;
    imgArray.forEach(f => {
        // Just use natural aspect ratio if it's already masonry! Because flex-col with gap-3 will naturally stack them based on width=100% and height=auto!
        // No need for aspect-[X], just w-full h-auto! It perfectly mimics masonry without the clipping issue!
        html += `                            <div class="w-full relative group">
                                <img src="nahyun_imported/image_source/About_Life/Culinary/${f}" alt="Culinary Gallery" class="w-full h-auto rounded-[3px] hover:opacity-90 cursor-pointer transition-opacity">
                            </div>\n`;
    });
    html += `                        </div>\n`;
    return html;
}

let final_html = `<div class="grid grid-cols-2 md:grid-cols-3 gap-3 w-full flex-grow" id="life-gallery">\n`;
final_html += generateColHtml(col1);
final_html += generateColHtml(col2);
// For mobile col 3 might hide or wrap, but we assume md:grid-cols-3
final_html += generateColHtml(col3);
final_html += `                    </div>`;

fs.writeFileSync('temp_html.txt', final_html);
