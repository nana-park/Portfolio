import json

with open('articles_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content[content.find('['): content.rfind(']')+1]
articles = json.loads(json_str)

for i, a in enumerate(articles):
    print(f"{i}: {a['title_ko']} => {a['title_en']}")
