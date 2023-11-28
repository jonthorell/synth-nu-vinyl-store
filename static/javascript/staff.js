//$('#delete-file-modal').on('click', '#delete-file-modal #confirm-delete-button', function (e) {
//    e.preventDefault();
//    console.log('confirmed delete');
//    return false;
//});

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



$('#info-modal .modal-footer button').on('click', function (event) {
    var $button = $(event.target);
    console.log($button[0].id)

});