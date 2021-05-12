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
const formElement = document.getElementById('dropzoneForm');
let formSubmitted = false;
const dropArea = document.getElementById('drop-area');
const fileElem = document.getElementById('drop-file-elem');
const urlForFiles = document.getElementById('url-for-files').value;
const collection = document.getElementById('collection').value;
const docId = document.getElementById('doc-id') ? document.getElementById('doc-id').value : 0;

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
* Updates the hidden input with uploaded filenames list.
*/
const fileListUpdate = () => {
    const fileListInput = document.getElementById('photo-list');
    const fileList = [];
    document.querySelectorAll('.photo-container').forEach(el => {
        fileList.push(el.dataset.src);
    });
    if (fileListInput) fileListInput.value = fileList.join(',');
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
        // check if there is a current file
        if (document.querySelectorAll('[data-photo-key]')[0]) {
            if (confirm('Are you sure?\r\n This will replace the current file!')) {
                if (uploadFile(files[0])) {
                    const delete_url = docId ? urlForFiles + "?collection=" + collection + "&docid=" + docId + "&photokey=0" :
                        urlForFiles + "?collection=" + collection + "&src=" + document.querySelectorAll('[data-photo-key]')[0].parentElement.dataset.src;
                    ajax_call(delete_url, 'DELETE', '', (data, stat) => {
                        if (stat === 200) {
                            document.querySelectorAll('[data-photo-key]')[0].parentElement.remove();
                            alertToast(data.message);
                        }
                    });
                }
            } else {
                return;
            }
        } else {
            uploadFile(files[0]);
        }
    }
}

/**
* Uploads a file element by sending at through an PATCH ajax call to a python route
* @param {obj} file - file object.
*/
const uploadFile = (file) => {
    const url = docId ? urlForFiles + "?collection=" + collection + "&docid=" + docId : urlForFiles + "?collection=" + collection;
    const formData = new FormData();

    formData.append('files', file);

    return ajax_call(url, 'PATCH', formData, (data, stat) => {
        if (stat === 201) {
            if (document.getElementById('gallery')) {
                const containerEl = document.getElementById('gallery');
                const existingElCount = document.querySelectorAll(".photo-container").length;
                const initialSlug = document.getElementById('initial-slug');
                let galleryClass;
                let imgTag;
                if (initialSlug) {
                    galleryClass = initialSlug.value + "-gallery";
                }
                if (galleryClass) {
                    imgTag = `<a href="/uploads/${data.newName}" class="${galleryClass}">
                                    <img class="img-thumbnail gallery-item" src="/uploads/${data.newName}" alt="${data.newName}">
                                </a>`;
                } else {
                    imgTag = `<img class="img-thumbnail" src="/uploads/${data.newName}" alt="${data.newName}">`;
                }
                const newEl = Object.assign(document.createElement('div'), {
                    className: 'photo-container col-sm-4 col-md-6 col-lg-4',
                    innerHTML: `${imgTag}
                                <a class="delete-photo btn btn-danger" data-photo-key="${existingElCount}">
                                    <i class="bi bi-trash-fill"></i>
                                </a>`
                });
                newEl.dataset.src = data.newName;
                containerEl.appendChild(newEl);
                fileListUpdate();
            }
            alertToast(data.message);
            return true;
        } else {
            alertToast(data.message);
            return false
        }
    });
}

/**
* Delay function
* @credit https://www.perimeterx.com/tech-blog/2019/beforeunload-and-unload-events/
* @param {number} delay - miliseconds.
*/
const sleep = (delay) => {
    const start = new Date().getTime();
    while (new Date().getTime() < start + delay);
}

// Event Delegation for dynamic created elements
// Click event listener for file delete button
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('delete-photo') && e.target.dataset.photoKey) {
        e.preventDefault;
        if (confirm('Are you sure?\r\n This will delete file and remove it from the database!')) {
            const url = docId ? urlForFiles + "?collection=" + collection + "&docid=" + docId + "&photokey=" + e.target.dataset.photoKey :
                urlForFiles + "?collection=" + collection + "&src=" + e.target.parentElement.dataset.src;
            console.log(url);
            ajax_call(url, 'DELETE', '', (data, stat) => {
                if (stat === 200) {
                    e.target.parentElement.remove();
                    alertToast(data.message);
                    fileListUpdate();
                }
            });
        }
    }
});

// Event listener for form submission
if (formElement) {
    formElement.addEventListener('submit', () => {
        formSubmitted = true;
        console.log("submitted");
    });
}

// Check if db doc id is set (if is set then page is on an edit form)
if (!docId) {
    // Prevent leaving page if any existing uploads (except for submit)
    window.onbeforeunload = () => {
        showSpinner();
        setTimeout(() => { hideSpinner() }, 1000); // Only hides the spinner if user cancels unload
        if (document.querySelectorAll('.photo-container').length && !formSubmitted) {
            return "Are you sure you want to leave?";
        } else {
            return;
        }
    };
    // Delete uploaded files on page unload
    window.onunload = () => {
        if (document.querySelectorAll('.photo-container').length && !formSubmitted) {
            document.querySelectorAll('.photo-container').forEach(el => {
                const url = urlForFiles + "?collection=" + collection + "&src=" + el.dataset.src;
                ajax_call(url, 'DELETE', '', () => { });
            });
            sleep(2000);
        }
    };
}

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
    fileElem.value = "";
};