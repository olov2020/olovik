document.addEventListener('DOMContentLoaded', () => {
  const fireImage = document.getElementById('fireImage');
  const fireCounter = document.getElementById('fireCounter');
  const textToLight = document.getElementById('textToLight');

  // Function to get the counter value from local storage
  function getCounter() {
    return parseInt(localStorage.getItem('fireCounter'), 10) || 0;
  }

  // Function to set the counter value in local storage
  function setCounter(value) {
    localStorage.setItem('fireCounter', value);
  }

  // Function to convert a number to a hexadecimal color component
  function toHex(value) {
    const hex = value.toString(16);
    return hex.length === 1 ? '0' + hex : hex;
  }

  // Function to increment the counter
  function incrementCounter() {
    const currentCounter = getCounter();
    const newCounter = currentCounter + 1;
    setCounter(newCounter);

    const red = toHex((newCounter * 10) % 256);
    const green = toHex((0) % 256);
    const blue = toHex((0) % 256);

    textToLight.style.color = `#${red}${green}${blue}`;
    const scale = 1 + newCounter * 0.01;
    textToLight.style.transform = `scale(${scale})`;
    fireCounter.textContent = newCounter;
  }

  // Initialize the counter value
  function initializeCounter() {
    fireCounter.textContent = getCounter();
  }

  // Add event listener to the image
  fireImage.addEventListener('click', incrementCounter);

  // Initialize the counter when the page loads
  initializeCounter();
});