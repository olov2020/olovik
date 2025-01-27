document.addEventListener('DOMContentLoaded', () => {
  const olovikHeader = document.getElementById('olovikHeader');
  const portfolioHeader = document.getElementById('portfolioHeader');
  const contactsHeader = document.getElementById('contactsHeader');
  const olovikArticle = document.getElementById('olovik');
  const portfolioArticle = document.getElementById('portfolio');
  const contactsArticle = document.getElementById('contacts');

  const options = {
    root: null, // Use the viewport as the root
    rootMargin: '0px',
    threshold: 0.5 // Trigger when 50% of the article is visible
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target.id === 'portfolio') {
          portfolioHeader.classList.add('active');
          contactsHeader.classList.remove('active');
          olovikHeader.classList.remove('active');
        } else if (entry.target.id === 'contacts') {
          contactsHeader.classList.add('active');
          portfolioHeader.classList.remove('active');
          olovikHeader.classList.remove('active');
        } else if (entry.target.id === 'olovik') {
          olovikHeader.classList.add('active');
          portfolioHeader.classList.remove('active');
          contactsHeader.classList.remove('active');
        }
      } else {
        if (entry.target.id === 'portfolio') {
          portfolioHeader.classList.remove('active');
        } else if (entry.target.id === 'contacts') {
          contactsHeader.classList.remove('active');
        } else if (entry.target.id === 'olovik') {
          olovikHeader.classList.remove('active');
        }
      }
    });
  }, options);

  observer.observe(portfolioArticle);
  observer.observe(contactsArticle);
  observer.observe(olovikArticle);
});
