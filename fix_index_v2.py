
import os
import sys

file_path = r"c:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"

print(f"Reading {file_path}...")

# Read with fallback encoding
content = ""
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print("Read as UTF-8")
except UnicodeDecodeError:
    print("UTF-8 failed, trying cp1252")
    try:
        with open(file_path, 'r', encoding='cp1252') as f:
            content = f.read()
    except Exception as e:
        print(f"cp1252 failed: {e}")
        # Last resort: binary read and decode with ignore
        with open(file_path, 'rb') as f:
            content = f.read().decode('utf-8', errors='replace')
        print("Read as binary with replacement")

# Replacements
replacements = [
    ('??/span>', '</span>'),
    ('??/p>', '</p>'),
    ('??/div>', '</div>'),
    ('div class="card-stars">????????/div>', 'div class="card-stars">★★★★★</div>'),
    ('doesn??', "doesn't"),
    ('??hy', 'why'),
    ('??Present', ' - Present'),
    ('??Dec', ' - Dec'),
    ('hj?n', 'hjʌn'),
    ('b?aŋ', 'b͈aŋ'),
    ('??and', ' and'),
    ('??which', ' which'),
    ('??s', "'s"),
    ('Korea?Japan', 'Korea-Japan'),
    ('shocked us ??and', 'shocked us - and'),
    ('??hy.??', 'why."'),
    ('She doesn?? wait', "She doesn't wait"),
    ('finds it ??and', 'finds it - and'),
    ('knows.??/p>', 'knows."</p>'),
    ('doesn?? drink', "doesn't drink"),
    ('doesn?? like', "doesn't like"),
    ('park-nahyun-?????08314925b', 'park-nahyun-08314925b'),
    ('<span>??</span> English', '<span>🇺🇸</span> English'),
    ('VIEW PUBLICATION ??/span>', 'VIEW PUBLICATION </span>'), # Fix specific case from screenshot
    ('??/SPAN>', '</span>'), # Case sensitivity check
]

# Apply replacements
count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        count += 1
        print(f"Replaced: {old} -> {new}")

print(f"Total patterns replaced: {count}")

# Write back as UTF-8
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully wrote back to index.html")
except Exception as e:
    print(f"Error writing file: {e}")
    sys.exit(1)
