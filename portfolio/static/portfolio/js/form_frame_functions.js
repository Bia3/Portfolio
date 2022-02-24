// Process message data from event listener
function processData(dat) {
    try {
        if (dat.name){
            document.querySelector(`#${dat.name}_form_button`).classList.remove('visually-hidden');
            document.querySelector(`#${dat.name}_form`).classList.add('visually-hidden');
            window.location.reload();
            // switch (dat.name) {
            //     case 'skill':
            //         document.querySelector(`#${dat.name}_form_button`).classList.remove('visually-hidden');
            //         document.querySelector(`#${dat.name}_form`).classList.add('visually-hidden');
            //         window.location.reload();
            //         break;
            //     default:
            //         break;
            // }
        }
    } catch (err) {
        console.log(`err: ${err}`)
    }
}

// Create IE + others compatible event handler
let eventMethod = window.addEventListener ? 'addEventListener' : 'attachEvent';
let eventer = window[eventMethod];
let messageEvent = eventMethod === 'attachEvent' ? 'onmessage' : 'message';

// Listen to message from child window
eventer(
  messageEvent,
  function (evt) {
      if (evt.origin !== "http://127.0.0.1:8000" &&
          evt.origin !== "https://rossdev.io" &&
          evt.origin !== "https://rossdev.io" &&
          evt.origin !== "https://rossdev.co" )
          return;
      processData(evt.data);
  },
  false
);

function toggle_frame(name){
    document.querySelector(`#${name}_form_button`).classList.add('visually-hidden');
    document.querySelector(`#${name}_form`).classList.remove('visually-hidden');
}