/* Javascript to set height of container as height of screen - the header */
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



/**********Animation **********/
//Set flight path of image
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

//Create animation
const tween = new TimelineLite();
tween.add(
    TweenLite.to('.scratch-img',1, {
        bezier: flightPath,
        ease: Power1.easeInOut
    })
);

//Scroll based animation
const controller = new ScrollMagic.Controller();

//Animation triggered when scratch-container enters viewport, lasts for 1000 px
const scene = new ScrollMagic.Scene({
    triggerElement: '.scratch-container',
    duration: 1000,
    triggerHook: 0
}).setTween(tween).setPin(".scratch-container").addTo(controller);