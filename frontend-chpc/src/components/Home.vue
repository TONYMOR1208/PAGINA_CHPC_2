<template>
  <div>
    <header class="header">
      <div class="main-header">
  <div class="logo">
    <img src="@/images/logo/logo.png" alt="Logo de la página" />
  </div>


        <div class="search-bar">
          <input
            type="text"
            v-model="searchQuery"
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
          <li><a href="#">Software</a></li>
          <li><a href="#">Redes</a></li>
          <li><a href="#">Electrónica</a></li>
          <li><a href="#">Movilidad</a></li>
          <li><a href="#">Oficina</a></li>
          <li><a href="#">Accesorios</a></li>
          <li><a href="#">Seguridad</a></li>
          <li><a href="#">Gaming</a></li>
          <li><a href="#">Cloud</a></li>
          <li><a href="#">POS</a></li>
          <li><a href="#">Marcas</a></li>
          <li><a href="#">Ofertas & Más</a></li>
        </ul>
      </nav>
    </header>

    <!-- Carrusel de Banners -->
    <div v-if="banners.length > 0" class="carousel">
      <div
        v-for="(banner, index) in banners"
        :key="banner.id"
        :class="['carousel-item', { active: index === activeBanner }]"
      >
        <img
          :src="getFullImageUrl(banner.imagen_url)"
          :alt="banner.titulo"
          class="banner-image"
        />
      </div>
      <div class="carousel-indicators">
        <span
          v-for="(banner, index) in banners"
          :key="`indicator-${index}`"
          :class="{ active: index === activeBanner }"
          @click="activeBanner = index"
        ></span>
      </div>
    </div>

    <!-- Contenido principal -->
    <div class="home-container">
      <h1>Bienvenidos a Nuestra Tienda</h1>
      <p>Explora nuestros productos y encuentra lo que necesitas.</p>
      <div class="product-grid">
        <div
          v-for="producto in productosMostrados"
          :key="producto.id"
          class="product-card"
        >
          <img
            :src="producto.imagen_url || 'ruta-imagen-default.png'"
            alt="Imagen del Producto"
          />
          <h3>{{ producto.nombre_producto }}</h3>
          <p>{{ producto.descripcion }}</p>
          <p v-if="isAuthenticated">
            <strong>Precio:</strong> ${{ producto.precio }}
          </p>
          <button v-if="isAuthenticated" @click="verDetalle(producto.id)">
            Ver Detalles
          </button>
          <button v-else @click="redirigirLogin">
            Inicia Sesión para Ver Precios
          </button>
        </div>
      </div>

      <!-- Botón para cargar más productos -->
      <button
        v-if="productosMostrados.length < productos.length"
        @click="cargarMasProductos"
        class="cargar-mas"
      >
        Cargar más productos
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomePage",
  data() {
    return {
      banners: [],
      activeBanner: 0,
      productos: [],
      productosMostrados: [],
      searchQuery: "",
      isAuthenticated: false,
      limiteProductos: 10,
      intervalId: null, // Intervalo para cambiar el banner automáticamente
    };
  },
  async created() {
    this.isAuthenticated = !!localStorage.getItem("access_token");

    try {
      const bannersResponse = await axios.get(
        "http://localhost:5000/tienda/banners"
      );
      this.banners = bannersResponse.data.data;
    } catch (error) {
      console.error("Error al cargar los banners:", error);
    }

    try {
      const productosResponse = await axios.get(
        "http://localhost:5000/tienda/productos"
      );
      this.productos = productosResponse.data.map((producto) => ({
        ...producto,
        imagen_url:
          producto.media?.length > 0
            ? `http://localhost:5000${producto.media[0].url}`
            : "ruta-imagen-default.png",
      }));
      this.cargarMasProductos();
    } catch (error) {
      console.error("Error al cargar los productos:", error);
    }

    // Configurar cambio automático de banners
    this.startCarousel();
  },
  beforeUnmount() { // Cambio de beforeDestroy a beforeUnmount
    // Limpiar el intervalo al desmontar el componente
    this.stopCarousel();
  },
  methods: {
    startCarousel() {
      this.intervalId = setInterval(() => {
        this.activeBanner =
          (this.activeBanner + 1) % this.banners.length;
      }, 4000); // Cambiar cada 4 segundos
    },
    stopCarousel() {
      if (this.intervalId) clearInterval(this.intervalId);
    },
    cargarMasProductos() {
      const siguienteBloque = this.productos.slice(
        this.productosMostrados.length,
        this.productosMostrados.length + this.limiteProductos
      );
      this.productosMostrados = [...this.productosMostrados, ...siguienteBloque];
    },
    getFullImageUrl(relativeUrl) {
      return `http://localhost:5000${relativeUrl}`;
    },
    verDetalle(id) {
      this.$router.push({ name: "ProductoDetalle", params: { id } });
    },
    buscarProductos() {
      if (this.searchQuery.trim() !== "") {
        this.productosMostrados = this.productos.filter((producto) =>
          producto.nombre_producto
            .toLowerCase()
            .includes(this.searchQuery.toLowerCase())
        );
      }
    },
    cerrarSesion() {
      localStorage.removeItem("access_token");
      this.isAuthenticated = false;
      this.$router.replace("/login");
    },
    redirigirLogin() {
      this.$router.push("/login");
    },
  },
};
</script>


