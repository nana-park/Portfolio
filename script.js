// ===========================
// Typing Animation
// ===========================
const typedTextElement = document.getElementById('typedText');
const textArray = [
    'AI Chatbot Product Manager',
    'Conversational AI Specialist',
    'Human-AI Interaction Designer'
];
let textArrayIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typingDelay = 100;
let erasingDelay = 50;
let newTextDelay = 2000;

function type() {
    const currentText = textArray[textArrayIndex];

    if (isDeleting) {
        typedTextElement.textContent = currentText.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typedTextElement.textContent = currentText.substring(0, charIndex + 1);
        charIndex++;
    }

    if (!isDeleting && charIndex === currentText.length) {
        isDeleting = true;
        setTimeout(type, newTextDelay);
        return;
    }

    if (isDeleting && charIndex === 0) {
        isDeleting = false;
        textArrayIndex = (textArrayIndex + 1) % textArray.length;
    }

    const delay = isDeleting ? erasingDelay : typingDelay;
    setTimeout(type, delay);
}

// Start typing animation when page loads (disabled — replaced by role-flipper)
document.addEventListener('DOMContentLoaded', () => {
    if (typedTextElement) setTimeout(type, 1000);
});

// ===========================
// Navbar Scroll Effect
// ===========================
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }

    lastScroll = currentScroll;
});

// ===========================
// Mobile Menu Toggle
// ===========================
const mobileToggle = document.getElementById('mobileToggle');
const navMenu = document.getElementById('navMenu');

mobileToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    mobileToggle.classList.toggle('active');
});

// Close mobile menu when clicking on a link
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        mobileToggle.classList.remove('active');
    });
});

// ===========================
// Smooth Scroll
// ===========================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            const offsetTop = target.offsetTop - 80;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// ===========================
// Scroll Animations
// ===========================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('reveal');
        }
    });
}, observerOptions);

// Observe all cards and sections
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll(
        '.project-card, .highlight-card, .skill-category, .contact-card, .cert-card, .expertise-card'
    );

    animatedElements.forEach(el => {
        observer.observe(el);
    });
});

// ===========================
// Project Card Interactions
// ===========================
const projectCards = document.querySelectorAll('.project-card');

projectCards.forEach(card => {
    card.addEventListener('mouseenter', function () {
        this.style.zIndex = '10';
    });

    card.addEventListener('mouseleave', function () {
        this.style.zIndex = '1';
    });
});

// ===========================
// Dynamic Background Gradient
// ===========================
let mouseX = 0;
let mouseY = 0;

document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX / window.innerWidth;
    mouseY = e.clientY / window.innerHeight;
});

function animateGradient() {
    const orb1 = document.querySelector('.orb-1');
    const orb2 = document.querySelector('.orb-2');
    const orb3 = document.querySelector('.orb-3');

    if (orb1 && orb2 && orb3) {
        const offsetX = mouseX * 50;
        const offsetY = mouseY * 50;

        orb1.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
        orb2.style.transform = `translate(${-offsetX}px, ${-offsetY}px)`;
        orb3.style.transform = `translate(${offsetX * 0.5}px, ${offsetY * 0.5}px)`;
    }

    requestAnimationFrame(animateGradient);
}

animateGradient();

// Parallax Effect Removed (Fixed layout issues)


// ===========================
// Add Active State to Nav Links
// ===========================
const sections = document.querySelectorAll('section[id]');

function highlightNavLink() {
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

        if (navLink) {
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navLink.classList.add('active');
            } else {
                navLink.classList.remove('active');
            }
        }
    });
}

window.addEventListener('scroll', highlightNavLink);

// ===========================
// Performance Optimization
// ===========================
// Lazy load images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src || img.src;
                img.classList.add('loaded');
                observer.unobserve(img);
            }
        });
    });

    document.querySelectorAll('img').forEach(img => {
        imageObserver.observe(img);
    });
}

