import { useNavigate } from "react-router-dom";

function Login() {
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
          width: "450px",
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
            marginBottom: "15px",
          }}
        >
          🎧
        </div>

        <h1
          style={{
            color: "#5c3b28",
            marginBottom: "10px",
            fontSize: "48px",
          }}
        >
          Helpdesk Portal
        </h1>

        <p
          style={{
            color: "#777",
            marginBottom: "30px",
            fontSize: "18px",
          }}
        >
          Automated Helpdesk Reasoner for CFAI
        </p>

        <input
          type="email"
          placeholder="📧 Email Address"
          style={{
            width: "100%",
            padding: "15px",
            borderRadius: "12px",
            border: "2px solid #e6d8c7",
            marginBottom: "18px",
            fontSize: "16px",
            boxSizing: "border-box",
          }}
        />

        <input
          type="password"
          placeholder="🔒 Password"
          style={{
            width: "100%",
            padding: "15px",
            borderRadius: "12px",
            border: "2px solid #e6d8c7",
            marginBottom: "22px",
            fontSize: "16px",
            boxSizing: "border-box",
          }}
        />

        <button
          onClick={() => navigate("/dashboard")}
          style={{
            width: "100%",
            padding: "15px",
            border: "none",
            borderRadius: "12px",
            background: "linear-gradient(90deg, #d8b08c, #9a5d34)",
            color: "white",
            fontSize: "18px",
            fontWeight: "bold",
            cursor: "pointer",
          }}
        >
          Login →
        </button>

        <p
          onClick={() => navigate("/signup")}
          style={{
            marginTop: "25px",
            color: "#5c3b28",
            cursor: "pointer",
            fontWeight: "bold",
          }}
        >
          New here? Create an account →
        </p>
      </div>
    </div>
  );
}

export default Login;