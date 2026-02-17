import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [idea, setIdea] = useState("");
  const [loading, setLoading] = useState(false);
  const [architecture, setArchitecture] = useState(null);
  const [error, setError] = useState("");

  const generateArchitecture = async () => {
  if (!idea.trim()) {
    setError("Please enter your app idea");
    return;
  }

  setLoading(true);
  setError("");
  setArchitecture(null);

  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/generate-architecture",
      {
        app_description: idea,
        api_key: ""
      }
    );

    setArchitecture(response.data);

  } catch (err) {
    console.error(err);
    setError("Failed to generate architecture. Make sure backend is running.");
  }

  setLoading(false);
};


  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>AI System Architecture Generator 🚀</h1>

        <textarea
          placeholder="Example: Build a food delivery app"
          value={idea}
          onChange={(e) => setIdea(e.target.value)}
          style={styles.textarea}
        />

        <button
          onClick={generateArchitecture}
          style={styles.button}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Architecture"}
        </button>

        {error && <p style={styles.error}>{error}</p>}

        {architecture && (
          <div style={styles.result}>
            <h2>Architecture Overview</h2>

            <p><strong>Frontend:</strong> {architecture.frontend}</p>
            <p><strong>Backend:</strong> {architecture.backend}</p>
            <p><strong>Database:</strong> {architecture.database}</p>
            <p><strong>Cache:</strong> {architecture.cache}</p>
            <p><strong>Queue:</strong> {architecture.queue}</p>

            <h3>Explanation</h3>
            <p>{architecture.explanation}</p>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    backgroundColor: "#0f172a",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    color: "white",
  },
  card: {
    backgroundColor: "#1e293b",
    padding: "30px",
    borderRadius: "12px",
    width: "600px",
    boxShadow: "0 0 20px rgba(0,0,0,0.5)",
  },
  title: {
    marginBottom: "20px",
  },
  textarea: {
    width: "100%",
    height: "100px",
    padding: "10px",
    borderRadius: "8px",
    border: "none",
    marginBottom: "15px",
  },
  button: {
    width: "100%",
    padding: "12px",
    borderRadius: "8px",
    border: "none",
    backgroundColor: "#3b82f6",
    color: "white",
    fontSize: "16px",
    cursor: "pointer",
  },
  result: {
    marginTop: "20px",
    backgroundColor: "#0f172a",
    padding: "15px",
    borderRadius: "8px",
  },
  error: {
    color: "red",
    marginTop: "10px",
  },
};

export default App;
