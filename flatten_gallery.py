import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the Travel gallery use CSS columns instead of rigid flex-cols to allow gapless reflowing during filtering
travel_pattern = r'(<div id="gallery-col-travel".*?>)(.*?)(?=<!-- Volunteering Gallery)'
m = re.search(travel_pattern, html, re.DOTALL)
if m:
    travel_container = m.group(1)
    travel_content = m.group(2)
    
    # 1. Update the container class to use columns instead of grid/flex
    travel_container = travel_container.replace('grid-cols-2 md:grid-cols-3', 'columns-2 md:columns-3 block')
    
    # 2. Extract out all individual img wrappers, removing the 3 rigid column wrappers entirely
    items = re.findall(r'<div class="w-full relative group[^>]*>.*?</div>\s*</div>\s*</div>', travel_content, re.DOTALL)
    
    # 3. Add inline-block and mb-3 break-inside-avoid to each item so they stack nicely in CSS columns
    flattened_items = []
    for item in items:
        new_item = re.sub(r'class="w-full relative group([^"]*)"', r'class="w-full relative group inline-block mb-3 break-inside-avoid\1"', item)
        flattened_items.append(new_item.strip())
        
    flattened_html = "\n".join(flattened_items) + "\n                        </div>\n                        \n                        "
    
    # 4. Replace
    new_travel_block = travel_container + "\n" + "\n".join(["                            " + i for i in flattened_items]) + "\n                        </div>\n                        \n                        "
    
    # Actually just replace the whole extracted match
    full_old = m.group(0)
    html = html.replace(full_old, new_travel_block)

# Also fix the JS behavior for travel-dest-btn filtering so it works properly with css columns 
# (we don't need flex/grid toggles, just block/none)
# wait, the JS already does item.style.display = "block" / "none". That is perfect for columns.
# We also want to make sure JS doesn't add 'grid' to column-based galleries.
js_pattern = r'if \(gal\.id === \'gallery-\' \+ targetId\) \{\s*gal\.classList\.remove\(\'hidden\'\);\s*gal\.classList\.add\(\'grid\'\);'
js_fixed = r'''if (gal.id === 'gallery-' + targetId) {
                        gal.classList.remove('hidden');
                        if (!gal.classList.contains('columns-2')) gal.classList.add('grid');
                        else gal.classList.add('block');'''
html = re.sub(js_pattern, js_fixed, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
