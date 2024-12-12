<template>
    <div>
      <HeaderAnth
        :isAuthenticated="isAuthenticated"
        @cerrar-sesion="cerrarSesion"
      />
  
      <div class="service-container">
        <h1 class="main-title">Servicios Técnicos Especializados</h1>
        <p class="description">
          Descubre los servicios que ofrecemos para garantizar el funcionamiento óptimo de tus dispositivos tecnológicos.
        </p>
  
        <div class="services-grid">
          <div class="service-card" @click="showImageModal(require('@/images/serviciotecnico/reparacion.jpg'))">
            <img src="@/images/serviciotecnico/reparacion.jpg" alt="Reparación de laptops" class="service-image" />
            <h3>Reparación de laptops</h3>
            <p>Solución de problemas de hardware y software para laptops de todas las marcas.</p>
          </div>
          <div class="service-card" @click="showImageModal('https://via.placeholder.com/300x200?text=Impresora+Mantenida')">
            <img src="https://via.placeholder.com/300x200?text=Impresora+Mantenida" alt="Mantenimiento de impresoras" class="service-image" />
            <h3>Mantenimiento de impresoras</h3>
            <p>Servicios de limpieza y reparación para impresoras láser y de inyección de tinta.</p>
          </div>
          <div class="service-card" @click="showImageModal('https://via.placeholder.com/300x200?text=Pantalla+Reemplazada')">
            <img src="https://via.placeholder.com/300x200?text=Pantalla+Reemplazada" alt="Reemplazo de pantallas" class="service-image" />
            <h3>Reemplazo de pantallas</h3>
            <p>Cambio de pantallas dañadas en laptops, tablets y smartphones.</p>
          </div>
          <div class="service-card" @click="showImageModal('https://via.placeholder.com/300x200?text=PC+Optimizada')">
            <img src="https://via.placeholder.com/300x200?text=PC+Optimizada" alt="Optimización de PC" class="service-image" />
            <h3>Optimización de PC</h3>
            <p>Mejoramos el rendimiento de tu computadora con actualizaciones y limpieza profunda.</p>
          </div>
        </div>
  
        <div v-if="isModalVisible" class="modal-overlay" @click="hideImageModal">
          <div class="modal-content" @click.stop>
            <img :src="modalImage" alt="Imagen ampliada" class="modal-image" />
            <button class="close-button" @click="hideImageModal">&times;</button>
          </div>
        </div>
  
        <div class="contact-section">
          <p>¿Necesitas más información? Contáctanos directamente en WhatsApp:</p>
          <a href="https://wa.me/593995924867" target="_blank" rel="noopener noreferrer" class="whatsapp-link">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" alt="WhatsApp" class="whatsapp-icon" />
            <span>Escríbenos en WhatsApp</span>
          </a>
        </div>
      </div>
         <!-- Pie de página -->
    <FooterAnth />
    </div>
  </template>
  
  <script>
  import HeaderAnth from "@/components/HeaderAnth.vue";
    import FooterAnth from "@/components/FooterAnth.vue";
  
  export default {
    name: "ServicioTecnico",
    components: {
      HeaderAnth,
        FooterAnth,

    },
    data() {
      return {
        isAuthenticated: false,
        isModalVisible: false,
        modalImage: "",
      };
    },
    methods: {
      showImageModal(imageUrl) {
        console.log("Image URL:", imageUrl); // Log para depuración
        this.modalImage = imageUrl;
        this.isModalVisible = true;
      },
      hideImageModal() {
        this.isModalVisible = false;
        this.modalImage = "";
      },
    },
    async created() {
      this.isAuthenticated = !!localStorage.getItem("access_token");
    },
  };
  </script>
  
  <style scoped>
  body {
    margin: 0;
    padding: 0;
    font-family: 'Roboto', Arial, sans-serif;
    color: #333;
    background-color: #f5f7fa;
  }
  
  .service-container {
    text-align: center;
    margin: 40px auto;
    max-width: 1200px;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 15px;
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  }
  
  .main-title {
    font-size: 36px;
    color: #34495e;
    margin-bottom: 20px;
    font-weight: bold;
  }
  
  .description {
    font-size: 18px;
    color: #7f8c8d;
    margin-bottom: 40px;
    line-height: 1.5;
  }
  
  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0 20px;
  }
  
  .service-card {
    background-color: #fefefe;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
  }
  
  .service-card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  }
  
  .service-image {
    width: 100%;
    height: auto;
    border-radius: 5px;
    margin-bottom: 15px;
    transition: transform 0.3s ease;
  }
  
  .service-card:hover .service-image {
    transform: scale(1.1);
  }
  
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-content {
    position: relative;
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    max-width: 90%;
    max-height: 90%;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
  }
  
  .modal-image {
    width: 100%;
    height: auto;
    border-radius: 10px;
  }
  
  .close-button {
    position: absolute;
    top: 10px;
    right: 10px;
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #333;
  }
  
  .contact-section {
    margin-top: 40px;
    text-align: center;
  }
  
  .whatsapp-link {
    display: inline-flex;
    align-items: center;
    text-decoration: none;
    background-color: #25d366;
    color: #ffffff;
    padding: 10px 20px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s;
  }
  
  .whatsapp-link:hover {
    background-color: #1da851;
  }
  
  .whatsapp-icon {
    width: 25px;
    height: 25px;
    margin-right: 10px;
  }
  </style>