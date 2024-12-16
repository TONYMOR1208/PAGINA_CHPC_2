<template>
  <HeaderAnth
    :searchQuery="searchQuery"
    :isAuthenticated="isAuthenticated"
    @buscar="buscarProductos"
    @cerrar-sesion="cerrarSesion"
  />
  <br />
  <br />
  <br />

  <div class="producto-contenedor">
    <!-- Mensaje de carga -->
    <div v-if="isLoading" class="mensaje-carga">
      <p>Cargando detalles del producto...</p>
    </div>

    <!-- Mensaje de error con botón de recarga -->
    <div v-if="errorMessage && !isLoading" class="mensaje-error">
      <p>{{ errorMessage }}</p>
      <button @click="recargarProducto" class="boton-recargar">Reintentar</button>
    </div>

    <!-- Mensaje de no autenticado -->
    <div v-if="!isAuthenticated" class="mensaje-error">
      <p>Por favor, inicie sesión para ver los detalles del producto.</p>
      <button @click="redirigirLogin" class="boton-recargar">Iniciar sesión</button>
    </div>

<!-- Detalles del producto -->
<div
  v-if="producto && !isLoading && !errorMessage && isAuthenticated"
  class="producto-contenedor"
>
  <h2 class="seccion-titulo">Detalles del Producto</h2> <!-- Título de la sección -->
  <div class="detalle-contenedor">
    <!-- Galería de medios del producto -->
    <div class="galeria-imagenes">
      <div class="miniaturas">
        <template v-for="(media, index) in producto.media || []" :key="index">
          <img
            v-if="media.tipo_media === 'imagen'"
            :src="getFullImageUrl(media.url)"
            :alt="`Imagen adicional ${index + 1}`"
            class="imagen-miniatura"
            @click="cambiarImagenPrincipal(index)"
          />
          <div
            v-else-if="media.tipo_media === 'video'"
            class="video-miniatura-wrapper"
            @click="cambiarImagenPrincipal(index)"
          >
            <video
              class="video-miniatura"
              :src="getFullImageUrl(media.url)"
              muted
              loop
            ></video>
          </div>
        </template>
      </div>
      <div class="imagen-principal">
        <!-- Imagen principal -->
        <img
          v-if="producto.media?.[imagenSeleccionada]?.tipo_media === 'imagen'"
          :src="getFullImageUrl(producto.media?.[imagenSeleccionada]?.url || '')"
          :alt="`Imagen principal de ${producto.nombre_producto || ''}`"
          class="imagen-grande"
        />
        <!-- Video principal -->
        <video
          v-else-if="producto.media?.[imagenSeleccionada]?.tipo_media === 'video'"
          class="video-grande"
          :src="getFullImageUrl(producto.media?.[imagenSeleccionada]?.url || '')"
          controls
          autoplay
        ></video>
      </div>
    </div>

    <!-- Información del producto -->
    <div class="informacion-producto">
      <h1 class="nombre-producto">{{ producto.nombre_producto }}</h1>

      <!-- Precio con descuento y original -->
      <div class="precio-contenedor">
        <span class="precio-descuento">USD ${{ formatPrice(producto.precio) }}</span>
        <span class="precio-original" v-if="producto.precio_original">
          USD ${{ formatPrice(producto.precio_original) }}
        </span>
      </div>

      <!-- Estado del stock -->
      <p class="stock-producto">
        {{ producto.stock > 0 ? "En stock" : "Agotado" }}
      </p>

      <!-- Descripción en formato de lista -->
      <div class="descripcion-producto">
        <p><strong>Descripción:</strong></p>
        <ul>
          <li><strong>Nombre del Producto:</strong> {{ producto.nombre_producto || 'Sin nombre' }}</li>
          <li v-if="producto.descripcion"><strong>Descripción del Producto:</strong> {{ producto.descripcion }}</li>
          <li><strong>Precio:</strong> USD ${{ formatPrice(producto.precio) }}</li>
          <li><strong>Stock:</strong> {{ producto.stock > 0 ? 'Disponible' : 'Agotado' }}</li>
          <li v-if="producto.peso"><strong>Peso:</strong> {{ producto.peso }} kg</li>
          <li v-if="producto.color"><strong>Color:</strong> {{ producto.color }}</li>
          <li v-if="producto.volumen"><strong>Volumen:</strong> {{ producto.volumen }} ml</li>

          <li><strong>Marca:</strong> {{ producto.marca?.nombre_marca || 'Sin marca' }}</li>
          <li v-if="producto.marca?.descripcion"><strong>Descripción de la Marca:</strong> {{ producto.marca.descripcion }}</li>
          <li v-if="producto.marca?.sitio_web"><strong>Sitio Web de la Marca:</strong> <a :href="producto.marca.sitio_web" target="_blank">{{ producto.marca.sitio_web }}</a></li>

          <li><strong>Categoría:</strong> {{ producto.categoria?.nombre_categoria || 'Sin categoría' }}</li>
        </ul>
      </div>

      <div class="botones-accion">
  <a href="https://wa.me/593995924867" target="_blank" class="boton-compra">Comprar ahora</a>
 
