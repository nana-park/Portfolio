import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Show what broken patterns look like
import re
broken = re.findall(r'[^\x00-\x7F\u0080-\uFFFF]?.{0,5}', content)

# Find all occurrences of replacement character or similar broken chars
# The broken chars appear as ?· or similar - let's find them
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    if '?' in line and ('★' in line or 'Human' in line or "Women" in line or "Korea" in line or "why" in line or "doesn" in line):
        print(f"Line {i}: {repr(line[:120])}")
