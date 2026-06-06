import { useNavigate } from "react-router-dom";

function Signup() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",

        backgroundColor: "#f7f1e8",

        backgroundImage: `
          linear-gradient(45deg, #f3ece2 25%, transparent 25%),
          linear-gradient(-45deg, #f3ece2 25%, transparent 25%),
          linear-gradient(45deg, transparent 75%, #f3ece2 75%),
          linear-gradient(-45deg, transparent 75%, #f3ece2 75%)
        `,
        backgroundSize: "60px 60px",
        backgroundPosition: "0 0, 0 30px, 30px -30px, -30px 0px",
      }}
    >
      <div
        style={{
          width: "500px",
          backgroundColor: "rgba(255,255,255,0.95)",
          padding: "45px",
          borderRadius: "25px",
          textAlign: "center",
          boxShadow: "0 15px 35px rgba(0,0,0,0.1)",
        }}
      >
        <div
          style={{
            fontSize: "45px",
            marginBottom: "10px",
          }}
        >
          ✨
        </div>

        <h1
          style={{
            color: "#5c3b28",
            fontSize: "46px",
            marginBottom: "10px",
          }}
        >
          Create Account
        </h1>

        <p
          style={{
            color: "#777",
            marginBottom: "30px",
          }}
        >
          Join the CFAI Helpdesk Portal
        </p>

        <input
          type="text"
          placeholder="👤 Full Name"
          style={inputStyle}
        />

        <input
          type="email"
          placeholder="📧 Email Address"
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="🔒 Password"
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="🔐 Confirm Password"
          style={inputStyle}
        />

        <button
          style={buttonStyle}
          onClick={() => navigate("/dashboard")}
        >
          Create Account →
        </button>

        <p
          onClick={() => navigate("/")}
          style={{
            marginTop: "20px",
            color: "#5c3b28",
            cursor: "pointer",
            fontWeight: "bold",
          }}
        >
          Already have an account? Login →
        </p>
      </div>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "15px",
  marginBottom: "15px",
  borderRadius: "12px",
  border: "2px solid #e6d8c7",
  fontSize: "16px",
  boxSizing: "border-box",
};

const buttonStyle = {
  width: "100%",
  padding: "15px",
  border: "none",
  borderRadius: "12px",
  background: "linear-gradient(90deg, #d8b08c, #9a5d34)",
  color: "white",
  fontSize: "18px",
  fontWeight: "bold",
  cursor: "pointer",
};

export default Signup;