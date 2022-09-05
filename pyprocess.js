var script = document.currentScript.getAttribute('data-script');

const loadingIndicator = () => document.getElementById("loading-indicator");
const processButton = () => document.getElementById("process");
const fileInput = () => document.getElementById("fileItem");
const resultElement = () => document.getElementById("results");
const summaryElement = () => document.getElementById("summary");
const htmlElement = () => document.getElementById("html");

const pyWorker = new Worker("../pyworker.js");

pyWorker.onerror = console.log;
pyWorker.onmessage = (event) => {
  const { eventType } = event.data;
  if (eventType === "result") {
    setControlsDisabled(false);
    summaryElement().textContent = event.data.result.summary;
    htmlElement().innerHTML = event.data.result.html;
    resultElement().style.display = "block";
    console.log(event.data.result);
  } else if (eventType === "initialized") {
    fetch(script)
    .then(response => response.text())
    .then((script) => {
      pyWorker.postMessage({ eventType: "loadScript", script});
    })
    .then(() => {
      loadingIndicator().hidden = true;
      fileInput().disabled = false;
    })
  }
};  

function toggleProcessButton() {
  const file = fileInput().files[0];
  processButton().disabled = file === undefined;
};

function setControlsDisabled(disabled) {
  fileInput().disabled = disabled;
  processButton().disabled = disabled;
};

function process() {
  console.log("process: started");

  setControlsDisabled(true);
  resultElement().style.display = "none";

  const file = fileInput().files[0];
  const reader = file.stream().getReader();
  const sendToWorker = ({ done, value }) => {
    if (done) {
      console.log("process: runPy");
      pyWorker.postMessage({ eventType: "processData" });
      return;
    }
    console.log("process: send event: data");
    pyWorker.postMessage({ eventType: "data", chunk: value });
    reader.read().then(sendToWorker);
  };
  console.log("process: send event: initData");
  pyWorker.postMessage({ eventType: "initData", size: file.size });
  reader.read().then(sendToWorker);
}

