let updateProfileBtn = document.getElementById('update-profile-btn');
if (updateProfileBtn) {
    updateProfileBtn.addEventListener('click', function () {
        this.style.backgroundColor = "red";
    });
}
let likeButtons = document.getElementsByClassName('btn-post');
for (let i = 0; i < likeButtons.length; i++) {
    likeButtons[i].addEventListener('click', function (event) {
        event.preventDefault();
        let postId = this.getAttribute('data-post-id');
        $.ajax({
            url: '/like_post/' + postId + '/',
            success: function (response) {
                alert(response.message);
            },
            error: function (xhr, status, error) {
                alert('An error occurred! ');
            }
        });
    });
}