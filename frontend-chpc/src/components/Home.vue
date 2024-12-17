//CODIGO CORTECIA DE:ANTHONY JOEL MOREIRAA CATAGUA Y CHATGPT GOD

<template>
  <div>
    <!-- Encabezado -->
    <HeaderAnth
      :searchQuery="searchQuery"
      :isAuthenticated="isAuthenticated"
      @buscar="buscarProductos"
      @cerrar-sesion="cerrarSesion"
    />



    <!-- Contenido principal -->
    <div class="home-container">
          <!-- Carrusel de Banners -->
    <div>
      <CarouselBanner :banners="banners" />
    </div>
      <h1>Bienvenidos a Nuestra Tienda </h1>
      <p>Explora nuestros productos y encuentra lo que necesitas.</p>

     <!-- Lista de Productos -->
<div class="product-grid">
  <div
    v-for="producto in productosMostrados"
    :key="producto.id"
    class="product-card"
  >
    <!-- Imagen del producto -->
    <img
      :src="producto.imagen_url || 'ruta-imagen-default.png'"
      alt="Imagen del Producto"
    />

    <!-- Nombre y descripción del producto -->
    <h3>{{ producto.nombre_producto }}</h3>
    <p>{{ producto.descripcion }}</p>

    <!-- Precio del producto (solo para usuarios autenticados) -->
    <p v-if="isAuthenticated">
      <strong>Precio:</strong> ${{ producto.precio }}
    </p>

    <!-- Mostrar cantidad en stock -->
    <p>
      <strong>Stock disponible:</strong> {{ producto.stock }} unidades
    </p>

    <!-- Botones de acción -->
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
        v-if="productosMostrados.length < productos.length && searchQuery.trim() === ''"
        @click="cargarMasProductos"
        class="cargar-mas"
      >
        Cargar más productos
      </button>

      <!-- Mensaje de No Resultados -->
      <div v-if="productosMostrados.length === 0 && searchQuery.trim() !== ''">
        <p>No se encontraron productos que coincidan con "{{ searchQuery }}".</p>
      </div>
    </div>

    <!-- Pie de página -->
    <FooterAnth />
  </div>
</template>

<script>
import axios from "axios";
import HeaderAnth from "@/components/HeaderAnth.vue";
import FooterAnth from "@/components/FooterAnth.vue";
import CarouselBanner from "@/components/CarouselBanner.vue";

export default {
  name: "HomePage",
  components: {
    HeaderAnth,
    CarouselBanner,
    FooterAnth,
  },
  data() {
    return {
      banners: [],
      productos: [],
      productosMostrados: [],
      searchQuery: "",
      isAuthenticated: false,
      limiteProductos: 10,
    };
  },
  async created() {
    this.isAuthenticated = !!localStorage.getItem("access_token");

    try {
      // Cargar Banners
      const bannersResponse = await axios.get("http://localhost:5000/tienda/banners");
      this.banners = bannersResponse.data.data;

      // Cargar Productos
      const productosResponse = await axios.get("http://localhost:5000/tienda/productos");
      this.productos = productosResponse.data.map((producto) => ({
        ...producto,
        imagen_url:
          producto.media?.length > 0
            ? `http://localhost:5000${producto.media[0].url}`
            : "ruta-imagen-default.png",
      }));
      this.cargarMasProductos();
    } catch (error) {
      console.error("Error al cargar los datos:", error);
    }

    // Procesar la búsqueda inicial (si existe)
    const search = this.$route.query.search;
    if (search) {
      this.buscarProductos(search);
    }
  },
  methods: {
    cargarMasProductos() {
      if (this.searchQuery.trim() !== "") return;

      const siguienteBloque = this.productos.slice(
        this.productosMostrados.length,
        this.productosMostrados.length + this.limiteProductos
      );

      this.productosMostrados = [...this.productosMostrados, ...siguienteBloque];
    },
    verDetalle(id) {
      this.$router.push({ name: "ProductoDetalle", params: { id } });
    },
    buscarProductos(query) {
      this.searchQuery = query.trim();
      if (this.searchQuery !== "") {
        this.productosMostrados = this.productos.filter(
          (producto) =>
            producto.nombre_producto
              .toLowerCase()
              .includes(this.searchQuery.toLowerCase()) ||
            producto.descripcion
              .toLowerCase()
              .includes(this.searchQuery.toLowerCase())
        );
      } else {
        this.productosMostrados = this.productos.slice(0, this.limiteProductos);
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

<style>
/* Estilos del fondo principal */
body {
  background-color: #f5f5f5; /* Fondo gris claro */
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif; /* Tipografía uniforme */
  color: #333; /* Color de texto predeterminado */
}

/* Contenido principal */
.home-container {
  text-align: center;
  margin: 30px;
  animation: fadeInUp 1s ease-in-out;
}

/* Animación para el contenedor principal */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* Máximo 4 columnas por fila */
  gap: 20px;
  animation: slideIn 1s ease-in-out;
}

/* Animación para la cuadrícula de productos */
@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
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

/* Estilos de las tarjetas de producto con animación */
.product-card {
  background-color: #ffffff; /* Fondo blanco */
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  animation: fadeIn 0.5s ease-in-out;
}

/* Animación para cada tarjeta de producto */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.product-card:hover {
  transform: scale(1.05); /* Aumenta el tamaño */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.product-card img {
  width: 180px; /* Ancho fijo */
  height: 180px; /* Alto fijo */
  object-fit: cover; /* Ajusta la imagen */
  border-radius: 8px; /* Esquinas redondeadas */
  margin: 0 auto; /* Centra la imagen */
  display: block; /* Centrado */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover img {
  transform: scale(1.1); /* Aumenta ligeramente la imagen */
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3); /* Sombra más grande */
}

.product-card h3 {
  font-size: 18px;
  margin: 10px 0;
  color: #333; /* Color de texto uniforme */
}

.product-card p {
  font-size: 14px;
  color: #666; /* Tonalidad más suave */
}

.product-card button {
  padding: 10px 20px;
  background-color: #ffa726; /* Naranja suave */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.product-card button:hover {
  background-color: #fb8c00; /* Tonalidad más oscura */
  transform: translateY(-3px);
}

/* Botón de carga progresiva */
.cargar-mas {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  font-size: 16px;
  color: white;
  background-color: #ffa726;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.cargar-mas:hover {
  background-color: #fb8c00;
}
</style>
