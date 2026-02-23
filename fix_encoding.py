import re

file_path = r'C:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# Fix date ranges: ??2024.07 -> - 2024.07
content = re.sub(r'\?\?(\d{4}\.\d{2})', r' - \1', content)

# Fix conference dates: ??May -> - May, etc.
content = re.sub(r'\?\?(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\s)', r' - \1\2', content)

# Fix LinkedIn URLs with Korean chars - multiple variants
content = re.sub(r'park-nahyun-[^\s"]+08314925b', 'park-nahyun-08314925b', content)
content = re.sub(r'park-nahyun-[^\s"]+08304925b', 'park-nahyun-08314925b', content)

# Fix writing ??weaving -> writing, weaving
content = content.replace('writing ??weaving', 'writing, weaving')

# Fix ??driving -> driving
content = content.replace('??driving', 'driving')

# Fix ??why.?? -> "why."
content = content.replace('??why.??', '"why."')

# Fix remaining ?? patterns that are em-dashes
content = content.replace('??', ' - ')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done. Original length: {original_len}, New length: {len(content)}')
