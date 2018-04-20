var card=$(".card")
var carousel=$(".container-fluid")
var button=$(".wrapper")

// var containerEl = document.querySelector(".ab");
// var mixer=mixitup(containerEl);





TweenMax.staggerFrom(card, 1, {y:100, opacity:0, delay:0.5}, 0.2);
TweenMax.from(carousel, 1, {y:100, opacity:0});
TweenMax.from(button, 1, {y:100, opacity:0});







