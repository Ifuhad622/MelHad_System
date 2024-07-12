// main.js

// Function to handle form submission
function handleFormSubmission(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());

    // Example: Sending data to the server
    fetch('/api/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Handle success (e.g., show a success message or redirect)
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle error (e.g., show an error message)
    });
}

// Add event listeners to forms
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', handleFormSubmission);
});

// Example: Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Example: Toggle a mobile navigation menu
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('nav');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('open');
    });
}
