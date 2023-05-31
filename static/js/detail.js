const likeForm = document.getElementById('like-form');
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
if (likeForm !== null) {
  likeForm.addEventListener('click', function (event) {
  const postId = likeForm.dataset.postId;
  event.preventDefault();

  axios.defaults.headers.common['X-CSRFToken'] = csrfToken;

  axios.post(`/community/${postId}/like/`)
    .then(function (response) {
      const likeCountElement = document.querySelector('.commu-post-like');
      const likeCount = response.data.like_count;

      likeCountElement.textContent = likeCount;
    })
    .catch(function (error) {
      console.error('Error liking post:', error);
    });
});
}