$content = Get-Content index.html -Raw -Encoding UTF8

$pattern = '(?s)// Filter the actual masonry items.*?}\);'
$replacement = @"
                // Filter the actual masonry items and redistribute them across the 3 rigid columns
                const travelGallery = document.getElementById('gallery-col-travel');
                if(travelGallery) {
                    const columns = Array.from(travelGallery.querySelectorAll('.flex.flex-col'));
                    const allItems = Array.from(travelGallery.querySelectorAll('[data-dest]'));
                    
                    const visibleItems = allItems.filter(item => filter === 'All Destinations' || item.getAttribute('data-dest') === filter);
                    const hiddenItems = allItems.filter(item => filter !== 'All Destinations' && item.getAttribute('data-dest') !== filter);
                    
                    hiddenItems.forEach(item => item.classList.add('hidden'));
                    
                    // Re-append visible items evenly across the 3 columns
                    visibleItems.forEach((item, index) => {
                        item.classList.remove('hidden');
                        const targetColIndex = index % columns.length;
                        columns[targetColIndex].appendChild(item);
                    });
                }
"@

$content = $content -replace $pattern, $replacement
Set-Content index.html -Value $content -Encoding UTF8
