<template>
  <div>
    <HeaderAnth
      :isAuthenticated="isAuthenticated"
      @cerrar-sesion="cerrarSesion"
    />

    <transition-group name="fade" tag="div" class="social-container">
      <h1 class="main-title">Síguenos en nuestras Redes Sociales</h1>
      <p class="description">
        Conéctate con nosotros a través de nuestras redes sociales y mantente al día con nuestras últimas noticias y ofertas.
      </p>
      <div class="social-grid">
        <div
          v-for="red in redesSociales"
          :key="red.nombre"
          class="social-card fade-in"
        >
          <a :href="red.url" target="_blank" rel="noopener noreferrer">
            <img
              :src="red.icono"
              :alt="'\u00cdcono de ' + red.nombre"
              class="social-icon"
            />
            <h3>{{ red.nombre }}</h3>
          </a>
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import HeaderAnth from "@/components/HeaderAnth.vue";

export default {
  name: "RedesSociales",
  components: {
    HeaderAnth,
  },
  data() {
    return {
      redesSociales: [
        {
          nombre: "Facebook",
          url: "https://www.facebook.com/clickherepcecuador",
          icono: "https://cdn-icons-png.flaticon.com/512/733/733547.png",
        },
        {
          nombre: "Instagram",
          url: "https://www.instagram.com/clickhere.pc?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==",
          icono: "https://cdn-icons-png.flaticon.com/512/733/733558.png",
        },
        {
          nombre: "TikTok",
          url: "https://www.tiktok.com/@chpctecnologia",
          icono: "https://cdn-icons-png.flaticon.com/512/3046/3046121.png",
        },
        {
          nombre: "WhatsApp",
          url: "https://wa.me/593995924867",
          icono: "https://cdn-icons-png.flaticon.com/512/733/733585.png",
        },
      ],
      isAuthenticated: false,
    };
  },
  methods: {
    cerrarSesion() {
      localStorage.removeItem("access_token");
      this.isAuthenticated = false;
      this.$router.replace("/login");
    },
  },
  created() {
    this.isAuthenticated = !!localStorage.getItem("access_token");
  },
};
</script>

<style scoped>
body {
  background-color: #f5f5f5; /* Gris claro */
  margin: 0;
  padding: 0;
  font-family: "Roboto", sans-serif; /* Tipografía uniforme */
  color: #333; /* Color de texto principal */
}

.social-container {
  text-align: center;
  margin: 40px auto;
  max-width: 1400px;
  padding: 40px;
  background-color: #ffffff;
  border-radius: 20px;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.main-title {
  font-size: 42px;
  color: #2c3e50;
  margin-bottom: 20px;
  font-weight: bold;
}

.description {
  font-size: 20px;
  color: #7f8c8d;
  margin-bottom: 40px;
  line-height: 1.8;
}

.social-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 40px;
  padding: 0 30px;
}

@media (max-width: 768px) {
  .social-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
  }
}

@media (max-width: 480px) {
  .social-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}

.social-card {
  background-color: #fefefe;
  border: none;
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
  text-align: center;
  transition: transform 0.3s, box-shadow 0.3s;
}

.social-card:hover {
  transform: translateY(-15px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
}

.social-icon {
  width: 100px;
  height: 100px;
  object-fit: contain;
  margin: 20px auto;
}

a {
  text-decoration: none;
  color: inherit;
}

a:hover {
  color: #3498db;
}

/* Animación de desvanecimiento */
.fade-in {
  animation: fadeIn 1s ease-in-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10%);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Transiciones para el grupo */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s, transform 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(20%);
}
</style>
