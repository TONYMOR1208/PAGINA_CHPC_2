<template>
    <div class="reseñas-productos">
      <h1>Reseñas del Producto</h1>
  
      <!-- Botón para volver al detalle del producto -->
      <button @click="volverAlProducto" class="boton-volver">Volver al Producto</button>
  
      <!-- Lista de reseñas -->
      <div v-if="reseñas.length > 0">
        <div v-for="reseña in reseñas" :key="reseña.id" class="reseña-item">

          <h3>Reseña de {{ reseña.usuario }}</h3>
          <p>{{ reseña.comentario }}</p>
          <span class="calificacion">Calificación: {{ reseña.calificacion }} / 5</span>
        </div>
      </div>
  
      <!-- Mensaje si no hay reseñas -->
      <div v-else>
        <p>No hay reseñas para este producto. Sé el primero en dejar una reseña.</p>
      </div>
  
      <!-- Formulario para agregar una nueva reseña -->
      <form @submit.prevent="agregarReseña" class="form-reseña">
        <label for="comentario">Tu comentario:</label>
        <textarea v-model="nuevaReseña.comentario" id="comentario" required></textarea>
  
        <label for="calificacion">Calificación (1-5):</label>
        <input
          type="number"
          v-model.number="nuevaReseña.calificacion"
          id="calificacion"
          min="1"
          max="5"
          required
        />
  
        <button type="submit" class="boton-enviar">Enviar Reseña</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ReseñasProductos',
    data() {
      return {
        reseñas: [],
        nuevaReseña: {
          comentario: '',
          calificacion: 1,
        },
        idProducto: this.$route.params.id, // Obtiene el ID del producto desde la ruta
      };
    },
    methods: {
      async cargarReseñas() {
        try {
          const response = await axios.get(
            `http://localhost:5000/tienda/productos/${this.idProducto}/reseñas`
          );
          this.reseñas = response.data;
        } catch (error) {
          console.error('Error al cargar las reseñas:', error);
        }
      },
      async agregarReseña() {
        try {
          await axios.post(
            `http://localhost:5000/tienda/productos/${this.idProducto}/reseñas`,
            this.nuevaReseña,
            {
              headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` },
            }
          );
          alert('Reseña agregada con éxito');
          this.nuevaReseña = { comentario: '', calificacion: 1 };
          this.cargarReseñas(); // Recargar las reseñas después de agregar
        } catch (error) {
          console.error('Error al agregar la reseña:', error);
        }
      },
      volverAlProducto() {
        this.$router.push({ name: 'ProductoDetalle', params: { id: this.idProducto } });
      },
    },
    async created() {
      await this.cargarReseñas();
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
  .form-reseña input {
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
  