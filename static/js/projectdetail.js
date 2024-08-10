document.getElementById('name').oninvalid = function(event) {
    event.target.setCustomValidity('Please enter your Name.');
};

document.getElementById('name').oninput = function(event) {
    event.target.setCustomValidity('');
};

document.getElementById('comment').oninvalid = function(event) {
    event.target.setCustomValidity('You cannot submit a blank comment.');
};

document.getElementById('comment').oninput = function(event) {
    event.target.setCustomValidity('');
};


document.addEventListener('DOMContentLoaded', (event) => {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('new_comment')) {
        const commentsSection = document.getElementById('comments');
        if (commentsSection) {
            commentsSection.scrollIntoView({ behavior: 'smooth' });
        }
    }
});