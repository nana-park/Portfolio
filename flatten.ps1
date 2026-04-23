$content = Get-Content -Raw -Encoding UTF8 index.html

# The exact target string from JS
$jsOld = "if (gal.id === 'gallery-' + targetId) {
                        gal.classList.remove('hidden');
                        gal.classList.add('grid');"
                        
$jsNew = "if (gal.id === 'gallery-' + targetId) {
                        gal.classList.remove('hidden');
                        if (!gal.classList.contains('columns-2')) { gal.classList.add('grid'); }
                        else { gal.classList.add('block'); }"

$content = $content.Replace($jsOld, $jsNew)


# Now refactor Travel Gallery html structure using regex
# We find everything inside the "travel" div
$pattern = '(?s)(<div id="gallery-col-travel".*?>)(.*?)(?=<!-- Volunteering)'
if ($content -match $pattern) {
    $container = $matches[1]
    $childrenHTML = $matches[2]
    
    $container = $container.Replace("grid-cols-2 md:grid-cols-3", "columns-2 md:columns-3 block")
    
    # Extract only the `.w-full.relative.group` divs, stripping their parent columns
    $itemPattern = '(?s)<div class="w-full relative group.*?(?=<div class="w-full relative group|</div>\s*</div>\s*</div>)'
    # Wait, simple split or specific Match is safer.
}

# Actually, doing it line by line is safer:
$content = $content.Replace('class="right-gallery grid-cols-2 md:grid-cols-3 gap-3 w-full hidden"', 'class="right-gallery columns-2 md:columns-3 gap-3 w-full hidden"')

# Strip out the 3 rigid column wrappers entirely
$content = $content.Replace('<div id="gallery-col-travel" class="right-gallery columns-2 md:columns-3 gap-3 w-full hidden">
                            <div class="flex flex-col gap-3">', '<div id="gallery-col-travel" class="right-gallery columns-2 md:columns-3 gap-3 w-full hidden">')

$content = $content.Replace('                            </div>
                            <div class="flex flex-col gap-3">', '')

# Replace end of the last column before volunteering
$content = $content.Replace('                            </div>
                        </div>
                        
                        <!-- Volunteering Gallery -->', '                        </div>
                        
                        <!-- Volunteering Gallery -->')

# Finally add the inline-block styles to all travel items
$content = $content -replace 'class="w-full relative group overflow-hidden rounded-\[3px\] cursor-default" data-dest', 'class="w-full relative group overflow-hidden rounded-[3px] cursor-default inline-block mb-3 break-inside-avoid" data-dest'

Set-Content -Path index.html -Value $content -Encoding UTF8
