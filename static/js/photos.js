(() => {
    /**
    * API GET function. Gets the data from the url and sends it as a parameter to the callback function.
    * @param {string} url - Api url to be called
    * @param {function} callback - Callback function
    */
    const ajax_call = async (url, method, callback) => {
        await fetch(url, {
            method: method,
            credentials: "include"
        }).then((response) => {
            if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                callback("", response.statusText);
            }
            else {
                response.json().then((data) => {
                    // console.log(data);
                    callback(data, response.status);
                });
            }
        }).catch((error) => {
            console.log("Fetch error: " + error);
            callback("", error);
        });
    };

    document.querySelectorAll('.delete-photo').forEach((el) => {
        el.addEventListener('click', (e) => {
            e.preventDefault();

            const url = el.href + "?collection=" + el.dataset.collection + "&docid=" + el.dataset.docId + "&photokey=" + el.dataset.photoKey;
            ajax_call(url, 'DELETE', (data, stat) => {
                if (stat === 200) {
                    el.parentElement.remove();
                    console.log(data)
                }
            });
        });
    });
})()