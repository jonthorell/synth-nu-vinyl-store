
$(window).resize(function () {
    /* Hide / show the image div */
    if ($(window).width() < 1100) {
        $('#image-div').attr('style', 'display:none')
    }

    if ($(window).width() > 1100) {
        $('#image-div').attr('style', 'display:inline')
    }
});