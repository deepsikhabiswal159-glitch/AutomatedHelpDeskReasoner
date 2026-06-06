import { useState } from "react";

function Chatbot() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = () => {
    const text = message.toLowerCase();

    if (text.includes("password")) {
      setResponse("🔒 Please use the password reset option.");
    } else if (text.includes("course")) {
      setResponse("📚 Please contact the course coordinator.");
    } else if (text.includes("fee")) {
      setResponse("💳 Please visit the Accounts Department.");
    } else if (text.includes("login")) {
      setResponse("👤 Try resetting your credentials.");
    } else {
      setResponse(
        "🤖 Thank you for contacting the Helpdesk. Please create a support ticket for further assistance."
      );
    }
  };

  return (
    <div
      style={{
        background: "white",
        padding: "25px",
        borderRadius: "20px",
        boxShadow: "0 5px 15px rgba(0,0,0,0.08)",
      }}
    >
   <h2
        style={{
          color: "#2d1810",
          fontSize: "30px",
          fontWeight: "700",
          marginBottom: "15px",
        }}
      >
        🤖 Helpdesk Assistant
      </h2>

      <input
        type="text"
        placeholder="Ask a question..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{
          width: "100%",
          padding: "12px",
          marginTop: "10px",
          borderRadius: "10px",
          border: "2px solid #e6d8c7",
          boxSizing: "border-box",
          color: "#2d1810",
          fontSize: "16px",
        }}
      />

      <button
        onClick={handleSend}
        style={{
          marginTop: "12px",
          padding: "12px 20px",
          border: "none",
          borderRadius: "10px",
          background: "linear-gradient(90deg, #d8b08c, #9a5d34)",
          color: "white",
          fontWeight: "bold",
          cursor: "pointer",
        }}
      >
        Send →
      </button>

      {response && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            backgroundColor: "#f7f1e8",
            borderRadius: "12px",
            color: "#2d1810",
            fontSize: "16px",
            lineHeight: "1.5",
          }}
        >
          {response}
        </div>
      )}
    </div>
  );
}

export default Chatbot;