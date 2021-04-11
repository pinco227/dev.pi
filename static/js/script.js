(function () {
    'use strict'

    document.querySelectorAll('[data-toggle="offcavas"]').forEach(item => {
        item.addEventListener('click', () => {
            document.querySelector('.offcanvas-collapse').classList.toggle('open');
            document.querySelector('#navbar-toggler .bi').classList.toggle('bi-x');
        })
    });

    const toastElList = [].slice.call(document.querySelectorAll('.toast'));
    const toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl, {
            autohide: true,
            delay: 4000
        });
    });
    toastList.forEach(toast => {
        toast.show();
    });

})()