<template>
  <div>
    <HeaderAnth
      :isAuthenticated="isAuthenticated"
      @cerrar-sesion="cerrarSesion"
    />

    <!-- Transición para el contenedor de marcas -->
    <transition name="fade">
      <div class="marcas-container">
        <h1 class="main-title">Explora nuestras Marcas</h1>
        <p class="description">
          Aquí encontrarás las mejores marcas para tus necesidades. ¡Haz clic y conoce más!
        </p>
        <div class="marca-grid">
          <div 
            v-for="marca in marcas" 
            :key="marca.id" 
            class="marca-card"
            @click="filtrarPorMarca(marca.id)"
          >
            <img
              :src="marca.imagen_url"
              :alt="'Logo de la marca ' + marca.nombre_marca"
              class="marca-logo"
            />
            <h3>{{ marca.nombre_marca }}</h3>
          </div>
        </div>
      </div>
    </transition>

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
          : "http://localhost:5000/static/logosmarcas/default.png",
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
    filtrarPorMarca(marcaId) {
      this.$router.push({ name: "ProductosPorMarca", params: { id: marcaId } });
    },
  },
};
</script>

<style>
body {
  background-color: #f5f5f5; /* Gris claro */
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif; /* Tipografía uniforme */
}

.marcas-container {
  text-align: center;
  margin: 40px auto;
  max-width: 1200px;
  opacity: 0; /* Oculto inicialmente */
  transform: translateY(20px); /* Mover hacia abajo inicialmente */
  animation: fadeIn 1s ease-out forwards; /* Animación */
}

.main-title {
  font-size: 32px;
  color: #333; /* Color de texto principal */
  margin-bottom: 10px;
}

.description {
  font-size: 18px;
  color: #555; /* Color de texto secundario */
  margin-bottom: 30px;
}

.marca-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 30px;
  padding: 0 20px;
}

@media (max-width: 768px) {
  .marca-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .marca-grid {
    grid-template-columns: 1fr;
  }
}

.marca-card {
  background-color: #ffffff; /* Fondo blanco */
  border: 1px solid #ddd; /* Tonalidad gris suave */
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.marca-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.marca-logo {
  width: 150px;
  height: 150px;
  object-fit: contain;
  border-radius: 10px;
  margin: 10px auto 15px;
}

.marca-card h3 {
  font-size: 18px;
  color: #333; /* Color de texto principal */
  margin: 10px 0;
  text-transform: capitalize;
}

/* Transición de entrada/salida */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Animación personalizada */
@keyframes fadeIn {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
