// delete 클래스명 이용
// 삭제 클릭 시 confirm()
const deleteAll = document.querySelectorAll(".delete");

deleteAll.forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();

    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.href;
    }
  });
});
