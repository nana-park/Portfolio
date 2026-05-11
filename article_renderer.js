// Renders the list of articles and handles detail view population

let currentArticlePage = 1;
const articlesPerPage = 3;

function renderArticlesList() {
    const container = document.getElementById('articles-list-container');
    if (!container || typeof articlesData === 'undefined') return;

    if (articlesData.length === 0) {
        container.innerHTML = '<div class="py-8 px-4 lg:px-8 text-center text-zinc-500 font-sans text-sm">No articles found.</div>';
        return;
    }

    const totalPages = Math.ceil(articlesData.length / articlesPerPage);
    if (currentArticlePage < 1) currentArticlePage = 1;
    if (currentArticlePage > totalPages) currentArticlePage = totalPages;

    const startIdx = (currentArticlePage - 1) * articlesPerPage;
    const endIdx = startIdx + articlesPerPage;
    const currentArticles = articlesData.slice(startIdx, endIdx);

    // Add a minimum height wrapper so the pagination controls don't jump when a page has fewer items
    let html = '<div class="flex flex-col min-h-[750px] lg:min-h-[550px]">';
    currentArticles.forEach(article => {
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
            <div class="lg:w-2/6 flex flex-col md:flex-row md:items-center justify-end gap-4">
                <a href="#article-detail?id=${article.id}" onclick="sessionStorage.setItem('articlesScrollY', window.scrollY)" class="shrink-0 px-5 py-2 rounded-full border border-gray-300 font-sans text-[12px] font-semibold text-zinc-900 hover:bg-zinc-100 transition-colors whitespace-nowrap">Read Article</a>
            </div>
        </div>
        `;
    });
    
    html += '</div>'; // Close min-height wrapper

    // Pagination Controls
    if (totalPages > 1) {
        html += `
        <div class="flex justify-center items-center gap-2 mt-12 mb-8 font-sans">
            <button onclick="changeArticlePage(${currentArticlePage - 1})" class="w-8 h-8 flex items-center justify-center rounded-full border border-gray-300 text-gray-500 hover:text-gray-900 hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed transition-colors" ${currentArticlePage === 1 ? 'disabled' : ''}>
                <svg class="w-4 h-4 ml-[-1px]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
            </button>
        `;
        
        // Show max 5 page buttons (simplified logic for small number of pages)
        let startPage = Math.max(1, currentArticlePage - 2);
        let endPage = Math.min(totalPages, startPage + 4);
        if (endPage - startPage < 4) {
            startPage = Math.max(1, endPage - 4);
        }

        for (let i = startPage; i <= endPage; i++) {
            if (i === currentArticlePage) {
                html += `<button class="w-8 h-8 flex items-center justify-center rounded-full bg-zinc-900 text-white text-[13px] font-medium">${i}</button>`;
            } else {
                html += `<button onclick="changeArticlePage(${i})" class="w-8 h-8 flex items-center justify-center rounded-full text-zinc-500 hover:text-zinc-900 hover:bg-gray-100 text-[13px] font-medium transition-colors">${i}</button>`;
            }
        }

        html += `
            <button onclick="changeArticlePage(${currentArticlePage + 1})" class="w-8 h-8 flex items-center justify-center rounded-full border border-gray-300 text-gray-500 hover:text-gray-900 hover:bg-gray-100 disabled:opacity-30 disabled:cursor-not-allowed transition-colors" ${currentArticlePage === totalPages ? 'disabled' : ''}>
                <svg class="w-4 h-4 ml-[1px]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
        </div>
        `;
    }

    container.innerHTML = html;
}

window.changeArticlePage = function(page) {
    currentArticlePage = page;
    renderArticlesList();
    // Scroll smoothly to top of the articles list (not the very top of the page)
    const listContainer = document.getElementById('articles-list-container');
    if (listContainer) {
        // Offset by 100px to account for the fixed navbar
        const offsetPosition = listContainer.getBoundingClientRect().top + window.scrollY - 150;
        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    }
}

function renderArticleDetail(id) {
    if (typeof articlesData === 'undefined') return;
    const article = articlesData.find(a => a.id === id);
    if (!article) return;

    document.getElementById('article-detail-title').textContent = article.title_en;
    document.getElementById('article-detail-meta').textContent = 'Published on ' + article.date;
    
    document.getElementById('article-detail-content').innerHTML = article.body_en;
    
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
    } else if (fullHash === 'articles' && sessionStorage.getItem('articlesScrollY')) {
        const scrollPos = parseInt(sessionStorage.getItem('articlesScrollY'));
        const originalScrollTo = window.scrollTo;
        window.scrollTo = function(x, y) {
            // Check if it's the exact call from script.js resetting scroll
            if (x === 0 && y === 0) {
                originalScrollTo(0, scrollPos);
                window.scrollTo = originalScrollTo; // Restore immediately
                sessionStorage.removeItem('articlesScrollY');
            } else {
                originalScrollTo(x, y);
            }
        };
        // Failsafe restore after 100ms
        setTimeout(() => {
            if (window.scrollTo !== originalScrollTo) {
                window.scrollTo = originalScrollTo;
            }
        }, 100);
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
