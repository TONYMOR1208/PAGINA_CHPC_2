<template>
  <transition name="fade">
    <header v-bind:class="{ 'fade-in': isVisible }" class="header">
      <div class="main-header">
        <!-- Logo -->
        <div class="logo">
          <a href="/">
            <img src="@/images/logo/logo.png" alt="Logo de la página" />
          </a>
        </div>

        <!-- Barra de búsqueda -->
        <div class="search-bar">
          <input
            type="text"
            v-model="localSearchQuery"
            placeholder="Tenemos lo que usted está buscando"
            @input="buscarProductos"
            aria-label="Buscar productos"
          />
          <button @click="buscarProductos" aria-label="Buscar">
            <span class="search-icon">🔍</span>
          </button>
        </div>

        <!-- Acciones de usuario -->
        <div class="user-actions">
          <template v-if="!isAuthenticated">
            <button class="action-button" @click="goToLogin">Ingresar</button>
            <button class="action-button" @click="goToRegister">Hacerse cliente</button>
          </template>
          <template v-else>
            <button class="action-button" @click="cerrarSesion">Cerrar Sesión</button>
          </template>
        </div>
      </div>

      <!-- Menú de navegación -->
      <nav class="main-menu">
        <ul>
          <li><a href="/home">Inicio</a></li>
          <li><a href="/servicio-tecnico">Servicio Técnico</a></li>
          <li><a href="/redes-sociales">Redes Sociales</a></li>
          <li><a href="/marcas">Marcas</a></li>
        </ul>
      </nav>
    </header>
  </transition>
</template>

<script>
export default {
  name: "HeaderAnth",
  props: {
    searchQuery: {
      type: String,
      required: true,
    },
    isAuthenticated: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      localSearchQuery: this.searchQuery,
      isVisible: false, // Control de visibilidad para animación
    };
  },
  mounted() {
    // Iniciar la animación tras montar el componente
    setTimeout(() => {
      this.isVisible = true;
    }, 100);
  },
  methods: {
    buscarProductos() {
      this.$emit("buscar", this.localSearchQuery.trim());
    },
    cerrarSesion() {
      this.$emit("cerrar-sesion");
    },
    goToLogin() {
      this.$router.push("/login");
    },
    goToRegister() {
      this.$router.push("/registro");
    },
  },
};
</script>

<style scoped>
/* Header general */
.header {
  font-family: "Roboto", sans-serif;
  color: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Estilo para la sección principal */
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 30px;
}

.logo img {
  width: 120px;
  height: auto;
  border-radius: 5px;
}

/* Barra de búsqueda */
.search-bar {
  display: flex;
  flex: 1;
  margin: 0 20px;
}

.search-bar input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-right: none;
  border-radius: 5px 0 0 5px;
  outline: none;
  font-size: 16px;
}

.search-bar button {
  background-color: #ffa726; /* Naranja suave */
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.search-bar button:hover {
  background-color: #fb8c00; /* Naranja más oscuro */
  transform: scale(1.05);
}

/* Acciones del usuario */
.user-actions {
  display: flex;
  gap: 10px;
}

.action-button {
  background-color: #ffa726; /* Naranja suave */
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s;
}

.action-button:hover {
  background-color: #fb8c00; /* Naranja más oscuro */
  transform: scale(1.05);
}

/* Menú de navegación */
.main-menu {
  background: linear-gradient(135deg, #000, #333); /* Gradiente negro */
  padding: 10px 0;
}

.main-menu ul {
  display: flex;
  justify-content: space-around;
  margin: 0;
  padding: 0;
  list-style: none;
}

.main-menu a {
  color: #ffa726; /* Naranja suave */
  text-decoration: none;
  font-size: 16px;
  font-weight: bold;
  transition: color 0.3s ease;
}

.main-menu a:hover {
  color: white; /* Cambio a blanco en hover */
}

/* Animaciones */
.fade-in {
  animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(-10%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Transiciones para los componentes */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active en <2.1.8 */ {
  opacity: 0;
}
</style>
