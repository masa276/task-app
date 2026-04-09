import client from "./client";

export const login = async (email: string, password: string) => {
  const res = await client.post("/auth/login", { email, password });
  return res.data;
};

export const register = async (email: string, password: string, name: string) => {
  const res = await client.post("/auth/register", { email, password, name });
  return res.data;
};
