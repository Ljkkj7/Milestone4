// Custom confirmation modal for delete action
document.addEventListener('DOMContentLoaded', function () {
    const openBtn = document.getElementById('delete-open-btn');
    const modal = document.getElementById('confirm-modal');
    const confirmBtn = document.getElementById('confirm-delete');
    const cancelBtn = document.getElementById('cancel-delete');
    const form = document.getElementById('delete-form');

    if (!openBtn || !modal) return;

    function openModal() {
        modal.setAttribute('aria-hidden', 'false');
        modal.classList.add('open');
        document.body.classList.add('no-scroll');
        // Focus first actionable element
        if (confirmBtn) confirmBtn.focus();
            // Auto-close after 5 seconds
            if (modal._autoCloseTimeout) clearTimeout(modal._autoCloseTimeout);
            modal._autoCloseTimeout = setTimeout(() => {
                closeModal();
            }, 5000);
    }

    function closeModal() {
        modal.setAttribute('aria-hidden', 'true');
        modal.classList.remove('open');
        document.body.classList.remove('no-scroll');
        openBtn.focus();
    }

    openBtn.addEventListener('click', function (e) {
        e.preventDefault();
        openModal();
    });

    cancelBtn.addEventListener('click', function (e) {
        e.preventDefault();
        closeModal();
    });

    // Confirm -> submit form
    confirmBtn.addEventListener('click', function (e) {
        e.preventDefault();
        if (form) form.submit();
    });

    // Close on outside click
    modal.addEventListener('click', function (e) {
        if (e.target === modal) closeModal();
    });

    // Close on Esc
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeModal();
    });
});
