document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', async function(event) {
        const button = event.target.closest('.like-btn');
        if (!button) return;

        event.preventDefault();
        const url = button.dataset.likeUrl;
        
        // getCookie is available because it's in layout.html
        const csrftoken = getCookie('csrftoken'); 

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({})
            });
            
            const data = await response.json();
            button.querySelector('.like-count').textContent = data.count;

            if (data.liked) {
                button.classList.add('liked');
            } else {
                button.classList.remove('liked');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});