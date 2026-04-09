import React, { useEffect, useState } from "react";
import { getTasks, deleteTask, toggleTaskDone } from "../api/task";
import TaskForm from "../components/TaskForm";
import TaskList from "../components/TaskList";

export interface Task {
  id: number;
  title: string;
  description?: string;
  done: boolean;
}

const Home: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // タスク一覧取得
  const fetchTasks = async () => {
    try {
      setLoading(true);
      const data = await getTasks();
      setTasks(data);
    } catch (err) {
      console.error(err);
      setError("タスクの取得に失敗しました");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // タスク削除
  const handleDelete = async (id: number) => {
    try {
      await deleteTask(id);
      setTasks(tasks.filter((task) => task.id !== id));
    } catch (err) {
      console.error(err);
      setError("タスクの削除に失敗しました");
    }
  };

  // タスク完了切替
  const handleToggleDone = async (id: number) => {
    try {
      const updatedTask = await toggleTaskDone(id);
      setTasks(
        tasks.map((task) => (task.id === id ? updatedTask : task))
      );
    } catch (err) {
      console.error(err);
      setError("タスク更新に失敗しました");
    }
  };

  // 新規タスク追加
  const handleAddTask = (newTask: Task) => {
    setTasks([...tasks, newTask]);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">タスク一覧</h1>

      {error && <p className="text-red-500 mb-2">{error}</p>}

      <TaskForm onAddTask={handleAddTask} />

      {loading ? (
        <p>読み込み中...</p>
      ) : tasks.length === 0 ? (
        <p>タスクがありません</p>
      ) : (
        <TaskList
          tasks={tasks}
          onDelete={handleDelete}
          onToggleDone={handleToggleDone}
        />
      )}
    </div>
  );
};

export default Home;
