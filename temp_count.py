import json
with open('articles_data.js', encoding='utf-8') as f:
    data = f.read()
data = data.replace('const articlesData = ', '').strip().rstrip(';')
articles = json.loads(data)
print(f"Total articles: {len(articles)}")
for i, a in enumerate(articles[:5]):
    print(f"{i}: {a['title_en']}")
