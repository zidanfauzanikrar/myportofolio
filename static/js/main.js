document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.site-header nav a');

    navLinks.forEach((link) => {
        if (link.pathname === window.location.pathname) {
            link.classList.add('active');
        }
    });

    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        const updateToggleUI = (theme) => {
            themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
            themeToggle.setAttribute(
                'aria-label',
                theme === 'dark' ? 'Ganti ke mode terang' : 'Ganti ke mode gelap'
            );
        };

        updateToggleUI(document.documentElement.getAttribute('data-theme'));

        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
            updateToggleUI(next);
        });
    }
});