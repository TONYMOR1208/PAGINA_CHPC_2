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
        />
        <button @click="buscarProductos">Buscar</button>
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
        <li><a href="#">Computo</a></li>
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
    };
  },
  watch: {
    searchQuery(newValue) {
      this.localSearchQuery = newValue;
    },
  },
  methods: {
    buscarProductos() {
      this.$emit("buscar", this.localSearchQuery);
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
  font-family: Arial, sans-serif;
}

.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #FFFFFF;
  padding: 10px 20px;
}

.logo img {
  width: 100px;
  height: 70px;
  object-fit: cover;
  border-radius: 5px;
}

.search-bar input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px 0 0 5px;
}

.search-bar button {
  padding: 10px 20px;
  background-color: #ff8c00;
  border: none;
  color: white;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
}
</style>