// ===========================
// Console Easter Egg
// ===========================
console.log('%cHello, curious developer!', 'font-size: 20px; color: #667eea; font-weight: bold;');
console.log('%cThis portfolio was built by Nahyun Park', 'font-size: 14px; color: #a5b4fc;');
console.log('%cInterested in AI chatbot product management? Let\'s connect!', 'font-size: 12px; color: #7dd3fc;');

// ===========================
// Project Modal System
// ===========================
const projectData = {
    'carecall': {
        title: 'CLOVA CareCall',
        subtitle: 'Senior Care AI Call-bot for Korea & Japan',
        period: 'October 2023 - Present',
        company: 'NAVER CLOUD',
        category: 'Healthcare AI',
        overview: 'AI-powered call-bot designed specifically for senior care services in Korea and Japan, providing intelligent call routing, transfer/waiting flows, and optimized user experience for elderly users.',
        responsibilities: [
            'Enhanced user routing system for efficient call distribution',
            'Designed call transfer and waiting flows for caregiver pickup',
            'Architected lightweight chatbot system optimized for senior users',
            'Eliminated abnormal termination issues through robust error handling',
            'Fine-tuned EPD (End of Phrase Detection) for senior speech patterns',
            'Localized service for both Korean and Japanese markets'
        ],
        technologies: ['Conversational AI', 'Voice UX', 'NLP', 'Healthcare Tech', 'EPD Tuning', 'Localization (JP/KR)', 'Service Architecture'],
        customSections: [
            {
                title: 'Scenario',
                content: 'Designed comprehensive call scenarios for senior care services including health check-ins, appointment reminders, medication alerts, and emergency response protocols. Created user-friendly conversation flows that accommodate varying levels of tech literacy among elderly users.'
            },
            {
                title: 'Console',
                content: 'Developed intuitive admin console for caregivers and service providers to monitor call activities, manage user profiles, configure call routing rules, and access real-time analytics. Implemented dashboard with key metrics including call success rates, user engagement, and service quality indicators.'
            },
            {
                title: 'Chatbot',
                content: 'Built lightweight chatbot architecture optimized for voice interactions with seniors. Features include natural language understanding tuned for elderly speech patterns, context-aware responses, graceful error handling, and seamless handoff to human caregivers when needed. Supports both Korean and Japanese languages with cultural adaptations.'
            }
        ],
        achievements: [
            {
                title: 'OSAKA Expo 2025 Digital Human Showcase',
                description: 'Leading the cutting-edge digital human video call showcase at OSAKA Expo 2025, featuring WebRTC barge-in technology that demonstrates the future of AI-human interaction on a global stage.',
                period: '2024 - 2025',
                technologies: ['Digital Human', 'WebRTC', 'Real-time AI', 'Barge-in Technology']
            }
        ],
        impact: 'Improved senior care accessibility and quality of service through AI-powered communication, serving thousands of elderly users across Korea and Japan with culturally-adapted conversational experiences.'
    },
    'lineworks': {
        title: 'LINE WORKS AiCall',
        subtitle: 'AI Contact Center for Japan Market',
        period: 'October 2023 - Present',
        company: 'NAVER CLOUD',
        category: 'Enterprise AI',
        overview: 'Enterprise-grade AI Contact Center solution designed for the Japanese market, enabling businesses to automate customer support with intelligent call routing, analytics, and seamless integration with LINE WORKS platform.',
        responsibilities: [
            'Led service planning and development for B2B voice AI solutions',
            'Expanded AI Contact Center (Voice IVR) services across Japan, US, and Korea',
            'Designed intelligent call routing and distribution systems',
            'Implemented call analytics and reporting features',
            'Collaborated with LINE WORKS team for platform integration',
            'Conducted market research for Japanese enterprise needs'
        ],
        technologies: ['Contact Center AI', 'Voice IVR', 'Call Analytics', 'Enterprise SaaS', 'B2B Solutions', 'Japan Market Localization'],
        impact: 'Enabled Japanese enterprises to scale customer support operations efficiently, reducing operational costs while improving customer satisfaction through AI-powered automation.',
        keyFeatures: [
            'Intelligent call routing and queue management',
            'Real-time call analytics and insights',
            'Multi-language support (Japanese, English, Korean)',
            'Seamless LINE WORKS integration',
            'Customizable voice AI responses',
            'Enterprise-grade security and compliance'
        ]
    },
    'adot': {
        title: 'A. (Adot)',
        subtitle: 'Personal AI Chatbot Assistant',
        period: 'April 2024 - July 2024',
        company: 'SK Telecom',
        category: 'Consumer AI',
        overview: 'Personal AI chatbot assistant for SK Telecom users, providing personalized daily assistance, schedule management, and conversational support with domain-specific agent capabilities.',
        responsibilities: [
            'Improved personal AI chatbot assistant functionality',
            'Developed "Agent for each domain" specialized capabilities',
            'Enhanced general chatbot assistant features',
            'Implemented personalization algorithms',
            'Designed conversational flows for daily tasks',
            'Conducted user testing and feedback integration'
        ],
        technologies: ['Personal AI', 'Conversational AI', 'NLP', 'Mobile App', 'Personalization', 'Product Management'],
        keyFeatures: [
            'Domain-specific AI agents (schedule, reminders, information)',
            'Personalized recommendations based on user behavior',
            'Natural language understanding for Korean users',
            'Mobile-first design and experience',
            'Integration with SK Telecom services',
            'Context-aware conversations'
        ],
        impact: 'Enhanced daily productivity for SK Telecom users through intelligent, personalized AI assistance that adapts to individual needs and preferences.'
    },
    'hopzie': {
        title: 'Hopzie',
        subtitle: 'AI-Powered Automated Online Store',
        period: 'January 2023 - December 2023',
        company: 'AI-based App Launch Initiative',
        category: 'E-commerce AI',
        overview: 'AI-powered automated online store for sponsored products, developed in collaboration with Google and SKT. Features intelligent product curation and automated store management.',
        responsibilities: [
            'Led product management for AI-based e-commerce platform',
            'Collaborated with Google and SKT on partnership initiatives',
            'Designed automated product curation algorithms',
            'Implemented intelligent store management features',
            'Developed sponsored product recommendation system',
            'Managed cross-functional team coordination'
        ],
        technologies: ['AI E-commerce', 'Product Management', 'Automation', 'Recommendation Systems', 'Partnership Management'],
        keyFeatures: [
            'Automated product selection and curation',
            'AI-driven inventory management',
            'Sponsored product integration',
            'Smart pricing optimization',
            'Automated marketing and promotions',
            'Analytics and performance tracking'
        ],
        impact: 'Streamlined e-commerce operations for sponsored products, enabling efficient automated store management with AI-powered product curation and optimization.'
    },
    'justdoit': {
        title: 'Just do it',
        subtitle: 'AI Exercise Management & Fitness Tracking',
        period: 'January 2023 - December 2023',
        company: 'AI-based App Launch Initiative',
        category: 'Health & Fitness AI',
        overview: 'AI-based exercise management and fitness tracking application featuring smart workout planning, progress tracking, and personalized fitness recommendations powered by AI.',
        responsibilities: [
            'Led product development for AI fitness application',
            'Designed personalized workout recommendation engine',
            'Implemented progress tracking and analytics features',
            'Developed AI-powered exercise form guidance',
            'Created motivational engagement systems',
            'Conducted user research and testing'
        ],
        technologies: ['Health Tech', 'Fitness AI', 'Mobile App', 'Product Management', 'Personalization', 'Analytics'],
        keyFeatures: [
            'AI-powered personalized workout plans',
            'Real-time exercise tracking and feedback',
            'Progress analytics and visualization',
            'Adaptive difficulty adjustment',
            'Motivational goal-setting system',
            'Social features for community engagement'
        ],
        impact: 'Empowered users to achieve fitness goals through personalized AI-driven workout plans and intelligent progress tracking, making exercise more accessible and effective.'
    },
    'metaverse': {
        title: 'Metaverse Bookclub',
        subtitle: 'AI-Driven Virtual Reading Platform',
        period: 'September 2022 - February 2023',
        company: 'Sungkyunkwan University (in collaboration with SK)',
        category: 'Metaverse & AI',
        overview: 'AI-driven book club service in a metaverse platform, developed in collaboration with SK. Features immersive virtual reading experiences with AI-powered recommendations. Excellence Prize winner.',
        responsibilities: [
            'Planned and developed metaverse platform for book club',
            'Designed AI-driven book recommendation system',
            'Created immersive virtual reading environments',
            'Implemented social features for virtual book discussions',
            'Collaborated with SK on digital transformation initiatives',
            'Led UX design for metaverse interactions'
        ],
        technologies: ['Metaverse', 'AI UX', 'Digital Transformation', 'Recommendation Systems', 'VR/AR', 'Social Platform'],
        keyFeatures: [
            'Virtual reality book club environments',
            'AI-powered book recommendations',
            'Immersive reading experiences',
            'Social discussion spaces',
            'Avatar-based interactions',
            'Digital library integration'
        ],
        achievements: [
            {
                title: 'Excellence Prize',
                description: 'Received Excellence Prize for innovative approach to combining AI, UX design, and metaverse technology for educational and social purposes.'
            }
        ],
        impact: 'Pioneered innovative approach to social reading experiences by combining metaverse technology with AI-driven recommendations, creating engaging virtual communities for book enthusiasts.'
    }
};

