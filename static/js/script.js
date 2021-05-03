// Offcanvas toggle click event listener
document.querySelectorAll('[data-toggle="offcavas"]').forEach(item => {
    item.addEventListener('click', () => {
        document.querySelector('.offcanvas-collapse').classList.toggle('open');
        document.querySelector('#navbar-toggler .bi').classList.toggle('bi-x');
    })
});

const toastContainer = document.querySelectorAll('.toast-container')[0];
const toastSettings = {
    autohide: true,
    delay: 4000
};

/**
* Creates a new toast element and displays it
* @param {string} message - message to be displayed.
*/
const alertToast = message => {
    const newToastEl = Object.assign(document.createElement('div'), {
        className: 'd-flex w-100 toast',
        role: 'alert',
        'aria-live': 'assertive',
        'aria-atomic': 'true',
        innerHTML: `<span class="m-auto px-2">
                                    <i class="bi bi-bell-fill"></i>
                                </span>
                                <div class="toast-body">
                                    <h4>${message}</h4>
                                </div>
                                <a href="" class="me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"><i
                                        class="bi bi-x-circle"></i></a>`
    });
    toastContainer.insertBefore(newToastEl, toastContainer.firstChild);
    const newToast = new bootstrap.Toast(newToastEl, toastSettings);
    newToast.show();
};

// Create Botstrap toasts from existing DOM elements
const toastElList = [].slice.call(document.querySelectorAll('.toast'));
const toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl, toastSettings);
});
// Show toasts
toastList.forEach(toast => {
    toast.show();
});