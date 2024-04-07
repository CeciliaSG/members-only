    console.log("Document ready function reached.");

    $(document).on('click', '#like-button', function () {
        console.log("Like button clicked.");

        let postId = $(this).data('post-id');
        console.log("Post ID:", postId);

        $.ajax({
            type: 'POST',
            url: 'like_post/',
            data: {
                'post_id': postId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function (response) {
                alert(response.message);
                $('#like-count' + postId).text(response.likes);
            }
        });
    });