import { useState } from "react";
import { Link } from "react-router-dom";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const baseUrl = process.env.REACT_APP_API_URL || 'https://app-llm.onrender.com';


  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(`${baseUrl}/login`
    // const res = await fetch("http://127.0.0.1:5000/login"
    , {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ username, password }),
    });
    const data = await res.json();
    setMsg(data.msg);
  };

  return (
    <div>
      <h2>登录</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="请输入用户名"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="请输入密码"
        />
        <button type="submit">登录</button>
      </form>
      <p>{msg}</p>
      <Link to="/register">去注册</Link>
    </div>
  );
}

export default LoginPage;
