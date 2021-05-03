(function () {
    /** 
    * Prevents event's default action if is not confirmed by user.
    * @param {obj} e - Event
    */
    const confirmIt = e => {
        if (!confirm('Are you sure?')) {
            e.preventDefault();
            e.stopPropagation();
        }
    };

    // Confirm action event listener for items with class .confirm
    document.querySelectorAll('.confirm').forEach(item => {
        item.addEventListener('click', confirmIt, false);
    });

    // CREDIT: https://css-tricks.com/value-bubbles-for-range-inputs/
    const allRanges = document.querySelectorAll(".range-wrap");
    allRanges.forEach(wrap => {
        const range = wrap.querySelector(".range");
        const bubble = wrap.querySelector(".bubble");

        range.addEventListener("input", () => {
            setBubble(range, bubble);
        });
        setBubble(range, bubble);
    });

    function setBubble(range, bubble) {
        const val = range.value;
        const min = range.min ? range.min : 0;
        const max = range.max ? range.max : 100;
        const newVal = Number(((val - min) * 100) / (max - min));
        bubble.innerHTML = val;

        // Sorta magic numbers based on size of the native UI thumb
        bubble.style.left = `calc(${newVal}% + (${8 - newVal * 0.15}px))`;
    }

    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    const tooltipList = tooltipTriggerList.map(tooltipTriggerEl => {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    })
})()