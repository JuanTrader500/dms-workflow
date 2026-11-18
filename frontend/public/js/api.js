// Cliente HTTP mínimo. Access token en memoria; refresh en sessionStorage (se borra al cerrar la pestaña).
const API = "/api/v1";
let accessToken = null;

export function haySesion() { return !!(accessToken || sessionStorage.getItem("refresh")); }

async function refrescar() {
  const refresh = sessionStorage.getItem("refresh");
  if (!refresh) return false;
  const r = await fetch(`${API}/auth/refresh/`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ refresh }) });
  if (!r.ok) return false;
  accessToken = (await r.json()).access;
  return true;
}

export async function login(username, password) {
  const r = await fetch(`${API}/auth/login/`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ username, password }) });
  if (!r.ok) throw new Error("Credenciales inválidas");
  const d = await r.json();
  accessToken = d.access;
  sessionStorage.setItem("refresh", d.refresh);
}

export function logout() { accessToken = null; sessionStorage.removeItem("refresh"); location.href = "index.html"; }

export async function api(ruta, { method = "GET", body, form } = {}) {
  if (!accessToken && !(await refrescar())) { location.href = "index.html"; return; }
  const headers = { Authorization: `Bearer ${accessToken}` };
  let payload;
  if (form) { payload = form; } else if (body) { headers["Content-Type"] = "application/json"; payload = JSON.stringify(body); }
  let r = await fetch(`${API}${ruta}`, { method, headers, body: payload });
  if (r.status === 401 && (await refrescar())) { headers.Authorization = `Bearer ${accessToken}`; r = await fetch(`${API}${ruta}`, { method, headers, body: payload }); }
  const datos = r.status === 204 ? null : await r.json().catch(() => null);
  if (!r.ok) { const e = new Error(datos?.detalle || "Error en la solicitud"); e.estado = r.status; e.datos = datos; throw e; }
  return datos;
}
