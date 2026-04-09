// src/api/task.ts
import { client } from "./client";

export const getTasks = async () => {
  const res = await client.get("/tasks");
  return res.data;
};

export const createTask = async (data: { title: string }) => {
  const res = await client.post("/tasks", data);
  return res.data;
};
