const fileUploadForm = document.getElementById("fileUploadForm");
const fileInput = document.getElementById("dropzone-file");
const fileResultField = document.getElementById("fileDataSection");
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
      console.log(response.status);
      if (!response.ok) {
        throw new Error(
          `something went wrong with status code : ${response.status}`,
        );
      } else {
        return response.json();
      }
    })
    .then((data) => {
      addNewFileInfo(data.name, data.created_at);
    })
    .catch((err) => {
      alert(`something went wrong : ${err}`);
    });
});

const fetchFileInfo = async () => {
  const response = await fetch(`${API_ROUTE}/file`, {
    method: "GET",
  });

  if (response.status == 200) {
    const data = await response.json();
    data.forEach((each) => {
      addNewFileInfo(each.name, each.created_at);
    });
  }
};

const info = fetchFileInfo();

const addNewFileInfo = (filename, date) => {
  const divHere = document.createElement("div");

  const h3Here = document.createElement("h3");
  h3Here.className = "text-lg font-bold text-white";
  h3Here.innerText = filename;

  const spanHere = document.createElement("span");
  spanHere.className = "text-md text-slate-400";
  spanHere.innerText = date;

  divHere.appendChild(h3Here);
  divHere.appendChild(spanHere);

  fileResultField.appendChild(divHere);
};
