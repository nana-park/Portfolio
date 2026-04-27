// Renders the list of articles and handles detail view population

function renderArticlesList() {
    const container = document.getElementById('articles-list-container');
    if (!container || typeof articlesData === 'undefined') return;

    if (articlesData.length === 0) {
        container.innerHTML = '<div class="py-8 px-4 lg:px-8 text-center text-zinc-500 font-sans text-sm">No articles found.</div>';
        return;
    }

    let html = '';
    articlesData.forEach(article => {
        // Date formatting (e.g. "2024.05.01" to "May 2024")
        let dateDisplay = article.date;
        if (dateDisplay.includes('.')) {
            const parts = dateDisplay.split('.');
            if (parts.length >= 2) {
                const year = parts[0];
                const month = new Date(year, parseInt(parts[1]) - 1).toLocaleString('en-US', { month: 'long' });
                dateDisplay = `${month} ${year}`;
            }
        }

        html += `
        <div class="py-8 px-4 lg:px-8 border-b border-gray-200 flex flex-col lg:flex-row gap-4 lg:gap-8 hover:bg-gray-50 transition-colors">
            <div class="lg:w-1/6 shrink-0 mt-0.5"><span class="font-sans text-zinc-500 text-[12px] font-medium">${dateDisplay}</span></div>
            <div class="lg:w-3/6 shrink-0 flex flex-col justify-start">
                <h3 class="font-sans text-[16px] md:text-[18px] font-medium text-zinc-900 tracking-tight mb-2 leading-snug">${article.title_en}</h3>
                <p class="font-sans text-zinc-600 text-[13px] leading-relaxed mb-4">${article.excerpt}</p>
            </div>
            <div class="lg:w-2/6 flex flex-col md:flex-row items-end justify-end gap-4 mt-auto">
                <a href="#article-detail?id=${article.id}" class="shrink-0 px-5 py-2 rounded-full border border-gray-300 font-sans text-[12px] font-medium text-zinc-900 hover:bg-zinc-100 transition-colors whitespace-nowrap lg:self-end">Read Article</a>
            </div>
        </div>
        `;
    });

    container.innerHTML = html;
}

function renderArticleDetail(id) {
    if (typeof articlesData === 'undefined') return;
    const article = articlesData.find(a => a.id === id);
    if (!article) return;

    document.getElementById('article-detail-title').textContent = article.title_en;
    document.getElementById('article-detail-meta').textContent = 'Published on ' + article.date;
    
    // Convert body newlines to paragraphs
    const paragraphs = article.body_en.split('\n\n').filter(p => p.trim() !== '');
    let bodyHtml = '';
    paragraphs.forEach(p => {
        bodyHtml += `<p>${p}</p>`;
    });
    document.getElementById('article-detail-content').innerHTML = bodyHtml;
    
    document.getElementById('article-original-link').href = article.url;
}

function backToArticles() {
    window.location.hash = '#articles';
}

// Hook into hashchange to render detail if needed
window.addEventListener('hashchange', () => {
    let fullHash = window.location.hash.replace('#', '');
    if (fullHash.startsWith('article-detail?id=')) {
        let id = fullHash.split('id=')[1];
        renderArticleDetail(id);
    }
});

// Run on load
document.addEventListener('DOMContentLoaded', () => {
    renderArticlesList();
    let fullHash = window.location.hash.replace('#', '');
    if (fullHash.startsWith('article-detail?id=')) {
        let id = fullHash.split('id=')[1];
        renderArticleDetail(id);
    }
});
