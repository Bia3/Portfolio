/*
 * Functions to handle collapsing the Large Header on scroll
 * Disable scroll adapted from @gblazex's answer on stackoverflow
 * https://stackoverflow.com/a/4770179
 */


//
// left: 37, up: 38, right: 39, down: 40,
// spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
const keys = {37: 1, 38: 1, 39: 1, 40: 1};

function preventDefault(e) {
  e.preventDefault();
}

function preventDefaultForScrollKeys(e) {
  if (keys[e.keyCode]) {
    preventDefault(e);
    return false;
  }
}

// modern Chrome requires { passive: false } when adding event
let supportsPassive = false;
try {
  window.addEventListener("test", null, Object.defineProperty({}, 'passive', {
    get: function () { supportsPassive = true; }
  }));
} catch(e) {}

const wheelOpt = supportsPassive ? { passive: false } : false;
const wheelEvent = 'onwheel' in document.createElement('div') ? 'wheel' : 'mousewheel';

// call this to Disable
function disableScroll() {
  window.addEventListener('DOMMouseScroll', preventDefault, false); // older FF
  window.addEventListener(wheelEvent, preventDefault, wheelOpt); // modern desktop
  window.addEventListener('touchmove', preventDefault, wheelOpt); // mobile
  window.addEventListener('keydown', preventDefaultForScrollKeys, false);
}

// call this to Enable
function enableScroll() {
  window.removeEventListener('DOMMouseScroll', preventDefault, false);
  window.removeEventListener(wheelEvent, preventDefault, wheelOpt);
  window.removeEventListener('touchmove', preventDefault, wheelOpt);
  window.removeEventListener('keydown', preventDefaultForScrollKeys, false);
}

// on scroll
document.addEventListener('scroll', () => {
    setTimeout(() => {
        setTimeout(() => {
            document.querySelector('#StandardHeader').classList.add('visible');
            setTimeout(() => {
                document.querySelector('#StandardHeader').classList.add('show');
            }, 5);
        }, 5);
        document.querySelector('#LargeHeader').classList.remove('hide');
        document.querySelector('#LargeHeader .header_container').classList.remove('hide');
        document.querySelector('#LargeHeader').classList.add('visually-hidden');
        enableScroll();
    }, 2000);
    disableScroll();
    document.querySelector('#LargeHeader').classList.add('hide');
    document.querySelector('#LargeHeader .header_container').classList.add('hide');
})