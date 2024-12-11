<template>
    <div>
      <HeaderAnth
        :isAuthenticated="isAuthenticated"
        @cerrar-sesion="cerrarSesion"
      />
  
      <div class="marcas-container">
        <h1>Marcas Disponibles</h1>
        <div class="marca-grid">
          <div v-for="marca in marcas" :key="marca.id" class="marca-card">
            <img
              :src="marca.imagen_url"
              alt="Logo de la Marca"
              class="marca-logo"
            />
            <h3>{{ marca.nombre_marca }}</h3>
          </div>
        </div>
      </div>
  
      <FooterAnth />
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import HeaderAnth from "@/components/HeaderAnth.vue";
  import FooterAnth from "@/components/FooterAnth.vue";
  
  export default {
    name: "ListaMarcas",
    components: {
      HeaderAnth,
      FooterAnth,
    },
    data() {
      return {
        marcas: [],
        isAuthenticated: false,
      };
    },
    async created() {
      this.isAuthenticated = !!localStorage.getItem("access_token");
  
      try {
        const response = await axios.get("http://localhost:5000/tienda/marcas/");
        this.marcas = response.data.map((marca) => ({
          ...marca,
          imagen_url: marca.imagen_url
            ? `http://localhost:5000${marca.imagen_url}`
            : "http://localhost:5000/static/logosmarcas/default.png", // Ruta por defecto si no hay imagen
        }));
      } catch (error) {
        console.error("Error al cargar las marcas:", error);
      }
    },
    methods: {
      cerrarSesion() {
        localStorage.removeItem("access_token");
        this.isAuthenticated = false;
        this.$router.replace("/login");
      },
    },
  };
  </script>
  
  <style>
  body {
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
  }
  
  .marcas-container {
    text-align: center;
    margin: 30px;
  }
  
  .marca-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* Máximo 4 columnas por fila */
    gap: 20px;
  }
  
  @media (max-width: 768px) {
    .marca-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 480px) {
    .marca-grid {
      grid-template-columns: repeat(1, 1fr);
    }
  }
  
  .marca-card {
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
  }
  
  .marca-card:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  }
  
  .marca-logo {
    width: 180px;
    height: 180px;
    object-fit: cover;
    border-radius: 8px;
    margin: 0 auto;
    display: block;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .marca-card:hover .marca-logo {
    transform: scale(1.1);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  }
  
  .marca-card h3 {
    font-size: 18px;
    margin: 10px 0;
  }
  </style>
  