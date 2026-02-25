document.addEventListener('DOMContentLoaded', function() {
    const categories = document.querySelectorAll('.category-card');
    const selectedCategoriesInput = document.getElementById('selectedCategoriesInput');
    const countText = document.getElementById('countText');
    const selectedCount = document.getElementById('selectedCount');
    
    // We use a Set to handle unique IDs efficiently
    const selectedCategories = new Set();

    // Initial load: Add categories that might be pre-selected (from Django backend)
    document.querySelectorAll('.category-card.selected').forEach(function(category) {
        selectedCategories.add(category.dataset.category);
    });

    function updateUI() {
        const count = selectedCategories.size;
        
        // Update the floating count badge
        if (count > 0) {
            countText.textContent = `${count} categor${count !== 1 ? 'ies' : 'y'} selected`;
            selectedCount.classList.add('show');
        } else {
            selectedCount.classList.remove('show');
        }

        // Convert Set to comma-separated string for the hidden input field
        selectedCategoriesInput.value = Array.from(selectedCategories).join(',');
    }

    categories.forEach(function(category) {
        // Toggle selection on click
        category.addEventListener('click', function() {
            const categoryId = this.dataset.category;
            
            if (this.classList.contains('selected')) {
                this.classList.remove('selected');
                selectedCategories.delete(categoryId);
            } else {
                this.classList.add('selected');
                selectedCategories.add(categoryId);
            }

            updateUI();
        });

        // Accessibility: Allow Enter or Space key to trigger selection
        category.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });

    // Run once on load to sync UI with initial state
    updateUI();
});