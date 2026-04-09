import React, { useEffect, useState } from "react";
import { getTasks, deleteTask } from "../api/task";

const Home = () => {
  const [tasks, setTasks] = useState<any[]>([]);

  const fetchTasks = async () => {
    const data = await getTasks();
    setTasks(data);
  };

  const handleDelete = async (id: number) => {
    await deleteTask(id);
    fetchTasks();
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div>
      <h1>Task List</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            {task.title} <button onClick={() => handleDelete(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
