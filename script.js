window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
function start(id)
{
  if (id == "b1")
  {
    document.getElementById("write").innerHTML = "you like this then you'll be ready to see the next update. :)";
  }
  else if (id == "b2")
  {
    document.getElementById("write").innerHTML = "Thanks for your feedback and we promise that the next update will be your expectation.";
  }
  else
  {
    document.getElementById("write").innerHTML = "Server responce...";
  }
}
function done()
{
  timer = setTimeout(show, 4000);
}
function show()
{
  document.getElementById("loader").style.display = "none";
  document.getElementById("content").style.display = "block";
}
