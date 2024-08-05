const flightPath = {
    curviness: 1.25,
    autoRotate: true,
    values: [

        {x: window.innerWidth, y: 0}
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
    triggerElement: '.animation',
    duration: 500,
    triggerHook: 0.5
}).setTween(tween).addTo(controller);