</div>

    </div>
  </div>
</div>
</div>

  <br>
  <br>
  <br>
  <br>

  <FooterAnth />
</template>



<script>
import axios from "axios";
import HeaderAnth from "@/components/HeaderAnth.vue";
import FooterAnth from "@/components/FooterAnth.vue";

export default {
  name: "ProductoDetalle",
  components: {
    HeaderAnth,
    FooterAnth,
  },
  data() {
    return {
      producto: {
        media: [], // Lista de medios del producto (imágenes y videos)
        categoria: {}, // Información de la categoría del producto
        marca: {}, // Información de la marca del producto
      },
      errorMessage: "",
      isLoading: true,
      isAuthenticated: false,
      imagenSeleccionada: 0, // Índice del medio seleccionado
      searchQuery: "",
    };
  },
  methods: {
    async cargarProducto() {
      if (!this.isAuthenticated) {
        return;
      }

      this.isLoading = true;
      this.errorMessage = "";

      const productoId = this.$route.params.id;
      try {
        // Obtener los datos del producto
        const response = await axios.get(
          `http://localhost:5000/tienda/productos/${productoId}`,
          { headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } }
        );
        this.producto = response.data;

        // Validar que todos los medios tengan el campo `tipo_media`
        this.producto.media = this.producto.media.map((media) => ({
          ...media,
          tipo_media: media.tipo_media || "imagen", // Predeterminar como "imagen" si no está definido
        }));

        // Llamar a los endpoints de categoría y marca si existen
        if (this.producto.categoria_id) {
          const categoriaResponse = await axios.get(
            `http://localhost:5000/tienda/categorias/${this.producto.categoria_id}`
          );
          this.producto.categoria = categoriaResponse.data;
        }

        if (this.producto.marca_id) {
          const marcaResponse = await axios.get(
            `http://localhost:5000/tienda/marcas/${this.producto.marca_id}`
          );
          this.producto.marca = marcaResponse.data;
        }
      } catch (error) {
        this.errorMessage =
          error.response?.data?.message || "Hubo un problema al cargar el producto.";
      } finally {
        this.isLoading = false;
      }
    },
    buscarProductos(query) {
      this.searchQuery = query; // Actualiza el valor local del query
      if (query.trim() !== "") {
        // Redirige al HomePage con el término de búsqueda como parámetro de consulta
        this.$router.push({ name: "HomePage", query: { search: query } });
      }
    },
    cambiarImagenPrincipal(index) {
      // Cambiar el medio seleccionado (imagen o video)
      this.imagenSeleccionada = index;
    },
    formatPrice(price) {
      return parseFloat(price).toFixed(2);
    },
    getFullImageUrl(relativeUrl) {
      return `http://localhost:5000${relativeUrl}`;
    },
    cerrarSesion() {
      // Elimina el token y actualiza el estado de autenticación
      localStorage.removeItem("access_token");
      this.isAuthenticated = false;
      this.$router.push("/login"); // Redirige al usuario al login
    },
    redirigirLogin() {
      this.$router.push("/login");
    },
  },
  async created() {
    this.isAuthenticated = !!localStorage.getItem("access_token");

    if (this.isAuthenticated) {
      await this.cargarProducto();
    }
  },
};
</script>


<style scoped>
/* ================= Animaciones ================= */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleUp {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.5);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* ================= Contenedor Principal ================= */
.producto-contenedor {
  animation: fadeIn 1s ease;
  display: flex;
  flex-direction: column;
  gap: 30px;
  max-width: 1200px;
  margin: auto;
  padding: 20px;
  background-color: #f9fafb;
  border-radius: 15px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}
