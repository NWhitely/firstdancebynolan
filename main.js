/* ==========================================================================
   Dance by Nolan — shared interactions
   Loaded on every page (home, weddings, lessons).
   Safe to load on pages that don't have every element (guards included).
   ========================================================================== */

// Mobile menu toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.getElementById('navLinks');

if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
        mobileMenuBtn.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close mobile menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenuBtn.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
}

// Navbar scroll effect & scroll progress bar
const navbar = document.getElementById('navbar');
const scrollProgress = document.getElementById('scrollProgress');

window.addEventListener('scroll', () => {
    // Navbar shadow
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }

    // Scroll progress bar
    if (scrollProgress) {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        scrollProgress.style.width = scrollPercent + '%';
    }
});

// Fade-in animations on scroll
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
};

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in, .fade-in-stagger').forEach(el => {
    fadeObserver.observe(el);
});

// FAQ Accordion
document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const item = button.parentElement;
        const isActive = item.classList.contains('active');

        // Close all other items
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));

        // Toggle current item
        if (!isActive) {
            item.classList.add('active');
        }
    });
});

// Web3Forms contact forms — AJAX submit with inline success/error message
// (keeps the visitor on the page instead of redirecting to Web3Forms)
document.querySelectorAll('form.web3-form').forEach(form => {
    const result = form.querySelector('.form-result');
    const submitBtn = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const originalBtnText = submitBtn ? submitBtn.textContent : '';

        if (result) {
            result.hidden = false;
            result.className = 'form-result sending';
            result.textContent = 'Sending...';
        }
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';
        }

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: { 'Accept': 'application/json' },
                body: new FormData(form)
            });
            const data = await response.json();

            if (response.ok && data.success) {
                if (result) {
                    result.className = 'form-result success';
                    result.textContent = "Thank you! Your message is on its way. I'll be in touch soon.";
                }
                form.reset();
            } else {
                throw new Error(data.message || 'Submission failed');
            }
        } catch (err) {
            if (result) {
                result.className = 'form-result error';
                result.innerHTML = 'Something went wrong. Please try again, or email me directly at <a href="mailto:whitely.nolan@gmail.com">whitely.nolan@gmail.com</a>.';
            }
        } finally {
            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.textContent = originalBtnText;
            }
        }
    });
});

// Smooth scroll for same-page anchor links (cross-page links like
// "index.html#about" are left to the browser's default navigation)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#' || href.length < 2) return;
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
