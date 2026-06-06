import { useNavigate } from "react-router-dom";
import Chatbot from "../components/Chatbot";

function Dashboard() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#f7f1e8",
        padding: "30px",
        color: "#3b2416",
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: "25px",
        }}
      >
        <h1
          style={{
            fontSize: "42px",
            color: "#4a2c1a",
            margin: 0,
          }}
        >
          🎧 Helpdesk Dashboard
        </h1>

        <div
          style={{
            display: "flex",
            gap: "12px",
          }}
        >
          <button
            onClick={() => navigate("/create-ticket")}
            style={buttonStyle}
          >
            ➕ Create Ticket
          </button>

          <button
            onClick={() => navigate("/")}
            style={buttonStyle}
          >
            🚪 Logout
          </button>
        </div>
      </div>

      <div
        style={{
          display: "flex",
          gap: "20px",
          marginBottom: "30px",
        }}
      >
        <div
          style={{
            ...cardStyle,
            backgroundColor: "#fff4e8",
          }}
        >
          <h3
            style={{
              color: "#5c3b28",
              marginBottom: "10px",
            }}
          >
            📂 Open Tickets
          </h3>

          <h1
            style={{
              color: "#2d1810",
              fontSize: "48px",
              margin: 0,
            }}
          >
            12
          </h1>
        </div>

        <div
          style={{
            ...cardStyle,
            backgroundColor: "#fff9eb",
          }}
        >
          <h3
            style={{
              color: "#5c3b28",
              marginBottom: "10px",
            }}
          >
            ⏳ Pending
          </h3>

          <h1
            style={{
              color: "#2d1810",
              fontSize: "48px",
              margin: 0,
            }}
          >
            5
          </h1>
        </div>

        <div
          style={{
            ...cardStyle,
            backgroundColor: "#eef8ee",
          }}
        >
          <h3
            style={{
              color: "#5c3b28",
              marginBottom: "10px",
            }}
          >
            ✅ Resolved
          </h3>

          <h1
            style={{
              color: "#2d1810",
              fontSize: "48px",
              margin: 0,
            }}
          >
            20
          </h1>
        </div>
      </div>

      <div
        style={{
          background: "white",
          padding: "25px",
          borderRadius: "20px",
          marginBottom: "25px",
          boxShadow: "0 5px 15px rgba(0,0,0,0.08)",
        }}
      >
        <h2
          style={{
            color: "#4a2c1a",
            marginBottom: "20px",
          }}
        >
          📋 Recent Tickets
        </h2>

        <div style={ticketStyle}>
          <span>📌 Password Reset Request</span>
          <span>🟠 Open</span>
        </div>

        <div style={ticketStyle}>
          <span>📌 Course Access Issue</span>
          <span>🟡 Pending</span>
        </div>

        <div style={ticketStyle}>
          <span>📌 LMS Login Problem</span>
          <span>🟢 Resolved</span>
        </div>
      </div>

      <Chatbot />
    </div>
  );
}

const buttonStyle = {
  padding: "12px 20px",
  border: "none",
  borderRadius: "10px",
  background: "linear-gradient(90deg, #d8b08c, #9a5d34)",
  color: "white",
  fontWeight: "bold",
  cursor: "pointer",
};

const cardStyle = {
  flex: 1,
  padding: "25px",
  borderRadius: "20px",
  textAlign: "center",
  boxShadow: "0 5px 15px rgba(0,0,0,0.08)",
};

const ticketStyle = {
  display: "flex",
  justifyContent: "space-between",
  padding: "15px 0",
  borderBottom: "1px solid #eee",
  color: "#4a2c1a",
  fontSize: "16px",
};

export default Dashboard;