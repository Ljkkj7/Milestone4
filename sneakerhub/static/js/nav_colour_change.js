document.addEventListener('DOMContentLoaded', function() {
    var header = document.getElementById('id-site-header');
    var isHomePage = window.location.pathname === '/';

    if (header) {
        if (!isHomePage && header.classList.contains('background-white')) {
            header.classList.remove('background-white');
            header.classList.add('background-peach');
        } else if (isHomePage && header.classList.contains('background-peach')) {
            header.classList.remove('background-peach');
            header.classList.add('background-white');
        }
    }
});