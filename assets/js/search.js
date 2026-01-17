// Client-side search and filtering for Claude Skills Directory

(function() {
  'use strict';

  let searchIndex = [];
  const searchInput = document.getElementById('skill-search');
  const categoryFilter = document.getElementById('category-filter');
  const ratingFilter = document.getElementById('rating-filter');
  const sortBy = document.getElementById('sort-by');
  const skillsGrid = document.getElementById('skills-grid');

  // Load search index
  async function loadSearchIndex() {
    try {
      const response = await fetch('/Awesome-Claude/assets/js/search-index.json');
      searchIndex = await response.json();
    } catch (e) {
      console.log('Search index not loaded:', e);
    }
  }

  // Filter and display skills
  function filterSkills() {
    if (!skillsGrid) return;

    const searchTerm = searchInput?.value.toLowerCase() || '';
    const category = categoryFilter?.value || '';
    const minRating = parseFloat(ratingFilter?.value) || 0;
    const sort = sortBy?.value || 'rating';

    const cards = skillsGrid.querySelectorAll('.skill-card');

    cards.forEach(card => {
      const name = card.dataset.name || '';
      const cardCategory = card.dataset.category || '';
      const rating = parseFloat(card.dataset.rating) || 0;

      let visible = true;

      // Search filter
      if (searchTerm && !name.includes(searchTerm)) {
        visible = false;
      }

      // Category filter
      if (category && cardCategory !== category) {
        visible = false;
      }

      // Rating filter
      if (rating < minRating) {
        visible = false;
      }

      card.style.display = visible ? '' : 'none';
    });

    // Sort cards
    const visibleCards = Array.from(cards).filter(c => c.style.display !== 'none');

    visibleCards.sort((a, b) => {
      if (sort === 'rating') {
        return (parseFloat(b.dataset.rating) || 0) - (parseFloat(a.dataset.rating) || 0);
      } else if (sort === 'name') {
        return (a.dataset.name || '').localeCompare(b.dataset.name || '');
      }
      return 0;
    });

    // Reorder DOM
    visibleCards.forEach(card => {
      skillsGrid.appendChild(card);
    });
  }

  // Initialize
  function init() {
    loadSearchIndex();

    // Add event listeners
    if (searchInput) {
      searchInput.addEventListener('input', debounce(filterSkills, 200));
    }
    if (categoryFilter) {
      categoryFilter.addEventListener('change', filterSkills);
    }
    if (ratingFilter) {
      ratingFilter.addEventListener('change', filterSkills);
    }
    if (sortBy) {
      sortBy.addEventListener('change', filterSkills);
    }
  }

  // Debounce helper
  function debounce(func, wait) {
    let timeout;
    return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
