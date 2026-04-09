import client from "./client";

// タスク取得
export const getTasks = async () => {
  const res = await client.get("/tasks");
  return res.data;
};

// タスク作成
export const createTask = async (data: { title: string; description?: string }) => {
  const res = await client.post("/tasks", data);
  return res.data;
};

// ✅ タスク削除
export const deleteTask = async (id: number) => {
  const res = await client.delete(`/tasks/${id}`);
  return res.data;
};

// タスク更新
export const updateTask = async (id: number, data: { title?: string; description?: string }) => {
  const res = await client.put(`/tasks/${id}`, data);
  return res.data;
};
