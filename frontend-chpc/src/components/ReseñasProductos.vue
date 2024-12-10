<template>
  <HeaderAnth
    :searchQuery="searchQuery"
    :isAuthenticated="isAuthenticated"
    @buscar="buscarProductos"
    @cerrar-sesion="cerrarSesion"
  />
  <div class="reseñas-productos">
    <button class="boton-volver" @click="$router.push('/')">Volver</button>
    <h1>Reseñas del Producto</h1>

    <!-- Indicador de carga -->
    <div v-if="isLoading" class="spinner"></div>

    <!-- Lista de reseñas -->
    <ul v-if="!isLoading && reseñas.length">
      <li v-for="reseña in reseñas" :key="reseña.id" class="reseña-item">
        <p><strong>Calificación:</strong> {{ reseña.calificacion }}</p>
        <p><strong>Comentario:</strong> {{ reseña.texto_resena || "Sin comentario" }}</p>
        <p><strong>Cliente:</strong> {{ reseña.cliente.nombre_usuario || "Anónimo" }}</p>
        <p><small><strong>Fecha:</strong> {{ new Date(reseña.fecha_resena).toLocaleDateString() }}</small></p>
      </li>
    </ul>
    <p v-else-if="!isLoading">No hay reseñas disponibles.</p>

    <!-- Formulario para agregar una nueva reseña -->
    <h2>Agregar una Reseña</h2>
    <form @submit.prevent="agregarReseña" class="form-reseña" v-if="isAuthenticated">
      <div>
        <label for="calificacion">Calificación:</label>
        <select v-model="nuevaReseña.calificacion" id="calificacion" required>
          <option v-for="i in 5" :key="i" :value="i">{{ i }}</option>
        </select>
      </div>

      <div>
        <label for="comentario">Comentario:</label>
        <textarea
          v-model="nuevaReseña.comentario"
          id="comentario"
          placeholder="Escribe tu comentario aquí..."
          maxlength="250"
          required
        ></textarea>
      </div>

      <button type="submit" class="boton-enviar">Enviar Reseña</button>
    </form>
    <p v-else>
      <strong>Inicia sesión para agregar una reseña.</strong>
      <button @click="redirigirLogin" class="boton-login">Iniciar Sesión</button>
    </p>
  </div>
  <FooterAnth />
</template>

<script>
import axios from "axios";
import HeaderAnth from "./HeaderAnth.vue";
import FooterAnth from "./FooterAnth.vue";

export default {
  name: "ReseñasProductos",
  components: {
    HeaderAnth,
    FooterAnth,
  },
  data() {
    return {
      idProducto: null, // ID del producto
      reseñas: [], // Lista de reseñas
      nuevaReseña: {
        comentario: "",
        calificacion: 1,
        id_cliente: null, // Este valor deberá configurarse según el cliente autenticado
      },
      isLoading: false, // Indicador de carga
      isAuthenticated: false,
    };
  },
  methods: {
    // Verifica si el usuario está autenticado
    verificarAutenticacion() {
      this.isAuthenticated = !!localStorage.getItem("access_token");
    },

    // Cargar reseñas para un producto específico
    async cargarReseñas() {
      this.isLoading = true;
      try {
        const response = await axios.get(
          `http://localhost:5000/tienda/reseñas?producto=${this.idProducto}`
        );
        this.reseñas = response.data;
      } catch (error) {
        console.error("Error al cargar las reseñas:", error);
        alert(
          error.response?.data?.message || "Hubo un error al cargar las reseñas."
        );
      } finally {
        this.isLoading = false;
      }
    },

    // Agregar una nueva reseña
    async agregarReseña() {
      try {
        if (!this.isAuthenticated) {
          alert("Por favor, inicia sesión para agregar una reseña.");
          return;
        }

        if (!this.nuevaReseña.comentario.trim()) {
          alert("El comentario no puede estar vacío.");
          return;
        }

        this.nuevaReseña.id_cliente = this.obtenerClienteAutenticado();

        await axios.post(
          `http://localhost:5000/tienda/reseñas`,
          { ...this.nuevaReseña, id_producto: this.idProducto },
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );

        alert("Reseña agregada con éxito.");
        this.nuevaReseña = { comentario: "", calificacion: 1 };
        this.cargarReseñas();
      } catch (error) {
        console.error("Error al agregar la reseña:", error);
        alert(
          error.response?.data?.message || "Hubo un error al agregar la reseña."
        );
      }
    },

    // Simular obtención del cliente autenticado
    obtenerClienteAutenticado() {
      const id_cliente = 1; // Cambiar esto según tu lógica de autenticación
      return id_cliente;
    },

    // Redirigir al login
    redirigirLogin() {
      this.$router.push("/login");
    },
  },
  created() {
    this.verificarAutenticacion();
    this.idProducto = this.$route.params.idProducto;
    this.cargarReseñas();
  },
};
</script>


<style scoped>
.reseñas-productos {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.boton-volver {
  display: inline-block;
  margin-bottom: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.boton-volver:hover {
  background-color: #0056b3;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border-left-color: #007bff;
  animation: spin 1s linear infinite;
  margin: 20px auto;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.reseña-item {
  padding: 15px;
  border-bottom: 1px solid #ddd;
  margin-bottom: 15px;
}

.reseña-item:last-child {
  border-bottom: none;
}

.calificacion {
  font-weight: bold;
  color: #28a745;
}

.form-reseña {
  margin-top: 20px;
  padding: 15px;
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.form-reseña label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-reseña textarea,
.form-reseña select {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.boton-enviar {
  padding: 10px 20px;
  background-color: #28a745;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.boton-enviar:hover {
  background-color: #1e7e34;
}
</style>
