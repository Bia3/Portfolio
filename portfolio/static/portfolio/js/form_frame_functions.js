/*
 * Function to process message data from event listener
 */
function processData(dat) {
  try {
    if (dat.name) {
      document
        .querySelector(`#${dat.name}_form_button`)
        .classList.remove("visually-hidden");
      document
        .querySelector(`#${dat.name}_form`)
        .classList.add("visually-hidden");
      window.location.reload();
    }
  } catch (err) {
    console.log(`err: ${err}`);
  }
}

// Create IE + others compatible event handler
const eventMethod = window.addEventListener
  ? "addEventListener"
  : "attachEvent";
const eventer = window[eventMethod];
const messageEvent = eventMethod === "attachEvent" ? "onmessage" : "message";

// Listen to message from child window
eventer(
  messageEvent,
  (evt) => {
    if (
      evt.origin !== "http://127.0.0.1:8000" &&
      evt.origin !== "https://rossdev.io" &&
      evt.origin !== "https://rossdev.io" &&
      evt.origin !== "https://rossdev.co"
    ) {
      return;
    }
    processData(evt.data);
  },
  false
);

/*
 * Function to toggle on or off the frame used for forms.
 */
// skipcq: JS-0128
function toggle_frame(name) {
  document
    .querySelector(`#${name}_form_button`)
    .classList.add("visually-hidden");
  document.querySelector(`#${name}_form`).classList.remove("visually-hidden");
}
