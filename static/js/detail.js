// 글 목록 요소를 선택합니다.
const posts = document.querySelectorAll('.commu_post');

// 글 목록 요소에 클릭 이벤트 리스너를 등록합니다.
posts.forEach(post => {
  post.addEventListener('click', () => {
    // 글의 pk 값을 가져옵니다.
    const pk = post.dataset.pk;
    
    // 서버로 글 디테일 정보 요청을 보냅니다.
    axios.get(`/community/${pk}/`)
      .then(response => {
        const data = response.data;
        
        // 받은 데이터를 HTML 요소에 업데이트합니다.
        document.getElementById('detail-category').textContent = data.category;
        document.getElementById('detail-user').textContent = data.user;
        document.getElementById('detail-title').textContent = data.title;
        document.getElementById('detail-content').textContent = data.content;
        // 추가 필드 등의 업데이트...
        
        // 글 디테일 영역을 보여줍니다.
        document.getElementById('detail-container').style.display = 'block';
      })
      .catch(error => {
        console.error('Error fetching post detail:', error);
      });
  });
});