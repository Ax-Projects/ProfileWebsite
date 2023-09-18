const shareButton = document.querySelectorAll('.tile-share-button').forEach((button) => {
    button.addEventListener('click', copyText)
})

async function copyText(e) {
    e.preventDefault();
    const link = this.getAttribute('link')
    try {
        await navigator.clipboard.writeText(link);
        this.classList.add('flash');
        setTimeout(() => {
            this.classList.remove('flash');
        }, 1000);
    } catch (e) {
        console.log(e)
    }
}