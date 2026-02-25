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