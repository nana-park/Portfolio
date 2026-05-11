const fs = require('fs');
let content = fs.readFileSync('script.js', 'utf8');
const searchStr = '            currentIndex = index;\n        };';
const idx = content.indexOf(searchStr);
if (idx !== -1) {
    const endStr = '// Expertise Section Navigation';
    const endIdx = content.indexOf(endStr);
    
    const newCode = \            currentIndex = index;
        };

        const scrollToCard = (index) => {
            if (index < 0) index = 0;
            if (index > cards.length - 1) index = cards.length - 1;
            const card = cards[index];
            const scrollPos = card.offsetLeft - (container.offsetWidth / 2) + (card.offsetWidth / 2);
            container.scrollTo({ left: scrollPos, behavior: 'smooth' });
            updateActiveState(index);
        };

        if (prevBtn) {
            prevBtn.addEventListener('click', () => { scrollToCard(currentIndex - 1); });
        }
        if (nextBtn) {
            nextBtn.addEventListener('click', () => { scrollToCard(currentIndex + 1); });
        }

        let initializedScroll = false;
        const initScroll = () => {
            if (!initializedScroll && container && cards[currentIndex] && container.offsetWidth > 0) {
                initializedScroll = true;
                const card = cards[currentIndex];
                const scrollPos = card.offsetLeft - (container.offsetWidth / 2) + (card.offsetWidth / 2);
                container.scrollTo({ left: scrollPos, behavior: 'auto' });
                updateActiveState(currentIndex);
            }
        };

        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) { initScroll(); }
        }, { threshold: 0.1 });
        observer.observe(container);
        setTimeout(initScroll, 100);
        setTimeout(initScroll, 500);

        cards.forEach((card, index) => {
            card.addEventListener('click', () => {
                if (currentIndex === index) { scrollToCard(index + 1); }
                else { scrollToCard(index); }
            });
        });

        let isScrolling;
        container.addEventListener('scroll', () => {
            window.clearTimeout(isScrolling);
            isScrolling = setTimeout(() => {
                const containerRect = container.getBoundingClientRect();
                const center = containerRect.left + containerRect.width / 2;
                let closestIndex = 0;
                let minDiff = Infinity;
                cards.forEach((card, idx) => {
                    const rect = card.getBoundingClientRect();
                    const cardCenter = rect.left + rect.width / 2;
                    const diff = Math.abs(center - cardCenter);
                    if (diff < minDiff) { minDiff = diff; closestIndex = idx; }
                });
                if (closestIndex !== currentIndex) { updateActiveState(closestIndex); }
            }, 50);
        }, { passive: true });
    }
});

// ===========================
\;
    content = content.substring(0, idx) + newCode + content.substring(endIdx);
    fs.writeFileSync('script.js', content, 'utf8');
    console.log('Fixed!');
} else {
    console.log('Search string not found');
}
