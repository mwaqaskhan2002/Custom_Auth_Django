// Login Page 

// Password Show/Hide Function
function togglePassword(spanElement) {
  // span ke andar input dhundo — sibling element
  const passwordField =
    spanElement.previousElementSibling.previousElementSibling;
  const toggleicon = spanElement.querySelector("i");

  if (passwordField.type === "password") {
    passwordField.type = "text";
    toggleicon.classList.remove("bi-eye-slash-fill");
    toggleicon.classList.add("bi-eye-fill");
  } else {
    passwordField.type = "password";
    toggleicon.classList.remove("bi-eye-fill");
    toggleicon.classList.add("bi-eye-slash-fill");
  }
}
