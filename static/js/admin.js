(function () {
    const confirmIt = e => {
        if (!confirm('Are you sure?')) e.preventDefault();
    };

    document.querySelectorAll('.confirm').forEach(item => {
        item.addEventListener('click', confirmIt, false);
    });
})()