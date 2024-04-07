$(document).ready(function () {
            console.log("Document ready function reached.");
            $('#like-button').click(function () {
                        console.log("Like button clicked.");
                        let postId = $(this).data('post-id');
                        console.log("Post ID:", postId);
                        let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
                        console.log("CSRF Token:", csrfToken);