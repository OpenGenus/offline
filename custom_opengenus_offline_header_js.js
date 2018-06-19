window.onscroll = function() {myFunction()};

var header = document.getElementById("custom_opengenus_offline_header_div");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
