function adjustContainerHeight() {
    const header = document.querySelector('header');
    const container = document.querySelector('.container');
    const headerHeight = header.offsetHeight;
    const viewportHeight = window.innerHeight;
    const containerHeight = viewportHeight - headerHeight;
    container.style.height = `${containerHeight}px`;
}

window.addEventListener('load', adjustContainerHeight);
window.addEventListener('resize', adjustContainerHeight);