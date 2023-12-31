
$(window).resize(function () {
    /*Remove or add the border classes depending on screensize. The classes provides the vertical line between the divs */
    if($(window).width() < 768)
    {
        $("#left_div").removeClass('border-end')
        $("#right_div").removeClass('border-start')
    }

    if ($(window).width() > 768) {
        $("#left_div").addClass('border-end')
        $("#right_div").addClass('border-start')
    }

    /* Hide/show the spans with the published date */

    if ($(window).width() < 500) {
        $(".published").hide()
    }

    if ($(window).width() > 500) {
        $(".published").show()
    }

});

/* the code to populate the modal comes from the mdb documentation */

const infoModal = document.getElementById('info-modal');

infoModal.addEventListener('show.mdb.modal', (e) => {
    // Button that triggered the modal
    const button = e.relatedTarget;
    // Extract info from data-mdb-* attributes
    const title = button.getAttribute('data-mdb-title');
    const body = button.getAttribute('data-mdb-body');
    
    // Update the modal's content.
    const modalTitle = infoModal.querySelector('.modal-title');
    const modalBodyInput = infoModal.querySelector('.modal-body');

    modalTitle.textContent = title;
    modalBodyInput.textContent = body;
});