// Modal elements
const modal = document.getElementById('projectModal');
const modalBody = document.getElementById('modalBody');
const modalClose = document.getElementById('modalClose');
const modalOverlay = document.querySelector('.modal-overlay');

// Function to create modal content
function createModalContent(projectKey) {
    const project = projectData[projectKey];
    if (!project) return '';

    let achievementsHTML = '';
    if (project.achievements && project.achievements.length > 0) {
        achievementsHTML = `
            <div class="modal-section">
                <h3>Key Achievements</h3>
                ${project.achievements.map(achievement => `
                    <div class="modal-highlight-box">
                        <h4>${achievement.title}</h4>
                        <p>${achievement.description}</p>
                        ${achievement.period ? `<p><strong>Period:</strong> ${achievement.period}</p>` : ''}
                        ${achievement.technologies ? `
                            <div class="modal-tech-tags">
                                ${achievement.technologies.map(tech => `<span class="modal-tech-tag">${tech}</span>`).join('')}
                            </div>
                        ` : ''}
                    </div>
                `).join('')}
            </div>
        `;
    }

    let keyFeaturesHTML = '';
    if (project.keyFeatures && project.keyFeatures.length > 0) {
        keyFeaturesHTML = `
            <div class="modal-section">
                <h3>Key Features</h3>
                <ul>
                    ${project.keyFeatures.map(feature => `<li>${feature}</li>`).join('')}
                </ul>
            </div>
        `;
    }

    let customSectionsHTML = '';
    if (project.customSections && project.customSections.length > 0) {
        customSectionsHTML = project.customSections.map(section => `
            <div class="modal-section">
                <h3>${section.title}</h3>
                <p>${section.content}</p>
            </div>
        `).join('');
    }

    return `
        <div class="modal-header">
            <h2 class="modal-title">${project.title}</h2>
            <p class="modal-subtitle">${project.subtitle}</p>
            <div class="modal-meta">
                <span>📅 ${project.period}</span>
                <span>🏢 ${project.company}</span>
                <span>🏷️ ${project.category}</span>
            </div>
        </div>

        <div class="modal-section">
            <h3>Overview</h3>
            <p>${project.overview}</p>
        </div>

        ${project.responsibilities ? `
            <div class="modal-section">
                <h3>Key Responsibilities</h3>
                <ul>
                    ${project.responsibilities.map(resp => `<li>${resp}</li>`).join('')}
                </ul>
            </div>
        ` : ''}

        ${customSectionsHTML}
        ${keyFeaturesHTML}
        ${achievementsHTML}

        <div class="modal-section">
            <h3>Technologies & Skills</h3>
            <div class="modal-tech-tags">
                ${project.technologies.map(tech => `<span class="modal-tech-tag">${tech}</span>`).join('')}
            </div>
        </div>

        ${project.impact ? `
            <div class="modal-section">
                <h3>Impact</h3>
                <p>${project.impact}</p>
            </div>
        ` : ''}
    `;
}