/* ================= Sección de Detalles ================= */
.detalle-contenedor {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
  background-color: #ffffff;
  border-radius: 15px;
  padding: 30px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.detalle-contenedor:hover {
  transform: scale(1.02);
}

/* Botón de Reseñas */
.boton-reseña {
  padding: 12px 20px;
  font-size: 18px;
  font-weight: bold;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  background-color: #ffc107;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.boton-reseña:hover {
  background-color: #e0a800;
  transform: translateY(-2px);
}

/* ================= Galería de Imágenes ================= */
.galeria-imagenes {
  flex: 1.5;
  display: flex;
  flex-direction: column;
  gap: 20px;
  animation: fadeIn 1s ease;
}

/* Contenedor de miniaturas */
.miniaturas {
  display: flex;
  gap: 10px;
  overflow-x: auto;
  padding: 10px 0;
  scrollbar-width: thin;
  scrollbar-color: #ffa726 transparent;
}

.miniaturas::-webkit-scrollbar {
  height: 8px;
}

.miniaturas::-webkit-scrollbar-track {
  background: transparent;
}

.miniaturas::-webkit-scrollbar-thumb {
  background-color: #ffa726;
  border-radius: 8px;
}

/* Miniaturas */
.imagen-miniatura {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border: 2px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
  animation: fadeIn 0.6s ease;
  position: relative;
  z-index: 1;
}

.imagen-miniatura:hover {
  transform: scale(1.2);
  border-color: #ffa726;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
  z-index: 2;
}

/* Efecto visual al seleccionar una miniatura */
.imagen-miniatura.active {
  transform: scale(1.3);
  border-color: #fb8c00;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
}

/* Contenedor de la imagen principal */
.imagen-principal {
  position: relative;
  overflow: hidden;
  border-radius: 15px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  background-color: #f0f0f0;
  animation: zoomIn 1s ease;
}

/* Imagen principal */
.imagen-principal .imagen-grande {
  width: 100%;
  max-height: 600px;
  object-fit: contain;
  border-radius: 15px;
  transition: transform 0.5s ease, box-shadow 0.5s ease;
}

.imagen-principal .imagen-grande:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

/* Efectos adicionales para videos principales */
.imagen-principal video {
  width: 100%;
  max-height: 600px;
  object-fit: contain;
  border-radius: 15px;
  transition: transform 0.5s ease, box-shadow 0.5s ease;
}

.imagen-principal video:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
}

/* Efectos de capa sobre miniaturas */
.imagen-miniatura::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.2) 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
  border-radius: 8px;
  z-index: 1;
}

.imagen-miniatura:hover::before {
  opacity: 1;
}

/* Indicador de selección */
.imagen-miniatura::after {
  content: "✓";
  position: absolute;
  top: 5px;
  right: 5px;
  color: #fff;
  background: #ffa726;
  width: 20px;
  height: 20px;
  font-size: 14px;
  font-weight: bold;
  text-align: center;
  line-height: 20px;
  border-radius: 50%;
  display: none;
}

.imagen-miniatura.active::after {
  display: block;
}

/* ================= Videos ================= */
.video-grande {
  width: 100%;
  max-height: 600px;
  object-fit: contain;
  border-radius: 15px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.video-grande:hover {
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.video-miniatura {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border: 2px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.video-miniatura:hover {
  transform: scale(1.2);
  border-color: #007bff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

/* ================= Información del Producto ================= */
.informacion-producto {
  flex: 1;
  padding: 25px;
  background-color: #1c1c1c; /* Fondo negro */
  border: 1px solid #333333; /* Bordes oscuros */
  border-radius: 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  color: #f5f5f5; /* Texto blanco suave */
}

.nombre-producto {
  font-size: 30px;
  font-weight: bold;
  color: #ffa726; /* Naranja */
  margin-bottom: 15px;
}

.precio-contenedor {
  margin: 20px 0;
  display: flex;
  align-items: center;
  gap: 15px;
}

.precio-descuento {
  font-size: 26px;
  font-weight: bold;
  color: #ffa726; /* Naranja */
}

.precio-original {
  font-size: 20px;
  color: #dc3545; /* Rojo */
  text-decoration: line-through;
}

.stock-producto {
  font-size: 18px;
  color: #f5f5f5; /* Blanco suave */
  margin-bottom: 20px;
}

/* ================= Descripción del Producto ================= */
.descripcion-producto ul {
  list-style: none;
  padding-left: 0;
}

.descripcion-producto li {
  margin-bottom: 10px;
  font-size: 16px;
  line-height: 1.5;
  color: #f5f5f5; /* Blanco suave */
}

.descripcion-producto strong {
  color: #ffa726; /* Naranja */
}

/* ================= Botones de Acción ================= */
.botones-accion {
  display: flex;
  gap: 15px;
  margin-top: 25px;
}

.boton-compra,
.boton-carrito {
  padding: 12px 20px;
  font-size: 18px;
  font-weight: bold;
  color: #1c1c1c; /* Texto negro */
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.boton-compra {
  background-color: #ffa726; /* Naranja */
}

.boton-compra:hover {
  background-color: #fb8c00; /* Naranja más oscuro */
  transform: translateY(-2px);
}

.boton-carrito {
  background-color: #ffa726; /* Naranja */
}

.boton-carrito:hover {
  background-color: #fb8c00; /* Naranja más oscuro */
  transform: translateY(-2px);
}


</style>


