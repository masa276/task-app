import { useEffect, useState } from "react";
import { getTasks } from "../api/task";

export const TaskList = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(setTasks);
  }, []);

  return (
    <ul>
      {tasks.map((task: any) => (
        <li key={task.id}>{task.title}</li>
      ))}
    </ul>
  );
};
