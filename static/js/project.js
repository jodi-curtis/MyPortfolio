/*Javascript to load in projects one at a time*/
const projectContainers = document.querySelectorAll('.project-item-container');
projectContainers.forEach((container, index) => {
    container.style.animationDelay = `${index * 0.5}s`;
});
