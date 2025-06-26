const fileUploadForm = document.getElementById("fileUploadForm");
const fileInput = document.getElementById("dropzone-file");

const API_ROUTE = "http://localhost:8000/api/v1";

fileUploadForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData();
  const file = fileInput.files[0];
  formData.append("file", file);

  fetch(`${API_ROUTE}/file`, {
    credentials: "include",
    method: "POST",
    body: formData,
  })
    .then((response) => {
      if (!response.status == "201") {
        console.log("its fine");
      } else {
        console.log("something wrong");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
    });
});
