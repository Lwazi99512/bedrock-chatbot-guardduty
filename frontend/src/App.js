import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://localhost:8000/chat", {
        user_input: input,
      });
      setResponse(res.data.reply);
    } catch (error) {
      console.error("Error communicating with backend:", error);
      setResponse("Something went wrong. Try again.");
    }
  };

  return (
    <div className="App">
      <h2>🧠 Bedrock Chatbot</h2>
      <input
        type="text"
        placeholder="Ask me anything..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={handleSubmit}>Send</button>
      <p><strong>Bot:</strong> {response}</p>
    </div>
  );
}

export default App;
 