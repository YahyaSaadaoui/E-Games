document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.wishlist-button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const gameId = this.dataset.gameId;

            // Check if gameId is a non-empty string consisting of digits
            if (!gameId || !/^\d+$/.test(gameId)) {
                console.error('Invalid game_id:', gameId);
                return;
            }

            const url = `wishlist/add/${gameId}/`;
            const data = { game_id: gameId };

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),  // Include the CSRF token
                },
                body: JSON.stringify(data),
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('Network response was not OK');
            })
            .then(result => {
                // Handle the response as needed
                console.log(result);
            })
            .catch(error => {
                // Handle errors
                console.error(error);
            });
        });
    });

    function getCSRFToken() {
        const cookieValue = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken='))
            .split('=')[1];
        return cookieValue;
    }
});
