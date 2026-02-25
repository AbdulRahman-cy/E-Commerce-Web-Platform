document.addEventListener('DOMContentLoaded', function() {
    // Event Delegation for all Cart-related buttons
    document.addEventListener('click', async function(event) {
        const target = event.target;

        // Check if we clicked an add/remove cart button or quantity button
        if (target.classList.contains('cart-btn') || 
            target.classList.contains('qty-btn-increase') || 
            target.classList.contains('qty-btn-decrease')) {
            
            event.preventDefault();

            const listingId = target.dataset.listingId;
            const url = target.dataset.cartUrl;
            const csrftoken = getCookie('csrftoken');
            
            // Determine the action for the backend
            let action = 'toggle'; // Default for the main cart button
            if (target.classList.contains('qty-btn-increase')) action = 'increase';
            if (target.classList.contains('qty-btn-decrease')) action = 'decrease';

            try {
                const response = await fetch(url, {
                    method: "POST",
                    headers: {
                        'X-CSRFToken': csrftoken,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ action: action })
                });
                
                const data = await response.json();
                
                // Find the main cart button for this specific listing to update its state
                const mainCartBtn = document.querySelector(`.cart-btn[data-listing-id="${listingId}"]`);
                
                // Call the global UI update function to change the button or controls
                if (window.updateCartUI) {
                    window.updateCartUI(data.cart_count, data.in_cart, mainCartBtn, listingId, data.item_quantity);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        }
    });
});