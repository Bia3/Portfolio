function readMore(e) {
  const dots = document.getElementById(e.id + "dots");
  const moreText = document.getElementById(e.id + "read");
  const btnText = e;

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
