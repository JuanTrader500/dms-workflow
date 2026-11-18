import { logout } from "./api.js";
import { requerirSesion } from "./guard.js";

document.getElementById("salir").addEventListener("click", logout);
const yo = await requerirSesion(["AUXILIAR_ADMIN_PERSONAL", "CONTABILIDAD"]);
// TODO: implementar la pantalla "Conciliación contable" según .opencode/PLAN_DESARROLLO_MVP.md §11
