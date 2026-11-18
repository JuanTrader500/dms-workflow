import { login } from "./api.js";

document.getElementById("form-login").addEventListener("submit", async (e) => {
  e.preventDefault();
  const error = document.getElementById("error");
  error.textContent = "";
  try {
    await login(e.target.usuario.value, e.target.clave.value);
    location.href = "dashboard.html";
  } catch (err) { error.textContent = err.message; }
});
