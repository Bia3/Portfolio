function readMore(e) {
  var dots = document.getElementById(e.id +"dots");
  var moreText = document.getElementById(e.id + "read");
  var btnText = e

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "block";
  }
}