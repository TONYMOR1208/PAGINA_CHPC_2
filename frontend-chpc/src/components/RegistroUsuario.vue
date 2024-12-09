<template>
  <div>
    <!-- Header con opción para ir a la página principal -->
    <HeaderAnth
      :searchQuery="searchQuery"
      :isAuthenticated="isAuthenticated"
      @buscar="buscarProductos"
      @cerrar-sesion="cerrarSesion"
    />
  </div>
  <br>

  <div class="register-container">
    <h2>Crear Una Cuenta</h2>
    <p><router-link to="/">Inicio</router-link> / Registro</p>

    <form @submit.prevent="register">
      <div class="input-group">
        <label for="nombre_usuario">Nombre de usuario *</label>
        <input
          v-model="nombre_usuario"
          id="nombre_usuario"
          type="text"
          placeholder="Nombre de usuario"
          required
          @input="clearError('nombre_usuario')"
        />
        <p v-if="errors.nombre_usuario" class="error">{{ errors.nombre_usuario }}</p>
      </div>

      <div class="input-group">
        <label for="email">Correo electrónico *</label>
        <input
          v-model="email"
          id="email"
          type="email"
          placeholder="Correo electrónico"
          required
          @input="clearError('email')"
        />
        <p v-if="errors.email" class="error">{{ errors.email }}</p>
      </div>

      <div class="input-group">
        <label for="telefono">Teléfono</label>
        <input
          v-model="telefono"
          id="telefono"
          type="text"
          placeholder="Número de teléfono"
          @input="clearError('telefono')"
        />
        <p v-if="errors.telefono" class="error">{{ errors.telefono }}</p>
      </div>

      <div class="input-group">
        <label for="direccion">Dirección</label>
        <input
          v-model="direccion"
          id="direccion"
          type="text"
          placeholder="Dirección"
          @input="clearError('direccion')"
        />
        <p v-if="errors.direccion" class="error">{{ errors.direccion }}</p>
      </div>

      <div class="input-group">
        <label for="contraseña">Contraseña *</label>
        <div class="password-container">
          <input
            v-model="contraseña"
            id="contraseña"
            :type="passwordVisible ? 'text' : 'password'"
            placeholder="Contraseña"
            required
            @input="clearError('contraseña')"
          />
          <span class="toggle-password" @click="togglePasswordVisibility">
            {{ passwordVisible ? '👁️' : '🙈' }}
          </span>
        </div>
        <p v-if="errors.contraseña" class="error">{{ errors.contraseña }}</p>
      </div>

      <button type="submit" class="register-button">Registrarse</button>

      <p class="account-info">
        ¿Ya tiene una cuenta? 
        <router-link to="/login">Inicie sesión aquí</router-link>
      </p>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
    <p v-if="success" class="success">{{ success }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import HeaderAnth from './HeaderAnth.vue';

export default {
  name: 'RegistroUsuario',
  components: {
    HeaderAnth,
  },
  data() {
    return {
      nombre_usuario: '',
      email: '',
      telefono: '',
      direccion: '',
      contraseña: '',
      errors: {},
      error: '',
      success: '',
      passwordVisible: false,
    };
  },
  methods: {
    async register() {
      this.validateFields();
      if (Object.keys(this.errors).length > 0) {
        return;
      }
      try {
        const response = await axios.post('http://localhost:5000/tienda/auth/registro', {
          nombre_usuario: this.nombre_usuario,
          email: this.email,
          telefono: this.telefono,
          direccion: this.direccion,
          contraseña: this.contraseña,
        });
        this.success = response.data.mensaje;
        this.clearForm();
      } catch (err) {
        this.error = err.response?.data?.mensaje || 'Error en el registro. Intenta de nuevo.';
      }
    },
    validateFields() {
      this.errors = {};
      if (this.nombre_usuario.length < 3 || this.nombre_usuario.length > 80) {
        this.errors.nombre_usuario = 'El nombre de usuario debe tener entre 3 y 80 caracteres.';
      }
      if (!this.email.includes('@')) {
        this.errors.email = 'El correo electrónico debe tener un formato válido.';
      }
      if (this.telefono && this.telefono.length > 20) {
        this.errors.telefono = 'El teléfono debe tener como máximo 20 caracteres.';
      }
      if (this.direccion && this.direccion.length > 255) {
        this.errors.direccion = 'La dirección debe tener como máximo 255 caracteres.';
      }
      if (!this.contraseña.match(/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$/)) {
        this.errors.contraseña = 'La contraseña debe tener al menos 6 caracteres, incluir una letra, un número y un carácter especial.';
      }
    },
    clearError(field) {
      delete this.errors[field];
    },
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    },
    clearForm() {
      this.nombre_usuario = '';
      this.email = '';
      this.telefono = '';
      this.direccion = '';
      this.contraseña = '';
      this.errors = {};
    },
  },
};
</script>

<style >
.register-container {
  max-width: 480px;
  margin: 50px auto;
  padding: 30px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

.register-container h2 {
  text-align: center;
  color: #333333;
  font-size: 24px;
  margin-bottom: 10px;
}

.register-container p {
  text-align: center;
  font-size: 14px;
  color: #666666;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  font-size: 14px;
  color: #555555;
  margin-bottom: 5px;
  display: block;
  font-weight: 500;
}

.input-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #cccccc;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.input-group input:focus {
  border-color: #007bff;
  outline: none;
}

.password-container {
  position: relative;
}

.toggle-password {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  font-size: 18px;
  color: #007bff;
  cursor: pointer;
  transition: color 0.3s;
}

.toggle-password:hover {
  color: #0056b3;
}

.register-button {
  width: 100%;
  padding: 14px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  margin-top: 20px;
  transition: background-color 0.3s;
}

.register-button:hover {
  background-color: #0056b3;
}

.error {
  color: #dc3545;
  font-size: 14px;
  text-align: left;
  margin-top: 5px;
}

.success {
  color: #28a745;
  text-align: center;
  font-weight: bold;
  font-size: 16px;
  margin-top: 10px;
}

.account-info {
  margin-top: 15px;
  text-align: center;
  font-size: 14px;
  color: #666666;
}

.account-info a {
  color: #007bff;
  text-decoration: none;
}

.account-info a:hover {
  text-decoration: underline;
}
</style>