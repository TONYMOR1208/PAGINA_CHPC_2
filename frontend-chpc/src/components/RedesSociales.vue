<template>
    <div>
      <HeaderAnth
        :isAuthenticated="isAuthenticated"
        @cerrar-sesion="cerrarSesion"
      />
  
      <div class="social-container">
        <h1 class="main-title">Síguenos en nuestras Redes Sociales</h1>
        <p class="description">
          Conéctate con nosotros a través de nuestras redes sociales y mantente al día con nuestras últimas noticias y ofertas.
        </p>
        <div class="social-grid">
          <div v-for="red in redesSociales" :key="red.nombre" class="social-card">
            <a :href="red.url" target="_blank" rel="noopener noreferrer">
              <img :src="red.icono" :alt="'Ícono de ' + red.nombre" class="social-icon" />
              <h3>{{ red.nombre }}</h3>
            </a>
          </div>
        </div>
      </div>
  
      <FooterAnth />
    </div>
  </template>
  
  <script>
 
  import HeaderAnth from "@/components/HeaderAnth.vue";
  import FooterAnth from "@/components/FooterAnth.vue";
  
  export default {
    name: "RedesSociales",
    components: {
      HeaderAnth,
      FooterAnth,
    },
    data() {
      return {
        redesSociales: [
          {
            nombre: "Facebook",
            url: "https://www.facebook.com/tuempresa",
            icono: "https://cdn-icons-png.flaticon.com/512/733/733547.png",
          },
          {
            nombre: "Instagram",
            url: "https://www.instagram.com/tuempresa",
            icono: "https://cdn-icons-png.flaticon.com/512/733/733558.png",
          },
          {
            nombre: "Twitter",
            url: "https://www.twitter.com/tuempresa",
            icono: "https://cdn-icons-png.flaticon.com/512/733/733579.png",
          },
          {
            nombre: "LinkedIn",
            url: "https://www.linkedin.com/company/tuempresa",
            icono: "https://cdn-icons-png.flaticon.com/512/733/733561.png",
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
  
  <style>
  body {
    background-color: #f9fafb;
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
  }
  
  .social-container {
    text-align: center;
    margin: 40px auto;
    max-width: 1200px;
  }
  
  .main-title {
    font-size: 32px;
    color: #333;
    margin-bottom: 10px;
  }
  
  .description {
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
  }
  
  .social-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 30px;
    padding: 0 20px;
  }
  
  @media (max-width: 768px) {
    .social-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }
  
  @media (max-width: 480px) {
    .social-grid {
      grid-template-columns: 1fr;
    }
  }
  
  .social-card {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .social-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
  }
  
  .social-icon {
    width: 100px;
    height: 100px;
    object-fit: contain;
    margin: 10px auto 15px;
  }
  
  .social-card h3 {
    font-size: 18px;
    color: #333;
    margin: 10px 0;
    text-transform: capitalize;
  }
  </style>
  