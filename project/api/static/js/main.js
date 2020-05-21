const inputSubmit = document.getElementById("input-submit");

let radio2Group1 = document.getElementById("radio-2-group-1");
let radio2Group2 = document.getElementById("radio-2-group-2");

const generatedText = document.getElementById("generated-text");

const generateSectionTitle = document.getElementById("generate-section-title");

const generatedTitle = document.getElementById("generated-title");
const generatedContent = document.getElementById("generated-content");

let radio1String = "";
let radio2String = "";


handleRadio1 = (radioValue) => {
  radio1String = radioValue.value;
  // if (radio1String == "dcinside") {
  //	radio2Group1.style.display = "block";
  //	radio2Group2.style.display = "none";
  // } else {
  //	radio2Group2.style.display = "block";
  //	radio2Group1.style.display = "none";
  // }
};

// handleRadio2 = (radioValue) => {
//   radio2String = radioValue.value;
// };

const spinner = document.getElementById("spinner");

function showSpinner() {
  spinner.className = "show";
}

function hideSpinner() {
  spinner.className = spinner.className.replace("show", "");
}

inputSubmit.addEventListener("click", (e) => {
  generatedText.innerHTML = '';
  showSpinner();
  generateSectionTitle.style.display = "none";

  sendObj = {
	community: radio1String,
	category: radio2String,
  };

  e.preventDefault();
  fetch("/generate", {
	method: "POST",
	headers: {
	  "Content-Type": "application/json"
	},
	body: JSON.stringify(sendObj)
  })
	.then(resp => {
	  if (resp.ok)
		resp.json().then(data => {
		  hideSpinner();

		  generateSectionTitle.style.display = "block";
		  titleDiv = document.createElement("div");
		  titleDiv.id = "title-text";
		  titleStrong = document.createElement("strong");
		  titleStrong.innerHTML = "Title: ";
		  titleDiv.append(titleStrong);
		  titleContent = document.createElement("span");
		  titleContent.innerHTML = data.title;
		  titleDiv.append(titleContent);

		  contentDiv = document.createElement("div");
		  contentDiv.id = "content-text";
		  contentStrong = document.createElement("strong");
		  contentStrong.innerHTML = "Content: ";
		  contentDiv.append(contentStrong);
		  contentContent = document.createElement("span");
		  contentContent.innerHTML = data.content;
		  contentDiv.append(contentContent);

		  generatedText.append(titleDiv);
		  generatedText.append(contentDiv);
		});
	})
	.catch(err => {
	  console.log("An error occured", err.message);
	  window.alert("Oops! Something went wrong.");
	});
}, false);


function displayResult(data) {
  hide(loader);
  predResult.innerHTML = data.result;
  show(predResult);
}

function hide(el) {
  // hide an element
  el.classList.add("hidden");
}

function show(el) {
  // show an element
  el.classList.remove("hidden");
}
