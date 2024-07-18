"use strict";

let likeButtons = document.getElementsByClassName('btn-like');

Array.from(likeButtons).forEach(likeButton => {
    likeButton.addEventListener('click', function (event) {
        event.preventDefault();
        let postId = this.getAttribute('data-post-id');
        let button = this;
        let icon = button.querySelector('i');

        $.ajax({
            url: '/like_post/' + postId + '/',
            success: function (response) {
                if (response.message === "You liked the post!") {
                    button.classList.add('liked');
                    icon.style.color = 'red';
                } else {
                    button.classList.remove('liked');
                    icon.style.color = '';
                }
                alert(response.message);
            },
            error: function (xhr, status, error) {
                alert('An error occurred!');
            }
        });
    });
});

let saveButtons = document.getElementsByClassName('btn-save-post');

Array.from(saveButtons).forEach(saveButton => {
    saveButton.addEventListener('click', function (event) {
        event.preventDefault();
        let postId = this.getAttribute('data-post-id');
        $.ajax({
            url: '/save_post/' + postId + '/',
            success: function (response) {
                alert(response.message);
            },
            error: function (xhr, status, error) {
                alert('An error occurred!');
            }
        });
    });
});


// Messages
document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll('#messages .messages');
    messages.forEach(message => {
        message.style.opacity = 1;
        setTimeout(() => {
            message.style.opacity = 0;
            setTimeout(() => {
                message.remove();
            }, 500);
        }, 4000);
    });
});

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
 * From Blog walkthrough
 * Initialises edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
}


/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */
document.addEventListener("DOMContentLoaded", () => {

    // Handling comment delete modal
    const deleteModal = document.getElementById("deleteModal");
    if (deleteModal) {
        const deleteModalInstance = new bootstrap.Modal(deleteModal);
        const deleteButtons = document.getElementsByClassName("btn-delete");
        const deleteConfirm = document.getElementById("deleteConfirm");

        if (deleteConfirm) {
            for (let button of deleteButtons) {
                button.addEventListener("click", (e) => {
                    let commentId = e.target.getAttribute("comment_id");
                    deleteConfirm.href = `delete_comment/${commentId}`;
                    deleteModalInstance.show();
                });
            }
        }
    }

    // Handling post delete modal
    const deletePostModal = document.getElementById("deletePostModal");
    if (deletePostModal) {
        const deletePostModalInstance = new bootstrap.Modal(deletePostModal);
        const deletePostButtons = document.getElementsByClassName("btn-post-delete");
        const deletePostConfirm = document.getElementById("deletePostConfirm");

        if (deletePostConfirm) {
            for (let button of deletePostButtons) {
                button.addEventListener("click", (e) => {
                    e.preventDefault();
                    let postId = e.target.getAttribute("data_post_id");
                    let postSlug = e.target.getAttribute("data_post_slug");
                    deletePostConfirm.href = `/posts/${postSlug}/delete/${postId}/`;
                    deletePostModalInstance.show();
                });
            }
        }
    }
});


$(document).ready(function () {
    $('#loginModal').modal('show');
});