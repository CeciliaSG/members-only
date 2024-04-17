let updateProfileBtn = document.getElementById('update-profile-btn');
if (updateProfileBtn) {
    updateProfileBtn.addEventListener('click', function () {
        this.style.backgroundColor = "red";
    });
}
let likeButton = document.getElementsByClassName('btn-like');
for (let i = 0; i < likeButton.length; i++) {
    likeButton[i].addEventListener('click', function (event) {
        event.preventDefault();
        let postId = this.getAttribute('data-post-id');
        $.ajax({
            url: '/like_post/' + postId + '/',
            success: function (response) {
                alert(response.message);
            },
            error: function (xhr, status, error) {
                alert('An error occurred!');
            }
        });
    });
}

let saveButton = document.getElementsByClassName('btn-save-post');
for (let i = 0; i < saveButton.length; i++) {
    saveButton[i].addEventListener('click', function (event) {
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
}