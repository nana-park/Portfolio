import os, random

directory = r'C:\Users\able2\.gemini\antigravity\scratch\Portfolio\nahyun_imported\image_source\About_Life\Culinary'
files = [f for f in os.listdir(directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Shuffle files to prevent similar sequential names from being grouped
random.seed(42)  # For reproducible but seemingly random layout
random.shuffle(files)

aspect_classes = ['aspect-square', 'aspect-[3/4]', 'aspect-[4/5]', 'aspect-video', 'aspect-auto', 'aspect-square', 'aspect-[4/3]']

html_output = '<div class="w-full flex-grow columns-2 md:columns-3 lg:columns-3 gap-3 space-y-3" id="life-gallery">\n'
for i, f in enumerate(files):
    aspect = random.choice(aspect_classes)
    html_output += f'''                        <div class="break-inside-avoid w-full relative group">
                            <img src="nahyun_imported/image_source/About_Life/Culinary/{f}" alt="Culinary Gallery" class="w-full {aspect} object-cover rounded-[3px] hover:opacity-90 cursor-pointer transition-opacity">
                        </div>\n'''
html_output += '                    </div>'
with open('temp_html.txt', 'w', encoding='utf-8') as fh:
    fh.write(html_output)
