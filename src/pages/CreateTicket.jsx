import { useNavigate } from "react-router-dom";

function CreateTicket() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#f7f1e8",
        padding: "40px",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          width: "650px",
          backgroundColor: "white",
          padding: "40px",
          borderRadius: "25px",
          boxShadow: "0 10px 25px rgba(0,0,0,0.08)",
        }}
      >
        <h1
          style={{
            color: "#5c3b28",
            marginBottom: "10px",
          }}
        >
          🎫 Create Support Ticket
        </h1>
        
        <p
          style={{
            color: "#777",
            marginBottom: "30px",
          }}
        >
          Submit your issue and our helpdesk system will assist you.
        </p>

        <input
          type="text"
          placeholder="📝 Issue Title"
          style={inputStyle}
        />

        <select style={inputStyle}>
          <option>📂 Select Category</option>
          <option>Technical Issue</option>
          <option>Course Access</option>
          <option>Account Problem</option>
          <option>Fee Related</option>
          <option>Other</option>
        </select>

        <select style={inputStyle}>
          <option>🚨 Select Priority</option>
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>

        <textarea
          placeholder="📄 Describe your issue..."
          rows="6"
          style={{
            ...inputStyle,
            resize: "none",
          }}
        />

        <div
          style={{
            display: "flex",
            gap: "15px",
          }}
        >
          <button
            style={buttonStyle}
            onClick={() => navigate("/dashboard")}
          >
            🚀 Submit Ticket
          </button>

          <button
            style={cancelButtonStyle}
            onClick={() => navigate("/dashboard")}
          >
            ↩ Cancel
          </button>
        </div>
      </div>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "15px",
  marginBottom: "18px",
  borderRadius: "12px",
  border: "2px solid #e6d8c7",
  fontSize: "16px",
  boxSizing: "border-box",
};

const buttonStyle = {
  flex: 1,
  padding: "15px",
  border: "none",
  borderRadius: "12px",
  background: "linear-gradient(90deg, #d8b08c, #9a5d34)",
  color: "white",
  fontSize: "18px",
  fontWeight: "bold",
  cursor: "pointer",
};

const cancelButtonStyle = {
  flex: 1,
  padding: "15px",
  border: "2px solid #d8b08c",
  borderRadius: "12px",
  background: "white",
  color: "#5c3b28",
  fontSize: "18px",
  fontWeight: "bold",
  cursor: "pointer",
};

export default CreateTicket;