// Sección 15. Pantalla para probar el middleware de CORS.
// La clase pide pegar este archivo en src/App.jsx del proyecto Vite.
// El botón llama a fetchData. El gist que se pegó primero dejaba la
// función vacía. La captura de la clase completa la llamada: pide
// GET http://127.0.0.1:8000/posts, que es la API de este repo.
// useState viene de React. Guarda el JSON de la API y, si falla, el texto del error.
import { useState } from "react";

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  // async porque adentro hay await: el navegador espera la respuesta de la API.
  const fetchData = async () => {
    // Limpia lo que haya quedado del clic anterior.
    setData(null);
    setError(null);

    try {
      // fetch es del navegador, no de React. Pide la lista de posts.
      // Si la API no manda la cabecera de CORS, el navegador corta acá
      // y el catch muestra el mensaje de abajo.
      const res = await fetch("http://127.0.0.1:8000/posts");
      // res.json() lee el cuerpo y lo convierte en objeto.
      const json = await res.json();
      setData(json);
    } catch (err) {
      // console.error deja el detalle en la consola del navegador.
      console.error(err);
      setError("Error de CORS o conexión. Revisa la consola del navegador.");
    }
  };

  return (
    <div style={{ fontFamily: "sans-serif", padding: 30 }}>
      <h1>Demo CORS con FastAPI</h1>
      <p>
        Este ejemplo intenta conectar con la API en <b>http://127.0.0.1:8000</b>
      </p>
      <button
        onClick={fetchData}
        style={{
          background: "#3182ce",
          color: "white",
          padding: "10px 20px",
          border: "none",
          borderRadius: 6,
          cursor: "pointer",
          fontSize: "16px",
        }}
      >
        Probar conexión
      </button>

      {data && (
        <pre
          style={{
            marginTop: 20,
            background: "#1a202c",
            color: "#f7fafc",
            padding: 15,
            borderRadius: 8,
          }}
        >
          {JSON.stringify(data, null, 2)}
        </pre>
      )}

      {error && (
        <pre
          style={{
            marginTop: 20,
            background: "#fed7d7",
            color: "#742a2a",
            padding: 15,
            borderRadius: 8,
          }}
        >
          {error}
        </pre>
      )}
    </div>
  );
}

export default App;
