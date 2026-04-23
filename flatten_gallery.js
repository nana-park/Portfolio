const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// Pattern to match Travel gallery
const travelPattern = /(<div id="gallery-col-travel".*?>)([\s\S]*?)(?=<!-- Volunteering Gallery)/;
const match = html.match(travelPattern);

if (match) {
    let container = match[1];
    let content = match[2];
    
    // Update container to columns
    container = container.replace('grid-cols-2 md:grid-cols-3', 'columns-2 md:columns-3 block');
    
    // Regex to grab each individual item out of the rigid columns
    // We match the w-full relative group... down to its closing div (2 levels deep)
    const items = [...content.matchAll(/<div class="w-full relative group[^>]*>[\s\S]*?<\/div>[\s\S]*?<\/div>[\s\S]*?<\/div>/g)].map(m => m[0]);
    
    let flattened = [];
    for(let item of items) {
        // Add mb-3 break-inside-avoid to each item container
        item = item.replace('class="w-full relative group', 'class="w-full relative group inline-block mb-3 break-inside-avoid');
        flattened.push('                            ' + item);
    }
    
    let newBlock = container + '\n' + flattened.join('\n') + '\n                        </div>\n                        \n                        ';
    
    html = html.replace(match[0], newBlock);
}

const jsPattern = /if \(gal\.id === 'gallery-' \+ targetId\) \{\s*gal\.classList\.remove\('hidden'\);\s*gal\.classList\.add\('grid'\);/g;
const jsFixed = `if (gal.id === 'gallery-' + targetId) {
                        gal.classList.remove('hidden');
                        if (!gal.classList.contains('columns-2')) gal.classList.add('grid');
                        else gal.classList.add('block');`;

html = html.replace(jsPattern, jsFixed);

fs.writeFileSync('index.html', html, 'utf8');
console.log("Done");
