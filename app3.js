$(document).ready(function() {
    let imageCount = 100;  // Initial number of images to display
    let loadIncrement = 20;  // Number of images to load each time we reach the bottom
    let allImages = [];  // Array to store all the image paths

    // Generate the array with all the image paths
    for (let i = 1; i <= 199; i++) {  // Assume you have 50 images
        let thumbnail = '/images/thumbnails/image' + i + '.png';
        let src = '/images/image' + i + '.png';
        allImages.push({thumbnail: thumbnail, src: src});
    }

    // Shuffle the array
    allImages.sort(() => Math.random() - 0.5);

    function loadImages() {
        let html = '';
        for (let i = 0; i < imageCount && i < allImages.length; i++) {
            let image = allImages[i];
            html += '<div class="image-wrapper">';
            html += '<a href="' + image.src + '" data-fancybox>';
            html += '<img src="' + image.thumbnail + '" class="img-fluid">';
            html += '</a>';
            html += '</div>';
        }
        $('#imageGallery').html(html);
    }

    // Initial load
    loadImages();

    $(window).scroll(function() {
        if ($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
            imageCount += loadIncrement;
            loadImages();
        }
    });
});

