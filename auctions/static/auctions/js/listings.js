document.addEventListener('DOMContentLoaded', function() {
    // Listening to the entire document
    document.addEventListener('click', function(event) {
        // Find the closest parent that is a listing card
        const card = event.target.closest('.listing-card');
        
        // If the click wasn't inside a card, or if it was on a button/control, STOP.
        if (!card || 
            event.target.closest('button') || 
            event.target.closest('.qty-btn-decrease') || 
            event.target.closest('.qty-btn-increase')) {
            return;
        }

        // If we got here, it's a valid card click
        const listingId = card.dataset.listingId;
        if (listingId) {
            window.location.href = `/listing/${listingId}`;
        }
    });
});