// Function to open modal
function openModal(projectKey) {
    const content = createModalContent(projectKey);
    modalBody.innerHTML = content;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Function to close modal
function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
}

// Add click event listeners to project cards
// Add click event listeners to project cards
document.addEventListener('DOMContentLoaded', () => {
    // Modal logic for project cards disabled in favor of direct page links

    // Close modal on close button click
    if (modalClose) modalClose.addEventListener('click', closeModal);

    // Close modal on overlay click
    if (modalOverlay) modalOverlay.addEventListener('click', closeModal);

    // Close modal on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
            closeModal();
        }
    });
});

// ===========================
// Project Filtering (Tabs)
// ===========================
document.addEventListener('DOMContentLoaded', () => {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const projectLinks = document.querySelectorAll('.project-card-link');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            tabBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectLinks.forEach(link => {
                if (filterValue === 'all') {
                    link.style.display = 'block';
                } else {
                    if (link.getAttribute('data-category') === filterValue) {
                        link.style.display = 'block';
                    } else {
                        link.style.display = 'none';
                    }
                }
            });
        });
    });
    const popup = document.getElementById('email-popup');
    const toggleBtn = document.getElementById('popupToggle');
    const minimizeBtn = document.getElementById('popupMinimize');
    const heroBtn = document.getElementById('hero-portfolio-btn');
    const form = document.getElementById('emailPopupForm');
    const feedback = document.getElementById('popupFeedback');
    const emailInput = document.getElementById('popupEmailInput');

    // Toggle Minimize/Expand
    function togglePopup() {
        if (popup.classList.contains('minimized')) {
            popup.classList.remove('minimized');
        } else {
            popup.classList.add('minimized');
        }
    }

    // Initialized as expanded on load (Per user request)


    // Close popup completely
    function closePopup() {
        popup.classList.add('minimized'); // Show the floating icon
    }

    if (toggleBtn && minimizeBtn) {
        toggleBtn.addEventListener('click', togglePopup);
        minimizeBtn.addEventListener('click', closePopup);
    }

    // Hero Button Trigger
    if (heroBtn) {
        heroBtn.addEventListener('click', (e) => {
            e.preventDefault();
            popup.classList.remove('minimized');
            if (emailInput) setTimeout(() => emailInput.focus(), 100);
            adjustPopupPosition(); // Re-check position on open
        });
    }

    // ===========================
    // Popup Positioning Logic (Stop at Footer)
    // ===========================
    function adjustPopupPosition() {
        if (!popup) return;

        const footer = document.querySelector('.footer');
        if (!footer) return;

        const footerTop = footer.offsetTop;
        const scrollTop = window.scrollY; // Use window.scrollY for consistency
        const windowHeight = window.innerHeight;
        const scrollBottom = scrollTop + windowHeight; // Bottom of viewport

        // Check if viewport bottom has reached the footer
        // The default bottom: 2rem is approx 32px
        const margin_bottom = 32;

        if (scrollBottom >= footerTop + margin_bottom) {
            // We have reached the footer.
            // Switch to absolute positioning relative to body
            // We want it to sit margin_bottom above the footer.
            // Since body is relative and contains footer, we can position from bottom of body.
            // Distance from Body Bottom = (Body Height - Footer Top) + margin_bottom? 
            // Actually, we want it to stay at Footer Top - margin_bottom.
            // Top (relative to body) = footerTop - popup.offsetHeight - margin_bottom.
            // Using 'top' is safer than 'bottom' if body height varies or margin collapsing occurs.

            // However, popup.offsetHeight changes when minimized/expanded. 
            // Let's use 'bottom' derived from document height if simpler, 
            // but 'top' based on footer.offsetTop is most robust reference point.

            // Force layout update if needed (rarely needed but safe)
            const popupHeight = popup.offsetHeight;

            popup.style.position = 'absolute';
            popup.style.top = `${footerTop - popupHeight - margin_bottom}px`;
            popup.style.bottom = 'auto';
            popup.style.right = '2rem'; // Keep right alignment
        } else {
            // Use fixed positioning within viewport
            popup.style.position = 'fixed';
            popup.style.top = 'auto';
            popup.style.bottom = '2rem';
            popup.style.right = '2rem';
            popup.style.transform = 'none'; // Ensure no stray translates are fighting it
        }
    }

    // Attach listeners
    window.addEventListener('scroll', adjustPopupPosition);
    window.addEventListener('resize', adjustPopupPosition);

    // Also update when popup toggles (height changes)
    // Also update when popup toggles (height changes)
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            // Wait for transition to likely finish or update repeatedly
            // Note: togglePopup() is handled by the original listener
            setTimeout(adjustPopupPosition, 50);
            setTimeout(adjustPopupPosition, 400); // After CSS transition
        });
    }
    if (minimizeBtn) {
        minimizeBtn.addEventListener('click', () => {
            // Note: closePopup() is handled by the original listener
            setTimeout(adjustPopupPosition, 50);
            setTimeout(adjustPopupPosition, 400);
        });
    }

    // Initial check
    adjustPopupPosition();

    // Form Submission
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            const email = emailInput.value;
            if (!email) return;

            // UI Loading State
            const submitBtn = form.querySelector('button');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<span>Sending...</span>';
            submitBtn.disabled = true;
            feedback.textContent = '';
            feedback.className = 'popup-feedback';

            // Simulate API Call (1.5s delay)
            setTimeout(() => {
                // Success Simulation
                submitBtn.innerHTML = '<span>Sent!</span>';
                submitBtn.style.backgroundColor = '#10b981'; // Green
                feedback.textContent = 'Portfolio link & PDF sent to your inbox.';
                feedback.classList.add('success');

                // Reset after 3 seconds
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.style.backgroundColor = '';
                    submitBtn.disabled = false;
                    form.reset();

                    // Optional: Minimize after success
                    setTimeout(() => {
                        popup.classList.add('minimized');
                        feedback.textContent = '';
                    }, 2000);
                }, 3000);

            }, 1500);
        });
    }
});


