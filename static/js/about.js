const flightPath = {
    curviness: 1.25,
    autoRotate: true,
    values: [
        {x: window.innerWidth*0.25, y: -100},
        {x: window.innerWidth*0.5, y: 100},
        {x: window.innerWidth*0.75, y: -100},
        {x: window.innerWidth, y: 100}
    ]
}

const tween = new TimelineLite();

tween.add(
    TweenLite.to('.scratch-img',1, {
        bezier: flightPath,
        ease: Power1.easeInOut
    })
);

const controller = new ScrollMagic.Controller();

const scene = new ScrollMagic.Scene({
    triggerElement: '.about-container-2',
    duration: 1000,
    triggerHook: 0
}).setTween(tween).setPin(".about-container-2").addTo(controller);


function adjustContainerHeight() {
    const header = document.querySelector('header');
    const container = document.querySelector('.about-container');
    const headerHeight = header.offsetHeight;
    const viewportHeight = window.innerHeight;
    const containerHeight = viewportHeight - headerHeight;
    container.style.height = `${containerHeight}px`;
}

window.addEventListener('load', adjustContainerHeight);
window.addEventListener('resize', adjustContainerHeight);