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

// typing effects whenever content appears on the screen
document.addEventListener('DOMContentLoaded', () => {
  const typewriterElements = document.querySelectorAll('.typewriter');

  const options = {
    root: null, // Use the viewport as the root
    rootMargin: '0px',
    threshold: 0.5 // Trigger when 50% of the element is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('typewriter');
      } else {
        entry.target.classList.remove('typewriter');
      }
    });
  }, options);

  typewriterElements.forEach(element => {
    observer.observe(element);
  });
});

// showing effects
document.addEventListener('DOMContentLoaded', () => {
  const sectionElements = document.querySelectorAll('section');

  const options = {
    root: null, // Use the viewport as the root
    rootMargin: '0px',
    threshold: 0.5 // Trigger when 50% of the element is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('showEffect');
      } else {
        entry.target.classList.remove('showEffect');
      }
    });
  }, options);

  sectionElements.forEach(element => {
    observer.observe(element);
  });
});