<style >
/* Estilos del fondo principal */
body {
  background-color:f5f5f1; /* Fondo gris claro */
  margin: 0;
  padding: 0;
}




/* Estilos del header */
/* Estilos generales del header */
.header {
  font-family: Arial, sans-serif;
}

/* Barra superior */
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f5f5f5;
  padding: 5px 20px;
  font-size: 14px;
  color: #333;
}

.language-selector span {
  font-weight: bold;
}

.top-links a {
  margin-left: 15px;
  text-decoration: none;
  color: #333;
}

.top-links a:hover {
  text-decoration: underline;
}

/* Header principal */
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #0053a0;
  padding: 10px 20px;
}

.logo img {
  height: 50px;
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

.search-bar button:hover {
  background-color: #ff9900;
}

.user-actions a,
.user-actions button {
  margin-left: 15px;
  text-decoration: none;
  color: white;
  font-weight: bold;
  background-color: transparent;
  border: none;
  cursor: pointer;
}

.user-actions a:hover,
.user-actions button:hover {
  text-decoration: underline;
}

/* Menú principal */
.main-menu {
  background-color: #003366;
}

.main-menu ul {
  display: flex;
  justify-content: space-between;
  list-style: none;
  padding: 0;
  margin: 0;
}

.main-menu li {
  flex: 1;
  text-align: center;
}

.main-menu a {
  display: block;
  padding: 10px 0;
  color: white;
  text-decoration: none;
  font-size: 14px;
  font-weight: bold;
}

.main-menu a:hover {
  background-color: #ff8c00;
}
.logo img {
  width: 100px;
  height: 100px;
}


.search-bar input {
  padding: 8px;
  border: none;
  border-radius: 5px 0 0 5px;
  width: 150px; /* Ajusta este valor para hacerlo más corto */
}

.search-bar button {
  padding: 12px 14px; /* Reduce el padding horizontal para acortar el botón */
  border: none;
  background-color: #ff9900;
  color: white;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
}


.user-actions a,
.user-actions button {
  margin-left: 15px;
  color: #ff9900;
  text-decoration: none;
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* Máximo 4 columnas por fila */
  gap: 20px;
}

@media (max-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .product-grid {
    grid-template-columns: repeat(1, 1fr);
  }
}

.cargar-mas {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background-color: #ff9900;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.search-bar button:hover:enabled {
  background-color: #ff8c00;
}

.user-actions a:hover,
.user-actions button:hover {
  text-decoration: underline;
}

/* Estilos del contenido principal */
.home-container {
  text-align: center;
  margin: 30px;
}

/* Mantener los contenedores de productos en blanco */
.product-card {
  background-color: #ffffff; /* Fondo blanco */
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}
.product-card img {
  width: 180px; /* Ancho fijo */
  height: 180px; /* Alto fijo */
  object-fit: cover; /* Ajusta la imagen */
  border-radius: 8px; /* Esquinas redondeadas */
  margin: 0 auto; /* Centra la imagen */
  display: block; /* Centrado */
}

.product-card h3 {
  font-size: 18px;
  margin: 10px 0;
}

.product-card p {
  font-size: 14px;
  color: #333;
}

.product-card button {
  padding: 10px 20px;
  background-color: #ff9900;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.product-card button:hover {
  background-color: #ff8c00;
}

/* Botón de carga progresiva */
.cargar-mas:hover {
  background-color: #ff8c00;
}

/* Estilos del carrusel */
.carousel {
  position: relative;
  width: 851px;
  height: 315px;
  margin: 20px auto;
  overflow: hidden;
  border-radius: 8px;
}

.carousel-item {
  display: none;
  position: absolute;
  width: 100%;
  height: 100%;
  transition: opacity 0.5s ease-in-out;
}

.carousel-item.active {
  display: block;
  opacity: 1;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 5px;
}

.carousel-indicators span {
  width: 10px;
  height: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  cursor: pointer;
}

.carousel-indicators .active {
  background-color: #fff;
}
</style>
