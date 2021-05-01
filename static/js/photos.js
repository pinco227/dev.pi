(function () {
    /**
    * API GET function. Gets the data from the url and sends it as a parameter to the callback function.
    * @param {string} url - Api url to be called
    * @param {function} callback - Callback function
    */
    const ajax_call = (url, method, callback) => {
        fetch(url, {
            method: method,
            credentials: "include"
        }).then(function (response) {
            if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                callback(response.statusText);
            }
            else {
                callback(response.status);
            }
        }).catch(function (error) {
            console.log("Fetch error: " + error);
            callback(error);
        });
    };

    document.querySelectorAll('.delete-photo').forEach((el) => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            console.log('delete photo pressed');
            ajax_call(el.href, 'DELETE', (stat) => {
                if (stat === 200) {
                    el.parentElement.remove();
                }
            });
        });
    });
})()