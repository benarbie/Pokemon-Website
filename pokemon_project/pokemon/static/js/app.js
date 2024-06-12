document.querySelectorAll('.form-item').forEach(item => {
    item.addEventListener('click', function() {
        var imageURL = this.dataset.image;
        
        // Set the image source
        document.getElementById('mon-image').src = imageURL;
    });
});