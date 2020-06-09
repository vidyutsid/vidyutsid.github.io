var card = document.getElementById('card');
var card2 = document.getElementById('card2');
card.addEventListener("mouseover", animate);
card2.addEventListener("mouseover", animate2);
function info(x){
	document.getElementById('info').innerHTML = x;
}
function animate() {
	info("<h2>Keshuook</h2>Keshuook is one of our developers. Keshuook's website can be found<a href='https://keshuook.github.io'>here</a>");
}
function animate2() {
	info("<h2>vidyutsid</h2>vidyutsid is one of our developers.vidyutsid's website can be found<a href='https://vidyutsid.github.io'>here</a>");
}
setTimeout(function(){
	console.clear();
},1000);
