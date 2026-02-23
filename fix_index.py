
import os

file_path = r"c:\Users\able2\.gemini\antigravity\scratch\ai-pm-portfolio\index.html"

# Read with fallback encoding
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    try:
        with open(file_path, 'r', encoding='cp1252') as f:
            content = f.read()
    except:
        with open(file_path, 'r', encoding='latin1') as f:
            content = f.read()

# Replacements
replacements = [
    ('??/span>', '</span>'),
    ('??/p>', '</p>'),
    ('??/div>', '</div>'),
    ('div class="card-stars">????????/div>', 'div class="card-stars">★★★★★</div>'),
    ('doesn??', "doesn't"),
    ('??hy', 'why'),
    ('??Present', ' - Present'),
    ('??Dec', ' - Dec'), # Assuming date ranges often break here
    ('hj?n', 'hjʌn'),
    ('b?aŋ', 'b͈aŋ'),
    ('??and', ' and'), # "us ??and yes" -> "us and yes"
    ('??which', ' which'),
    ('??s', "'s"), # "provider??s" -> "provider's"
    # Specifics from FindStr output step 1207
    ('Korea?Japan', 'Korea-Japan'),
    ('shocked us ??and', 'shocked us - and'),
    ('??hy.??', 'why."'),
    ('She doesn?? wait', "She doesn't wait"),
    ('finds it ??and', 'finds it - and'),
    ('knows.??/p>', 'knows."</p>'),
    ('doesn?? drink', "doesn't drink"),
    ('doesn?? like', "doesn't like"),
     # Fix the link with ?????
    ('park-nahyun-?????08314925b', 'park-nahyun-08314925b'), # Just remove garbage if I can't guess
    ('<span>??</span> English', '<span>🇺🇸</span> English'),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write back as UTF-8
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed encoding artifacts.")
