import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
// La plantilla de la clase usa este plugin (Babel). Hace falta Node 20.19+ o 22.
// En esta máquina el `node` del PATH es 20.6.0 y Babel falla con
// "Cannot redefine property: File". .nvmrc apunta a 22.17.1, que ya está
// instalado con nvm: desde cors-demo, `nvm use` y después `npm run dev`.
// La clase abre http://localhost:3000. Vite, si no se le dice el puerto,
// levanta en 5173. strictPort hace que falle si el 3000 ya está ocupado,
// en vez de saltar a otro puerto sin avisar.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    strictPort: true,
  },
})
