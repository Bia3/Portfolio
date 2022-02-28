/*
 * Function used on readmore buttons for homepage
 */
// skipcq: JS-0128
function readMore(btn_text) {
  const dots = document.getElementById(btn_text.id + "dots");
  const moreText = document.getElementById(btn_text.id + "read");
  const btnText = btn_text;

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
