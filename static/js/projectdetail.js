/* Javascript to ensure data us input in comment form */
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





/* If new comment has been added, on page load scroll down to comment section */
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.has('new_comment')) {
    const commentsSection = document.getElementById('comments');
    if (commentsSection) {
        commentsSection.scrollIntoView({ behavior: 'smooth' });
    }
}





let currentSlide = 0;

function showSlide(index) {
    //Get Slides
    const slides = document.querySelectorAll('.project-image');
    // If index is greater than number of slides 
    if (index >= slides.length) {
        // Show first slide 
        currentSlide = 0;
    // If index is less than 0 
    } else if (index < 0) {
        // Show last slide 
        currentSlide = slides.length - 1;
    } else {
        // Show slide of passed index
        currentSlide = index;
    }
    // Calculate translation needed to show slide
    const offset = -currentSlide * 100;
    document.querySelector('.project-images').style.transform = `translateX(${offset}%)`;
}

// On Click of previous button, call show slide function and pass value of current slide - 1 
document.querySelector('.prev').addEventListener('click', function() {
    showSlide(currentSlide - 1);
});

// On Click of next button, call show slide function and pass value of current slide + 1 
document.querySelector('.next').addEventListener('click', function() {
    showSlide(currentSlide + 1);
});

showSlide(currentSlide);