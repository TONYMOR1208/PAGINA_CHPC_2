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
        <button class="boton-compra">Comprar ahora</button>
        <button class="boton-carrito">Añadir al carrito</button>
        <button class="boton-reseña" @click="redirigirAgregarReseña">Agregar Reseña</button>
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
    redirigirAgregarReseña() {
      this.$router.push({ name: "ReseñasProductos", params: { id: this.$route.params.id } });
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
/* Contenedor principal */
.producto-contenedor {
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

/* Sección de detalles */
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
  transform: scale(1.02); /* Ampliación suave */
}
.boton-reseña {
  padding: 12px 20px;
  font-size: 18px;
  font-weight: bold;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  background-color: #ffc107; /* Color de botón amarillo */
  transition: background-color 0.3s ease, transform 0.2s ease;
}
.video-miniatura {
  width: 90px;
  height: 90px;
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

.video-grande {
  max-width: 100%;
  max-height: 500px;
  border-radius: 15px;
}


.boton-reseña:hover {
  background-color: #e0a800; /* Cambio de color al pasar el cursor */
  transform: translateY(-2px);
}


/* Galería de imágenes */
.galeria-imagenes {
  flex: 1.5;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.miniaturas {
  display: flex;
  gap: 10px;
  overflow-x: auto;
}

.imagen-miniatura {
  width: 90px;
  height: 90px;
  object-fit: cover;
  border: 2px solid transparent;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.imagen-miniatura:hover {
  transform: scale(1.2); /* Incrementar tamaño */
  border-color: #007bff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.imagen-principal {
  position: relative;
  overflow: hidden;
  border-radius: 15px;
}

.imagen-principal .imagen-grande {
  max-width: 100%;
  max-height: 500px;
  object-fit: contain;
  border-radius: 15px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.imagen-principal .imagen-grande:hover {
  transform: scale(1.05); /* Incrementar tamaño */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}


/* Información del producto */
.informacion-producto {
  flex: 1;
  padding: 25px;
  background-color: #fefefe;
  border: 1px solid #e0e0e0;
  border-radius: 15px;
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.05);
}

.nombre-producto {
  font-size: 30px;
  font-weight: bold;
  color: #333;
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
  color: #28a745;
}

.precio-original {
  font-size: 20px;
  color: #dc3545;
  text-decoration: line-through;
}

.stock-producto {
  font-size: 18px;
  color: #555;
  margin-bottom: 20px;
}

/* Descripción */
.descripcion-producto ul {
  list-style: none;
  padding-left: 0;
}

.descripcion-producto li {
  margin-bottom: 10px;
  font-size: 16px;
  line-height: 1.5;
}

.descripcion-producto strong {
  color: #333;
}

/* Botones de acción */
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
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.boton-compra {
  background-color: #007bff;
}

.boton-compra:hover {
  background-color: #0056b3;
  transform: translateY(-2px);
}

.boton-carrito {
  background-color: #28a745;
}

.boton-carrito:hover {
  background-color: #1e7e34;
  transform: translateY(-2px);
}

</style>


