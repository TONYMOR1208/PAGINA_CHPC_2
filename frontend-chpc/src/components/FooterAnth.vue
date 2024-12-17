<template>
  <footer class="footer-container">
    <div class="footer-content">
      <div class="footer-section about-us">
        <h4>Sobre Nosotros</h4>
        <p>
          Tenemos todo en Informática: Portátiles, Computadoras de escritorio, Impresoras, Tablets, Accesorios, Cámaras de seguridad, solo en CHCP Tecnología.
        </p>
        <p>Haz CLICK, lo tenemos...!</p>
      </div>
      <div class="footer-section contact-us">
        <h4>Contáctanos</h4>
        <p>Email: <a href="mailto:clickhereventas3@gmail.com">clickhereventas3@gmail.com</a></p>
        <p>Teléfono: <a href="tel:+593995924867">099 592 4867</a></p>
        <p>Dirección: Calle 12 Avenida 20 Esquina, Manta, Ecuador</p>
      </div>
      <div class="footer-section social-media">
        <h4>Redes Sociales</h4>
        <ul class="social-media-grid">
          <li v-for="red in redesSociales" :key="red.nombre">
            <a :href="red.url" target="_blank" rel="noopener noreferrer">
              <img :src="red.icono" :alt="red.nombre" class="social-icon" />
              {{ red.nombre }}
            </a>
          </li>
        </ul>
      </div>
    </div>
    <!-- Nueva sección para Misión y Visión -->
    <div class="mission-vision-section">
  <div class="mission-section">
    <h4 class="section-title">Nuestra Misión</h4>
    <p class="section-content">
      En CHPC Tecnología, nuestra misión es ir más allá de la simple venta de equipos tecnológicos. Nos dedicamos a crear 
      experiencias únicas mediante la combinación de innovación, calidad y servicio personalizado. Lo que nos hace 
      especiales es nuestro enfoque centrado en el cliente: analizamos profundamente sus desafíos, diseñamos soluciones 
      a medida y brindamos un acompañamiento continuo. Cada producto que ofrecemos refleja nuestro compromiso con la 
      excelencia y la tecnología de punta. Nos destacamos por integrar sostenibilidad en cada etapa del proceso, desde 
      la selección de productos hasta la gestión de residuos electrónicos, asegurando que nuestra huella tecnológica sea 
      positiva para nuestros clientes, la industria y el planeta.
    </p>
  </div>
  
  <div class="vision-section">
    <h4 class="section-title">Nuestra Visión</h4>
    <p class="section-content">
      Convertirnos en la referencia global en soluciones tecnológicas integrales, distinguiéndonos por nuestra capacidad 
      de anticipar las necesidades del mercado y ofrecer productos y servicios que redefinan la experiencia tecnológica. 
      Nos visualizamos liderando un ecosistema innovador donde cada equipo y solución que ofrecemos no solo resuelve 
      problemas, sino que transforma la manera en que las personas y las empresas interactúan con la tecnología. En CHPC 
      Tecnología, creemos que la verdadera innovación no es solo adelantarse al futuro, sino construirlo de la mano de 
      nuestros clientes, con un enfoque en sostenibilidad, inclusión y excelencia operativa.
    </p>
  </div>
</div>

    <div class="footer-bottom">
      <p>&copy; 2024 CHCP Tecnología. Todos los derechos reservados.</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "FooterAnth",
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
          url: "https://www.instagram.com/clickhere.pc",
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
    };
  },
};
</script>
<style scoped>
/* Estilos relacionados con el footer */
.footer-container {
  background: linear-gradient(135deg, #000, #333); /* Gradiente negro */
  color: white;
  padding: 30px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.footer-content {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  flex-wrap: wrap;
  gap: 20px;
  margin-bottom: 30px;
}

.footer-section {
  flex: 1;
  min-width: 250px;
  margin: 10px;
  text-align: left;
}

.footer-section h4 {
  margin-bottom: 15px;
  font-size: 18px;
  font-weight: bold;
  color: #ffa726; /* Naranja suave */
}

.footer-section p,
.footer-section ul {
  margin: 10px 0;
  line-height: 1.6;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section ul li {
  margin: 8px 0;
}

.footer-section ul li a {
  color: #ffa726; /* Naranja suave */
  text-decoration: none;
  display: flex;
  align-items: center;
  transition: color 0.3s;
}

.footer-section ul li a:hover {
  color: #ffffff;
}

.footer-section a {
  color: inherit;
}

.footer-section a:hover {
  text-decoration: underline;
}

.social-media-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
  justify-items: center;
  align-items: center;
  padding: 0;
  list-style: none;
}

.social-media-grid li {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.social-icon {
  width: 40px;
  height: 40px;
  margin-bottom: 8px;
  transition: transform 0.3s;
}

.social-icon:hover {
  transform: scale(1.1);
}

.footer-bottom {
  border-top: 1px solid #ffa726; /* Naranja suave */
  padding-top: 15px;
  font-size: 14px;
  color: #ffa726;
  
}

/* Estilos para la sección Misión y Visión */
.mission-vision-section {
  margin-top: 20px;
  padding: 20px 10px;
  border-top: 1px solid #ffa726; /* Línea divisoria en naranja suave */
  text-align: center;
}

.mission-vision-section h4 {
  margin-bottom: 15px;
  font-size: 18px;
  font-weight: bold;
  color: #ffa726; /* Naranja suave */
  text-transform: uppercase;
}

.mission-vision-section p {
  margin: 10px auto;
  max-width: 800px;
  line-height: 1.6;
  color: #ffffff; /* Texto blanco */
  font-size: 16px;
}

.mission-vision-section p:hover {
  color: #ffa726; /* Efecto hover en texto */
  transition: color 0.3s ease;
}


</style>
