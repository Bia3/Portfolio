// const bttn = document.querySelector('.submit')

function getTargetOrigin() {
  try {
    const url =
      window.location !== window.parent.location
        ? document.referrer
        : document.location.href;

    if (url.indexOf("rossdev.io") !== -1) {
      return document.location.protocol + "//rossdev.io";
    }
    if (url.indexOf("rossdev.co") !== -1) {
      return document.location.protocol + "//rossdev.co";
    }
    return url.indexOf("rossdev.tech") !== -1 ? document.location.protocol + "//rossdev.tech" : document.location.protocol + "//" + url.split("/")[2];
  } catch (
    e // falback to production
  ) {
    return document.location.protocol + "//rossdev.io";
  }
}

if (form_complete) {
  parent.postMessage({ name: "project" }, getTargetOrigin());
}
