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

    // Declare used variables
    const dropArea = document.getElementById('drop-area');
    const fileElem = document.getElementById('drop-file-elem');
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
    * Function called when drop area is clicked and it triggers click on the file input.
    */
    const handleClick = () => {
        fileElem.click();
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

    /**
    * Handles a set of files by calling Upload function for each.
    * If the drag&drop area is not set to multiple, then an ajax DELETE request is sent to delete the current file.
    * @param {obj} files - files object.
    */
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

    /**
    * Uploads a file element by sending at through an PATCH ajax call to a python route
    * @param {obj} file - file object.
    */
    const uploadFile = (file) => {
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

    // Event Delegation for dynamic created elements
    // Click event listener for file delete button
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

    // Drag&Drop event listeners
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
    });
    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });
    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });
    dropArea.addEventListener('drop', handleDrop, false);

    // Click on the drag&drop area event listener
    dropArea.addEventListener('click', handleClick, false);

    // File input change event listener
    fileElem.onchange = () => {
        handleFiles(fileElem.files);
    };
})()