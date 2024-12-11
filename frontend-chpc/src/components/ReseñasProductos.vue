<template>
  
    <!-- Encabezado -->
    <HeaderAnth
      :searchQuery="searchQuery"
      :isAuthenticated="isAuthenticated"
      @buscar="buscarProductos"
      @cerrar-sesion="cerrarSesion"
    />

    <!-- Título -->
    <div class="reseñas-container">
    <div class="header">
      <h1>Reseñas del Producto</h1>
      <p class="breadcrumb">
        <router-link to="/">Inicio</router-link> / <span>Reseñas</span>
      </p>
    </div>

    <!-- Listado de reseñas -->
    <section class="reseñas-list">
      <h2>Lo que dicen nuestros clientes</h2>
      <div v-if="reseñas.length">
        <div v-for="reseña in reseñas" :key="reseña.id" class="reseña-item">
          <div class="reseña-header">
            <p class="nombre-cliente">{{ reseña.cliente.nombre_usuario }}</p>
            <p class="calificacion">{{ reseña.calificacion }} ★</p>
          </div>
          <p class="comentario">{{ reseña.texto_resena }}</p>
          <p class="fecha">{{ new Date(reseña.fecha_resena).toLocaleDateString() }}</p>
          <div class="acciones">
            <button class="btn-editar" @click="editarResena(reseña)">Editar</button>
            <button class="btn-eliminar" @click="eliminarResena(reseña.id)">Eliminar</button>
          </div>
        </div>
      </div>
      <p v-else>No hay reseñas disponibles. Sé el primero en opinar.</p>
    </section>

    <!-- Formulario para crear o editar reseñas -->
    <section class="reseña-form">
      <h2>{{ editMode ? 'Editar Reseña' : 'Deja tu Reseña' }}</h2>
      <form @submit.prevent="guardarResena">
        <div class="form-group">
          <label for="calificacion">Calificación *</label>
          <input
            v-model="calificacion"
            id="calificacion"
            type="number"
            min="1"
            max="5"
            required
            class="input"
            placeholder="Calificación (1-5)"
          />
        </div>

        <div class="form-group">
          <label for="texto_resena">Comentario *</label>
          <textarea
            v-model="texto_resena"
            id="texto_resena"
            class="textarea"
            placeholder="Escribe tu opinión aquí"
            required
          ></textarea>
        </div>

        <div class="form-actions">
          <button type="submit" class="btn-submit">
            {{ editMode ? 'Actualizar' : 'Enviar' }}
          </button>
          <button v-if="editMode" type="button" @click="resetFormulario" class="btn-cancelar">Cancelar</button>
        </div>
      </form>

      <!-- Mensajes de éxito y error -->
      <p v-if="success" class="message success">{{ success }}</p>
      <p v-if="error" class="message error">{{ error }}</p>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import HeaderAnth from "./HeaderAnth.vue";

export default {
  name: "ReseñasProductos",
  components: {
    HeaderAnth,
  },
  data() {
    return {
      reseñas: [],
      calificacion: "",
      texto_resena: "",
      id_producto: 1, // Producto actual (dinámico en producción)
      id_cliente: 1, // Cliente autenticado (dinámico en producción)
      success: "",
      error: "",
      editMode: false,
      reseñaEditandoId: null,
    };
  },
  methods: {
    async obtenerReseñas() {
      try {
        const response = await axios.get(
          `http://localhost:5000/tienda/reseñas/producto/${this.id_producto}`
        );
        this.reseñas = response.data;
      } catch (err) {
        this.error = err.response?.data?.message || "Error al cargar las reseñas.";
      }
    },
    async guardarResena() {
      try {
        if (this.editMode) {
          // Actualizar reseña
          await axios.put(
            `http://localhost:5000/tienda/reseñas/${this.reseñaEditandoId}`,
            {
              calificacion: this.calificacion,
              texto_resena: this.texto_resena,
            }
          );
          this.success = "Reseña actualizada con éxito.";
        } else {
          // Crear reseña
          await axios.post("http://localhost:5000/tienda/reseñas/", {
            id_producto: this.id_producto,
            id_cliente: this.id_cliente,
            calificacion: this.calificacion,
            texto_resena: this.texto_resena,
          });
          this.success = "Reseña enviada con éxito.";
        }
        this.error = "";
        this.resetFormulario();
        this.obtenerReseñas();
      } catch (err) {
        this.error = err.response?.data?.message || "Error al procesar la reseña.";
        this.success = "";
      }
    },
    resetFormulario() {
      this.editMode = false;
      this.reseñaEditandoId = null;
      this.calificacion = "";
      this.texto_resena = "";
    },
    editarResena(reseña) {
      this.editMode = true;
      this.reseñaEditandoId = reseña.id;
      this.calificacion = reseña.calificacion;
      this.texto_resena = reseña.texto_resena;
    },
    async eliminarResena(id) {
      if (confirm("¿Seguro que deseas eliminar esta reseña?")) {
        try {
          await axios.delete(`http://localhost:5000/tienda/reseñas/${id}`);
          this.success = "Reseña eliminada con éxito.";
          this.obtenerReseñas();
        } catch (err) {
          this.error = err.response?.data?.message || "Error al eliminar la reseña.";
        }
      }
    },
  },
  mounted() {
    this.obtenerReseñas();
  },
};
</script>

<style>
.reseñas-container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: "Arial", sans-serif;
  color: #333;
}

.header {
  text-align: center;
  margin-bottom: 20px;
}

.header h1 {
  font-size: 2.5rem;
  font-weight: bold;
}

.breadcrumb {
  font-size: 0.9rem;
  color: #555;
}

.reseñas-list {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.reseña-item {
  border-bottom: 1px solid #ddd;
  padding: 10px 0;
}

.reseña-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nombre-cliente {
  font-weight: bold;
  font-size: 1.2rem;
}

.calificacion {
  color: #f5c518;
  font-weight: bold;
}

.acciones button {
  margin-right: 10px;
}

.reseña-form {
  background: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 15px;
}

.input, .textarea {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-submit {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}

.btn-submit:hover {
  background-color: #0056b3;
}

.btn-cancelar {
  background: none;
  border: 1px solid #ccc;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  color: #555;
  margin-left: 10px;
}

.btn-cancelar:hover {
  border-color: #888;
}

.message {
  margin-top: 15px;
  text-align: center;
  font-weight: bold;
}

.success {
  color: green;
}

.error {
  color: red;
}
</style>