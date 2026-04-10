import client from "./client";

// ログイン
export const loginUser = async (email: string, password: string) => {
  const res = await client.post("/auth/login", { email, password });
  return res.data;
};

// 新規登録
export const registerUser = async (email: string, password: string, name: string) => {
  const res = await client.post("/auth/register", { email, password, name });
  return res.data;
};
