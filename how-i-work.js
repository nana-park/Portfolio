document.addEventListener('DOMContentLoaded', () => {
    const accordionItems = document.querySelectorAll('.accordion-item');

    accordionItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all items
            accordionItems.forEach(i => i.classList.remove('active'));

            // Add active class to the clicked item
            item.classList.add('active');
        });
    });
});
