<template>
  <header class="header">
    <div class="main-header">
      <div class="logo">
        <a href="/">
          <img src="@/images/logo/logo.png" alt="Logo de la página" />
        </a>
      </div>

      <div class="search-bar">
        <input
          type="text"
          v-model="localSearchQuery"
          placeholder="Tenemos lo que usted está buscando"
          @input="buscarProductos"
          aria-label="Campo de búsqueda"
        />
        <button @click="buscarProductos" aria-label="Botón para buscar productos">
          Buscar
        </button>
      </div>
      <div class="user-actions">
        <template v-if="!isAuthenticated">
          <a href="/login">Ingresar</a>
          <a href="/registro">Hacerse cliente</a>
        </template>
        <template v-else>
          <button @click="cerrarSesion">Cerrar Sesión</button>
        </template>
      </div>
    </div>
    <nav class="main-menu">
      <ul>
        <li><a href="/home">Inicio</a></li>
        <li><a href="/servicio-tecnico">Servicio Tecnico</a></li>
        <li><a href="/redes-sociales">Redes Sociales</a></li>
        <li><a href="/marcas">Marcas</a></li>
      </ul>
    </nav>
  </header>
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
      delayTimer: null, // Temporizador para manejar debounce
    };
  },
  watch: {
    searchQuery(newValue) {
      this.localSearchQuery = newValue;
    },
  },
  methods: {
    buscarProductos() {
      clearTimeout(this.delayTimer); // Reinicia el temporizador
      this.delayTimer = setTimeout(() => {
        const query = this.localSearchQuery.trim();
        // Emitir búsqueda al padre si la barra no está vacía o vaciar la búsqueda
        this.$emit("buscar", query || "");
      }, 300); // Espera 300ms para optimizar búsquedas
    },
    cerrarSesion() {
      this.$emit("cerrar-sesion");
    },
  },
};
</script>


<style scoped>
/* Estilos relacionados con el header */
.header {
  font-family: 'Roboto', sans-serif;
}

.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #ffff; /* Negro en lugar de blanco */
  padding: 10px 20px;
}

.logo img {
  width: 100px;
  height: 70px;
  object-fit: cover;
  border-radius: 5px;
}

.search-bar {
  flex: 1;
  display: flex;
  align-items: center;
  margin: 0 20px;
}

.search-bar input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd; /* Tonalidad gris suave */
  border-radius: 5px 0 0 5px;
}

.search-bar button {
  padding: 10px 20px;
  background-color: #ffa726; /* Naranja suave */
  border: none;
  color: white;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  transition: background 0.3s ease;
}

.search-bar button:hover {
  background-color: #fb8c00; /* Tonalidad más oscura */
}

</style>
