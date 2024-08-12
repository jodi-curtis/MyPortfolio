/* Javascript to ensure data is input in contact form */
document.getElementById('fname').oninvalid = function(event) {
    event.target.setCustomValidity('Please enter your First Name.');
};

document.getElementById('fname').oninput = function(event) {
    event.target.setCustomValidity('');
};

document.getElementById('sname').oninvalid = function(event) {
    event.target.setCustomValidity('Please enter your Surname.');
};

document.getElementById('sname').oninput = function(event) {
    event.target.setCustomValidity('');
};

document.getElementById('email').oninvalid = function(event) {
    event.target.setCustomValidity('Please enter your Email Address.');
};

document.getElementById('email').oninput = function(event) {
    event.target.setCustomValidity('');
};

document.getElementById('subject').oninvalid = function(event) {
    event.target.setCustomValidity('Please enter a Subject for your Message.');
};

document.getElementById('subject').oninput = function(event) {
    event.target.setCustomValidity('');
};

document.getElementById('message').oninvalid = function(event) {
    event.target.setCustomValidity('Please enter a Message. You cannot submit a blank Message.');
};

document.getElementById('message').oninput = function(event) {
    event.target.setCustomValidity('');
};