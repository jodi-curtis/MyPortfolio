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


let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.project-image');
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }
    const offset = -currentSlide * 100;
    document.querySelector('.project-images').style.transform = `translateX(${offset}%)`;
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.prev').addEventListener('click', function() {
        showSlide(currentSlide - 1);
    });

    document.querySelector('.next').addEventListener('click', function() {
        showSlide(currentSlide + 1);
    });

    showSlide(currentSlide);
});