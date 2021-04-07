(function () {
    'use strict'

    document.querySelector('#navbar-toggler').addEventListener('click', function () {
        document.querySelector('.offcanvas-collapse').classList.toggle('open');
        document.querySelector('#navbar-toggler .bi').classList.toggle('bi-x');
    })
})()