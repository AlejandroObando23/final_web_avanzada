export const request = async <T = any>(
  method: "GET" | "POST" | "PUT" | "DELETE",
  path: string,
  body: any = null
): Promise<T> => {
  const BASE_URL = import.meta.env.VITE_API_URL || "https://productosweb.duckdns.org/api";
  
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };

  const config: RequestInit = {
    method,
    headers,
  };

  if (body !== null && (method === "POST" || method === "PUT")) {
    config.body = JSON.stringify(body);
  }

  const response = await fetch(`${BASE_URL}${path}`, config);
  const responseData = await response.json();

  if (!response.ok) {
    throw new Error(responseData.detail || "Error en la petición API");
  }

  return responseData as T;
};
