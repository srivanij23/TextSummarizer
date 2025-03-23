// Add at the beginning of the file
document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    
    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggle.checked = savedTheme === 'dark';
    }

    // Theme toggle handler
    themeToggle.addEventListener('change', (e) => {
        const theme = e.target.checked ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    });
});

async function summarize() {
    const text = document.getElementById('text').value;
    const sentences = parseInt(document.getElementById('sentences').value);
    const summaryDiv = document.getElementById('summary');

    if (!text.trim()) {
        summaryDiv.innerHTML = 'Please enter some text to summarize.';
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: text,
                num_sentences: sentences
            })
        });

        const data = await response.json();
        if (data.error) {
            summaryDiv.innerHTML = data.error;
        } else {
            summaryDiv.innerHTML = '<strong>Summary:</strong><br>' + data.summary;
        }
    } catch (error) {
        summaryDiv.innerHTML = 'Error: Could not connect to the server.';
    }
}

function clearAll() {
    document.getElementById('text').value = '';
    document.getElementById('summary').innerHTML = '';
    document.getElementById('sentences').value = '2';
}