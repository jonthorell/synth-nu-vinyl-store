
$(window).resize(function () {
    /*Remove or add the border classes depending on screensize. The classes provides the vertical line between the divs*/
    if($(window).width() < 768)
    {
        $("#left_div").removeClass('border-end')
        $("#right_div").removeClass('border-start')
    }

    if ($(window).width() > 768) {
        $("#left_div").addClass('border-end')
        $("#right_div").addClass('border-start')
    }

});