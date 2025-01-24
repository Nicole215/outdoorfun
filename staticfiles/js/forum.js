// Add post form validation
document.getElementById("addPostForm")?.addEventListener("submit", function(event) {
    const title = document.getElementById("id_title");
    const content = document.getElementById("id_content");

    if (title.value.trim() === "") {
        alert("Title is required.");
        event.preventDefault();
    } else if (content.value.trim() === "") {
        alert("Content is required.");
        event.preventDefault();
    }
});

// Confirmation modal for deleting posts
document.addEventListener("DOMContentLoaded", function() {
    // Show the confirmation modal
    document.getElementById("confirmDelete")?.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the default action (e.g., link navigation)
        var myModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
        myModal.show();
    });

    // Handle the confirmation button inside the modal
    document.getElementById("confirmDeleteButton")?.addEventListener("click", function() {
        const deleteForm = document.getElementById("deleteForm");
        if (deleteForm) {
            deleteForm.submit(); // Submit the form to delete the post
        } else {
            console.error("Delete form not found");
        }  
    });
});