// Initialize Tabs on Load
document.addEventListener('DOMContentLoaded', () => {
    // Project Tabs
    const activeTab = document.querySelector('.tab-btn.active');
    if (activeTab) {
        setTimeout(() => activeTab.click(), 100);
    }

    // Timeline Filters
    const activeTimelineBtn = document.querySelector('.filter-btn.active');
    if (activeTimelineBtn) {
        // Extract category from onclick or match by ID pattern
        // The id is 'btn-' + category
        const category = activeTimelineBtn.id.replace('btn-', '');
        if (category) {
            setTimeout(() => filterTimeline(category), 150);
        }
    }
});


// ===========================
// Testimonials Carousel
// ===========================
document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('testimonialsContainer');
    const prevBtn = document.getElementById('prevTestimonial');
    const nextBtn = document.getElementById('nextTestimonial');
    const cards = container ? container.querySelectorAll('.testimonial-card') : [];

    if (container && prevBtn && nextBtn && cards.length > 0) {

        // Center-Focus Logic: Open to the "Blue" card (Index 1) as requested
        // [0: Purple, 1: Blue, 2: Green ...]
        let currentIndex = cards.length > 1 ? 1 : 0;

        const updateActiveState = (index) => {
            cards.forEach((card, idx) => {
                if (idx === index) {
                    card.classList.add('active');
                } else {
                    card.classList.remove('active');
                }
            });
            currentIndex = index;
        };

        const scrollToCard = (index) => {
            // Boundary checks
            if (index < 0) index = 0;
            if (index > cards.length - 1) index = cards.length - 1;

            const card = cards[index];

            // Align 'center' to put this card in the middle
            card.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest',
                inline: 'center'
            });

            updateActiveState(index);
        };

        prevBtn.addEventListener('click', () => {
            scrollToCard(currentIndex - 1);
        });

        nextBtn.addEventListener('click', () => {
            scrollToCard(currentIndex + 1);
        });

        // Initialize: Scroll & Highlight immediately
        setTimeout(() => {
            const card = cards[currentIndex];
            // Use scrollLeft calculation to avoid scrolling the main window
            if (container && card) {
                const cardRect = card.getBoundingClientRect();
                const containerRect = container.getBoundingClientRect();
                const currentRelLeft = cardRect.left - containerRect.left;
                const targetRelLeft = (container.clientWidth - card.clientWidth) / 2;

                container.scrollLeft = container.scrollLeft + (currentRelLeft - targetRelLeft);
            }
            updateActiveState(currentIndex);
        }, 100);

        // Click to focus
        cards.forEach((card, index) => {
            card.addEventListener('click', () => {
                scrollToCard(index);
            });
        });

        // Scroll Listener updates Active State
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
                    if (diff < minDiff) {
                        minDiff = diff;
                        closestIndex = idx;
                    }
                });

                if (closestIndex !== currentIndex) {
                    updateActiveState(closestIndex);
                }
            }, 50);
        }, { passive: true });
    }
});


