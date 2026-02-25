// Utility to get CSRF tokens from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== null) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Global cart update function
window.updateCartUI = function(cartCount, inCart, buttonElement, listingId, item_quantity) {
    const cartButton = document.getElementById('cartButton');
    const cartCountBadge = document.getElementById('cartCountBadge');
    
    if (cartButton && cartCountBadge) {
        cartCountBadge.textContent = cartCount;
        cartButton.dataset.count = cartCount;
        
        if (cartCount > 0) {
            cartButton.classList.add('show');
        } else {
            cartButton.classList.remove('show');
        }
    }

    if (item_quantity === 0) {
        // Find the specific item card using the listingId
        const card = document.querySelector(`.cart-item[data-listing-id="${listingId}"]`);
        
        // Only remove if we are physically on the cart page URL
        if (card && window.location.pathname.includes('/cart/')) {
            card.style.opacity = '0';
            card.style.transition = 'opacity 0.3s ease';
            
            setTimeout(() => {
                card.remove();
                
                // If it was the last item, show the "Empty" message
                const container = document.querySelector('.cart-page');
                if (container && document.querySelectorAll('.cart-item').length === 0) {
                    container.innerHTML = '<h2 class="mb-4">Your cart</h2><p>Your cart is empty.</p>';
                }
            }, 300);
            return; // Exit early since the item is gone
        }
    }
    
    if (buttonElement) {
        if (inCart) {
            buttonElement.classList.add('in-cart');
            buttonElement.textContent = 'Remove from cart';
        } else {
            buttonElement.classList.remove('in-cart');
            buttonElement.textContent = '🛒 Add to cart';
        }
    }
    
    const qtySpan = document.getElementById(`qty-${listingId}`);
    if (qtySpan) {
        qtySpan.textContent = item_quantity;
    }

    const controls = document.getElementById(`cart-controls-${listingId}`);
    if (controls) {
        if (inCart && item_quantity > 0) {
            controls.style.display =   'inline-flex';
        } else {
            controls.style.display = 'none';
        }
    }
    
    
};