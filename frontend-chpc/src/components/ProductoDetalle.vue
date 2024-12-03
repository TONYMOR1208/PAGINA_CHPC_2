<template>
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

    <!-- Detalles del producto -->
    <div v-if="producto && !isLoading && !errorMessage" class="producto-detalle">
      <!-- Imágenes del producto -->
      <div class="galeria-imagenes">
        <div class="miniaturas">
          <img
            v-for="(media, index) in producto.media || []"
            :key="index"
            :src="getFullImageUrl(media.url)"
            :alt="`Imagen adicional ${index + 1}`"
            class="imagen-miniatura"
            @click="cambiarImagenPrincipal(index)"
          />
        </div>
        <div class="imagen-principal">
          <img
            :src="getFullImageUrl(producto.media?.[imagenSeleccionada]?.url || '')"
            :alt="`Imagen principal de ${producto.nombre_producto || ''}`"
            class="imagen-grande"
          />
        </div>
      </div>

      <!-- Información del producto -->
      <div class="informacion-producto">
        <h1 class="nombre-producto">{{ producto.nombre_producto }}</h1>
        <p class="precio-producto">USD ${{ formatPrice(producto.precio) }}</p>
        <p class="stock-producto">
          {{ producto.stock > 0 ? "En stock" : "Agotado" }}
        </p>
        <p><strong>Categoría:</strong> {{ producto.categoria?.nombre_categoria || 'Sin categoría' }}</p>
        <p><strong>Marca:</strong> {{ producto.marca?.nombre_marca || 'Sin marca' }}</p>
        <p v-if="producto.peso"><strong>Peso:</strong> {{ producto.peso }} kg</p>
        <p v-if="producto.color"><strong>Color:</strong> {{ producto.color }}</p>

        <button class="boton-compra">Comprar ahora</button>
        <button class="boton-carrito">Añadir al carrito</button>
      </div>
    </div>

    <!-- Reseñas del producto -->
    <div v-if="producto && producto.reseñas" class="producto-reseñas">
      <h3>Reseñas</h3>
      <div v-if="producto.reseñas.length">
        <div v-for="(reseña, index) in producto.reseñas" :key="index" class="reseña">
          <p><strong>Usuario:</strong> {{ reseña.cliente?.nombre_usuario || 'Anónimo' }}</p>
          <p><strong>Calificación:</strong> {{ reseña.calificacion }} / 5</p>
          <p><strong>Comentario:</strong> {{ reseña.texto_resena }}</p>
          <p><small>{{ formatDate(reseña.fecha_resena) }}</small></p>
        </div>
      </div>
      <div v-else>
        <p>No hay reseñas para este producto.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
  return {
    producto: {
      media: [],
      reseñas: [],
    },
    errorMessage: "",
    isLoading: true,
    nuevaReseña: {
      calificacion: null,
      comentario: "",
    },
    imagenSeleccionada: 0,
  };
}
,
  methods: {
    async cargarProducto() {
      this.isLoading = true;
      this.errorMessage = "";

      const productoId = this.$route.params.id;
      try {
        const response = await axios.get(
          `http://localhost:5000/tienda/productos/${productoId}`
        );
        this.producto = response.data;
      } catch (error) {
        this.errorMessage =
          error.response?.data?.message ||
          "Hubo un problema al cargar el producto.";
      } finally {
        this.isLoading = false;
      }
    },
    async enviarReseña() {
      const productoId = this.$route.params.id;
      const usuarioId = localStorage.getItem("user_id");
      try {
        const response = await axios.post(
          `http://localhost:5000/tienda/reseñas`,
          {
            id_producto: productoId,
            id_cliente: usuarioId,
            calificacion: this.nuevaReseña.calificacion,
            texto_resena: this.nuevaReseña.comentario,
          }
        );

        this.producto.reseñas.push(response.data);
        this.nuevaReseña = { calificacion: null, comentario: "" };
      } catch (error) {
        this.errorMessage =
          error.response?.data?.message ||
          "Hubo un problema al enviar la reseña.";
      }
    },
    cambiarImagenPrincipal(index) {
      this.imagenSeleccionada = index;
    },
    formatPrice(price) {
      return parseFloat(price).toFixed(2);
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString("es-ES", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    },
    getFullImageUrl(relativeUrl) {
      return `http://localhost:5000${relativeUrl}`;
    },
  },
  created() {
    this.cargarProducto();
  },
};
</script>
<style scoped>
.producto-contenedor {
  display: flex;
  flex-direction: column;
  gap: 20px;
  max-width: 1200px;
  margin: auto;
}

.galeria-imagenes {
  display: flex;
  gap: 20px;
}

.miniaturas {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.imagen-miniatura {
  width: 70px;
  height: 70px;
  object-fit: cover;
  border: 2px solid transparent;
  cursor: pointer;
  transition: border-color 0.3s ease;
}

.imagen-miniatura:hover {
  border-color: #ff9900;
}

.imagen-principal .imagen-grande {
  width: 500px;
  border-radius: 5px;
}

.informacion-producto {
  flex: 1;
}

.nombre-producto {
  font-size: 24px;
  font-weight: bold;
}

.precio-producto {
  color: #b12704;
  font-size: 22px;
}

.boton-compra,
.boton-carrito {
  width: 100%;
  padding: 12px 20px;
  border: none;
  font-size: 16px;
  margin: 10px 0;
  cursor: pointer;
}

.boton-compra {
  background-color: #ffa41c;
  color: white;
}

.boton-compra:hover {
  background-color: #ff8c00;
}

.boton-carrito {
  background-color: #e7e9ec;
}

.boton-carrito:hover {
  background-color: #d6d7da;
}
</style>
