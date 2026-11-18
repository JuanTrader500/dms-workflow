import { logout } from "./api.js";
import { requerirSesion } from "./guard.js";

document.getElementById("salir").addEventListener("click", logout);
const yo = await requerirSesion(null);
// TODO: implementar la pantalla "Alertas y notificaciones" según .opencode/PLAN_DESARROLLO_MVP.md §11
