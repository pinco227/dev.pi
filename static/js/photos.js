(() => {
    /**
    * API GET function. Gets the data from the url and sends it as a parameter to the callback function.
    * @param {string} url - Api url to be called
    * @param {function} callback - Callback function
    */
    const ajax_call = async (url, method, body, callback) => {
        await fetch(url, {
            method: method,
            credentials: "include",
            body: body
        }).then((response) => {
            if (response.status < 200 && response.status > 299) {
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

    const dropArea = document.getElementById('drop-area');
    const urlForPhotos = document.getElementById('url-for-photos').value;
    const collection = document.getElementById('collection').value;
    const docId = document.getElementById('doc-id').value;

    /** 
    * Prevents default action for the event in which was called.
    * @param {obj} e - event object.
    */
    const preventDefaults = (e) => {
        e.preventDefault();
        e.stopPropagation();
    }

    /**
    * Adds .highlight class to the drop area element.
    */
    const highlight = () => {
        dropArea.classList.add('highlight');
    }

    /**
    * Removes .highlight class from the drop area element.
    */
    const unhighlight = () => {
        dropArea.classList.remove('highlight');
    }

    /**
     * Handles the dropped files.
    * @credit https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/
    * @param {obj} e - event object.
    */
    const handleDrop = (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;

        handleFiles(files);
    }

    const handleFiles = (files) => {
        if (dropArea.dataset.multiple == "true") {
            ([...files]).forEach(uploadFile);
        } else {
            if (uploadFile(files[0])) {
                if (document.querySelectorAll('[data-photo-key]')[0]) {
                    const delete_url = urlForPhotos + "?collection=" + collection + "&docid=" + docId + "&photokey=0";
                    ajax_call(delete_url, 'DELETE', '', (data, stat) => {
                        if (stat === 200) {
                            document.querySelectorAll('[data-photo-key]')[0].parentElement.remove();
                            console.log(data);
                        }
                    });
                }
            }
        }
    }

    function uploadFile(file) {
        const url = urlForPhotos + "?collection=" + collection + "&docid=" + docId;
        const formData = new FormData();

        formData.append('photos', file);

        if (ajax_call(url, 'PATCH', formData, (data, stat) => {
            if (stat === 201) {
                console.log(data);
                const containerEl = document.getElementById('gallery');
                const newEl = document.createElement("div");
                newEl.classList.add("photo-container", "col-sm-4", "col-md-6", "col-lg-4");
                const existingElCount = document.querySelectorAll(".photo-container").length;
                newEl.innerHTML = `<img class="img-thumbnail" src="/uploads/${data.newName}" alt="${data.newName}">
                                    <button href="#" class="delete-photo btn btn-danger" data-photo-key="${existingElCount}">
                                        <i class="bi bi-trash-fill"></i>
                                    </button>`
                containerEl.appendChild(newEl);
                return true;
            } else {
                console.log(stat);
                return false
            }
        })) {
            return true
        } else {
            return false
        }
    }

    document.getElementById("gallery").addEventListener('click', (e) => {
        if (e.target && e.target.classList.contains('delete-photo')) {
            e.preventDefault();

            const url = urlForPhotos + "?collection=" + collection + "&docid=" + docId + "&photokey=" + e.target.dataset.photoKey;
            console.log(url);
            ajax_call(url, 'DELETE', '', (data, stat) => {
                if (stat === 200) {
                    e.target.parentElement.remove();
                    console.log(data);
                }
            });
        }
    });

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    })

    dropArea.addEventListener('drop', handleDrop, false);

})()