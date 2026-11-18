// Guarda de ruta por rol (RF-025). La autorización real siempre se valida en el backend.
import { api, haySesion } from "./api.js";

export async function requerirSesion(rolesPermitidos = null) {
  if (!haySesion()) { location.href = "index.html"; return null; }
  const yo = await api("/auth/me/");
  if (rolesPermitidos && !rolesPermitidos.includes(yo.rol)) { location.href = "dashboard.html"; return null; }
  document.querySelectorAll("[data-usuario]").forEach((el) => (el.textContent = `${yo.username} (${yo.rol})`));
  return yo;
}
