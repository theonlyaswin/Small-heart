const final = document.getElementById("final");
const btn = document.getElementById("copy-button");

btn.addEventListener("click", copyText);

// CopyText Function
function copyText() {
  final.select();
  document.execCommand("copy");
  btn.value = "Copied!";
}