// Show all toasts
document.addEventListener('DOMContentLoaded', function () {
    const toastsEl = document.querySelectorAll('.toast')
    toastsEl.forEach(function (toastEl, index) {
        setTimeout(function () {
            var toast = new bootstrap.Toast(toastEl)
            toast.show()
        }, index * 600)
    })
})
