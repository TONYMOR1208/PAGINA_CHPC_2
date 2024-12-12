<template>
  <div>
    <!-- Header con opción para ir a la página principal -->
    <HeaderAnth
      :searchQuery="searchQuery"
      :isAuthenticated="isAuthenticated"
      @buscar="buscarProductos"
      @cerrar-sesion="cerrarSesion"
    />

    <!-- Contenedor de inicio de sesión -->
    <div class="login-container">
      <h2>Iniciar Sesión</h2>
      <form @submit.prevent="login">
        <div class="input-group">
          <label for="nombre_usuario">Nombre de usuario *</label>
          <input
            v-model="nombre_usuario"
            id="nombre_usuario"
            type="text"
            placeholder="Nombre de usuario"
            required
            @input="clearError"
          />
          <p v-if="error && !contraseña" class="error">{{ error }}</p>
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
              @input="clearError"
            />
            <span class="toggle-password" @click="togglePasswordVisibility">
              {{ passwordVisible ? '👁️' : '🙈' }}
            </span>
          </div>
        </div>

        <button type="submit" class="login-button">Iniciar sesión</button>
        <p class="account-info">
          ¿No tiene una cuenta? 
          <button class="create-account-link" @click="goToRegister">
            Regístrese aquí
          </button>
        </p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import HeaderAnth from './HeaderAnth.vue';

export default {
  name: "SesionUsuario",
  components: {
    HeaderAnth,
  },
  data() {
    return {
      nombre_usuario: '',
      contraseña: '',
      errors: {}, // Objeto para almacenar errores específicos
      error: '', // Error general
      passwordVisible: false,
    };
  },
  methods: {
    async login() {
      // Validar campos antes de enviar la solicitud
      this.validateFields();
      if (Object.keys(this.errors).length > 0) {
        return; // Detener si hay errores de validación
      }
      try {
        const response = await axios.post('http://localhost:5000/tienda/auth/login', {
          nombre_usuario: this.nombre_usuario,
          contraseña: this.contraseña,
        });
        localStorage.setItem('access_token', response.data.access_token); // Guarda el token en localStorage
        this.$router.replace('/home'); // Usa replace en lugar de push
      } catch (err) {
        this.error = err.response?.data?.mensaje || "Credenciales inválidas. Intenta de nuevo.";
      }
    },
    validateFields() {
      this.errors = {}; // Limpiar errores previos

      // Validación del nombre de usuario
      if (!this.nombre_usuario.trim()) {
        this.errors.nombre_usuario = "El nombre de usuario es obligatorio.";
      } else if (this.nombre_usuario.trim().length < 3 || this.nombre_usuario.trim().length > 80) {
        this.errors.nombre_usuario =
          "El nombre de usuario debe tener entre 3 y 80 caracteres.";
      }

      // Validación de la contraseña
      if (!this.contraseña.trim()) {
        this.errors.contraseña = "La contraseña es obligatoria.";
      } else if (!/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$/.test(this.contraseña)) {
        this.errors.contraseña =
          "La contraseña debe tener al menos 6 caracteres, incluir una letra, un número y un carácter especial.";
      }
    },
    clearError(field) {
      // Elimina el error asociado a un campo específico
      delete this.errors[field];
    },
    togglePasswordVisibility() {
      this.passwordVisible = !this.passwordVisible;
    },
    goToRegister() {
      this.$router.push('/registro');
    },
  },
};
</script>

  <style scoped>
  /* Login Container */
  .login-container {
    max-width: 480px;
    margin: 50px auto;
    padding: 30px;
    background-color: #ffffff; /* Blanco */
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    font-family: 'Roboto', sans-serif;
  }
  
  .login-container h2 {
    text-align: center;
    color: #ffa726; /* Naranja */
    font-size: 24px;
    margin-bottom: 10px;
  }
  
  .input-group {
    margin-bottom: 20px;
  }
  
  .input-group label {
    font-size: 14px;
    color: #555555; /* Gris oscuro */
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
    border-color: #ffa726; /* Naranja */
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
    color: #ffa726; /* Naranja */
    cursor: pointer;
    transition: color 0.3s;
  }
  
  .toggle-password:hover {
    color: #fb8c00; /* Naranja más oscuro */
  }
  
  .login-button {
    width: 100%;
    padding: 14px;
    background-color: #1c1c1c; /* Negro */
    color: #ffffff; /* Blanco */
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    margin-top: 20px;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .login-button:hover {
    background-color: #ffa726; /* Naranja */
    color: #1c1c1c; /* Negro */
  }
  
  .account-info {
    margin-top: 15px;
    text-align: center;
    font-size: 14px;
    color: #666666; /* Gris */
  }
  
  .create-account-link {
    background: none;
    border: none;
    color: #ffa726; /* Naranja */
    cursor: pointer;
    font-size: 14px;
    text-decoration: underline;
    padding: 0;
  }
  
  .create-account-link:hover {
    color: #fb8c00; /* Naranja más oscuro */
  }
  
  .error {
    color: #e53935; /* Rojo para errores */
    font-size: 14px;
    text-align: left;
    margin-top: 5px;
  }
  </style>
  