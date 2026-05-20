const fs = require('fs');

let content = fs.readFileSync('script.js', 'utf8');

// 1. routerConfig
content = content.replace(
    "'article-detail': ['article-detail'],",
    "'article-detail': ['article-detail'],\n    'hopzie-oneclickbuilder': ['hopzie-oneclickbuilder'],"
);

// 2. parentMap
content = content.replace(
    "'article-detail': 'projects'",
    "'article-detail': 'projects',\n        'hopzie-oneclickbuilder': 'projects'"
);

// 3. lightPages
content = content.replace(
    "const lightPages = ['life', 'projects', 'research', 'articles', 'article-detail', 'awards', 'contact'];",
    "const lightPages = ['life', 'projects', 'research', 'articles', 'article-detail', 'hopzie-oneclickbuilder', 'awards', 'contact'];"
);

// 4. scroll logic
const oldScroll = `    // Handle scroll position (Top for main tabs, smooth scroll for sub-sections)
    if (activeTab === targetSection) {
        window.scrollTo(0, 0);
    } else {`;
    
const newScroll = `    // Handle scroll position (Top for main tabs, smooth scroll for sub-sections)
    if (activeTab === targetSection) {
        if (activeTab === 'projects' && sessionStorage.getItem('projectsScrollY')) {
            const scrollPos = parseInt(sessionStorage.getItem('projectsScrollY'));
            setTimeout(() => { window.scrollTo(0, scrollPos); }, 10);
            sessionStorage.removeItem('projectsScrollY');
        } else {
            window.scrollTo(0, 0);
        }
    } else {`;

content = content.replace(oldScroll, newScroll);

fs.writeFileSync('script.js', content, 'utf8');
console.log('Done');
