import { useState } from "react";
import { createTask } from "../api/task";

export const TaskForm = () => {
  const [title, setTitle] = useState("");

  const handleSubmit = async () => {
    await createTask({ title });
    setTitle("");
  };

  return (
    <div>
      <input value={title} onChange={(e) => setTitle(e.target.value)} />
      <button onClick={handleSubmit}>追加</button>
    </div>
  );
};