// ===========================
// Expertise Section Navigation
// ===========================
document.addEventListener('DOMContentLoaded', () => {
    const prevBtn = document.getElementById('prevExpertise');
    const nextBtn = document.getElementById('nextExpertise');
    const panels = document.querySelectorAll('.expertise-panel');

    if (prevBtn && nextBtn && panels.length > 0) {
        let currentIndex = 0;
        const navLabel = document.getElementById('expertiseLabel');
        const labels = ['CORE COMPETENCIES', 'SKILLS', 'CERTIFICATIONS'];

        const updatePanels = () => {
            panels.forEach((panel, index) => {
                if (index === currentIndex) {
                    panel.classList.add('active');
                } else {
                    panel.classList.remove('active');
                }
            });

            // Update label text
            if (navLabel) {
                navLabel.textContent = labels[currentIndex];
            }
        };

        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + panels.length) % panels.length;
            updatePanels();
        });

        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % panels.length;
            updatePanels();
        });

        // Initialize
        updatePanels();
    }
});

// Timeline Filtering Function (Light Mode) - Global
function filterTimeline(category) {
    // Update Buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });

    const activeBtn = document.getElementById('btn-' + category);
    if (activeBtn) activeBtn.classList.add('active');

    // Filter Items
    const items = document.querySelectorAll('.timeline-item');

    items.forEach(item => {
        // Check if item matches category (all, career, or education)
        if (category === 'all' || item.classList.contains('category-' + category)) {
            item.classList.remove('item-hidden');
            item.classList.add('item-visible');

            // Trigger animation
            item.style.animation = 'none';
            item.offsetHeight; /* trigger reflow */
            item.style.animation = 'fadeIn 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards';
        } else {
            item.classList.remove('item-visible');
            item.classList.add('item-hidden');
        }
    });
}
