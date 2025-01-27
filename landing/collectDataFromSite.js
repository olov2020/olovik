document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contactForm');
  const webAppUrl = 'https://script.google.com/macros/s/AKfycbzGLgPaTn2URr4OGiwTeYi81_TzYBz2QP0_v7jnXWBGi6G4XX3s6HgGmooZV5fRCSA/exec'; // Replace with your web app URL

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {
      email: formData.get('email'),
      message: formData.get('message')
    };

    if (!data.email || !data.message) {
      alert('Please fill in all fields.');
      return;
    }

    try {
      const response = await fetch(webAppUrl, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json'
        }
      });

      const result = await response.json();
      if (result.result === 'success') {
        alert('Form submitted successfully!');
        form.reset();
      } else {
        alert('Form submission failed.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('Form submission failed.');
    }
  });
});
