// 하단의 페이지 나누기 영역 클릭 시
// href 값 가져오기

document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault();

  let href = e.target.getAttribute("href");
  // console.log(href);

  // 페이지 값이 있다면 페이지값을 업데이트하고 폼 제출
  if (href) {
    document.querySelector("#page").value = href;
    document.querySelector("#actionForm").submit();
  }
});
