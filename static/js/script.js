(function () {
    'use strict'

    document.querySelectorAll('[data-toggle="offcavas"]').forEach(item => {
        item.addEventListener('click', () => {
            document.querySelector('.offcanvas-collapse').classList.toggle('open');
            document.querySelector('#navbar-toggler .bi').classList.toggle('bi-x');
        })
    });
})()