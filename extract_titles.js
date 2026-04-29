const fs = require('fs');
let data = fs.readFileSync('articles_data.js', 'utf8');
let jsonStr = data.replace('const articlesData = ', '').trim().replace(/;$/, '');
let articles = JSON.parse(jsonStr);
articles.forEach(a => {
  console.log(`ID: ${a.id}`);
  console.log(`Title: ${a.title_en}`);
  // Extract a brief plain text from body
  let plain = a.body_en.replace(/<[^>]+>/g, '').substring(0, 300);
  console.log(`BodyStart: ${plain}...`);
  console.log('---');
});
