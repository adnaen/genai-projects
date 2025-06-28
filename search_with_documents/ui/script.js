const fileUploadForm = document.getElementById("fileUploadForm");
const fileInput = document.getElementById("dropzone-file");
const fileResultField = document.getElementById("fileDataSection");
const docStatus = document.getElementById("docStatus");
const prompt = document.getElementById("promptArea");
const chatForm = document.getElementById("chatForm");
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
      addNewFileInfo(data, id, data.name, data.created_at);
    })
    .catch((err) => {
      alert(`something went wrong : ${err}`);
    });
});

const fetchFileInfo = async () => {
  try {
    const response = await fetch(`${API_ROUTE}/file`, {
      method: "GET",
    });

    if (response.status == 200) {
      const data = await response.json();
      console.log("its coming");
      data.forEach((each) => {
        addNewFileInfo(each.id, each.name, each.created_at);
      });
    }
  } catch (err) {
    docStatus.classList.remove("hidden");
  }
};

const info = fetchFileInfo();

const addNewFileInfo = (id, filename, date) => {
  const divHere = document.createElement("div");
  const div2Here = document.createElement("div");

  const labelHere = document.createElement("label");
  const inputRadio = document.createElement("input");
  labelHere.className = "flex gap-4 cursor-pointer";

  inputRadio.type = "radio";
  inputRadio.name = "fileContext";
  inputRadio.value = id;

  const h3Here = document.createElement("h3");
  h3Here.className = "text-lg font-bold text-white";
  h3Here.innerText = filename;

  const spanHere = document.createElement("span");
  spanHere.className = "text-md text-slate-400";
  spanHere.innerText = date;

  labelHere.appendChild(inputRadio);
  div2Here.appendChild(h3Here);
  div2Here.appendChild(spanHere);
  labelHere.appendChild(div2Here);

  divHere.appendChild(labelHere);

  fileResultField.appendChild(divHere);
};

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const selectedFileContext = document.querySelector(
    'input[name="fileContext"]:checked',
  );
  if (!selectedFileContext) {
    alert("please choose an file context before prompt");
    return;
  }

  if (prompt.value == "") {
    alert("type anything on prompt field");
    return;
  }

  const formData = new FormData();
  formData.append("prompt", prompt.value);
  formData.append("file_id", selectedFileContext.value);

  console.log(`choosed file id : ${selectedFileContext.value}`);
  console.log(`prompt: ${prompt.value}`);
});
