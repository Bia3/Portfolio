function onClick(e){
  Array.prototype.slice.call(document.getElementsByClassName('content')).forEach((i) => {
    i.style.opacity = '0';
    i.style.display = 'none';
  });
  let elem = Array.prototype.slice.call(document.getElementsByClassName(e.classList[0])).find((i) => {
    return Array.prototype.slice.call(i.classList).includes('content');
  });
  elem.style.display = 'block';
  elem.style.opacity = '1';
}