document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.site-header nav a');

    navLinks.forEach((link) => {
        if (link.pathname === window.location.pathname) {
            link.classList.add('active');
        }
    });
});
