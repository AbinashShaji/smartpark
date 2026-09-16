/**
 * SmartPark — Premium Animation Controller
 * Vanilla JS — no external dependencies
 */
document.addEventListener('DOMContentLoaded', () => {

    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // =============================================
    // 1. HERO WORD-BY-WORD REVEAL
    // =============================================
    document.querySelectorAll('.hero-reveal').forEach(el => {
        if (prefersReduced) {
            el.style.opacity = '1';
            return;
        }

        // Get all direct text and child spans
        const childSpans = el.querySelectorAll('span');

        if (childSpans.length > 0) {
            // The heading already contains <span> children (e.g., two lines).
            // Process each span's text into words.
            childSpans.forEach(span => {
                const text = span.textContent.trim();
                if (!text) return;
                const words = text.split(/\s+/);
                span.textContent = '';
                words.forEach(word => {
                    const w = document.createElement('span');
                    w.className = 'hw';
                    w.textContent = word;
                    span.appendChild(w);
                });
            });
        } else {
            // Plain text heading — split into word spans
            const text = el.textContent.trim();
            const words = text.split(/\s+/);
            el.textContent = '';
            words.forEach(word => {
                const w = document.createElement('span');
                w.className = 'hw';
                w.textContent = word;
                el.appendChild(w);
            });
        }

        // Stagger reveal
        const allWords = el.querySelectorAll('.hw');
        allWords.forEach((w, i) => {
            setTimeout(() => w.classList.add('visible'), 80 + i * 50);
        });
    });

    // =============================================
    // 2. HERO SUPPORTING FADE
    // =============================================
    document.querySelectorAll('.hero-fade').forEach(el => {
        if (prefersReduced) {
            el.classList.add('visible');
            return;
        }
        const delay = parseFloat(getComputedStyle(el).getPropertyValue('--delay')) || 0;
        setTimeout(() => el.classList.add('visible'), delay * 1000);
    });

    // =============================================
    // 3. SCROLL REVEAL (IntersectionObserver)
    // =============================================
    const revealEls = document.querySelectorAll('.reveal');

    if (prefersReduced) {
        revealEls.forEach(el => el.classList.add('revealed'));
    } else {
        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;

                    // If this is a stagger container, set child delays
                    if (el.classList.contains('reveal-stagger')) {
                        const children = el.children;
                        for (let i = 0; i < children.length; i++) {
                            children[i].style.opacity = '0';
                            children[i].style.transform = 'translateY(16px)';
                            children[i].style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
                            children[i].style.transitionDelay = `${i * 0.08}s`;
                        }
                        // Trigger after a frame so the initial state is painted
                        requestAnimationFrame(() => {
                            for (let i = 0; i < children.length; i++) {
                                children[i].style.opacity = '1';
                                children[i].style.transform = 'translateY(0)';
                            }
                        });
                    }

                    el.classList.add('revealed');
                    obs.unobserve(el);
                }
            });
        }, { threshold: 0.12 });

        revealEls.forEach(el => observer.observe(el));
    }

    // =============================================
    // 4. FAQ SMOOTH ACCORDION
    // =============================================
    document.querySelectorAll('.faq-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const content = btn.nextElementSibling;
            if (!content || !content.classList.contains('faq-content')) return;

            const isOpen = btn.getAttribute('aria-expanded') === 'true';

            // Close all others first
            document.querySelectorAll('.faq-btn').forEach(other => {
                if (other !== btn) {
                    other.setAttribute('aria-expanded', 'false');
                    const otherContent = other.nextElementSibling;
                    if (otherContent && otherContent.classList.contains('faq-content')) {
                        otherContent.classList.remove('open');
                        otherContent.style.setProperty('--faq-h', '0px');
                    }
                }
            });

            // Toggle current
            if (isOpen) {
                btn.setAttribute('aria-expanded', 'false');
                content.classList.remove('open');
                content.style.setProperty('--faq-h', '0px');
            } else {
                btn.setAttribute('aria-expanded', 'true');
                content.style.setProperty('--faq-h', content.scrollHeight + 'px');
                content.classList.add('open');
            }
        });
    });
});
