// changing contents opacity while scrolling
document.addEventListener('DOMContentLoaded', () => {
  const contents = document.querySelectorAll('article');

  const showContentOnScroll = () => {
    contents.forEach(content => {
      const contentPosition = content.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      const contentHeight = content.offsetHeight;
      const halfWindowHeight = windowHeight / 2;
      const halfContentHeight = contentHeight / 2;

      // Calculate the opacity based on the scroll position
      let opacity = 0;
      const centerPoint = halfWindowHeight - halfContentHeight;
      const distanceFromCenter = Math.abs(contentPosition + halfContentHeight - halfWindowHeight);
      const maxDistance = Math.max(halfWindowHeight, halfContentHeight);

      if (distanceFromCenter <= maxDistance) {
        opacity = 1 - (distanceFromCenter / maxDistance);
      }

      // Set the opacity
      content.style.opacity = opacity;
    });
  };

  window.addEventListener('scroll', showContentOnScroll);
  showContentOnScroll(); // Initial check
});

// changing background color while scrolling
// script.js
document.addEventListener('DOMContentLoaded', () => {
  const contactsSection = document.querySelector('.contacts');

  const changeBackgroundOnScroll = () => {
    const contactsPosition = contactsSection.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;
    const halfSectionHeight = contactsSection.offsetHeight / 2;

    if (contactsPosition < windowHeight - halfSectionHeight) {
      // More than half of the contacts section is in the viewport
      document.body.style.backgroundColor = '#454545';
    } else {
      // Less than half of the contacts section is in the viewport
      document.body.style.backgroundColor = '#cdcdcd';
    }
  };

  window.addEventListener('scroll', changeBackgroundOnScroll);
  changeBackgroundOnScroll(); // Initial check
});
