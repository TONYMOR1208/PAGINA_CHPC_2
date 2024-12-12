<template>
  <footer class="footer-container">
    <div class="footer-content">
      <div class="footer-section">
        <h4>Sobre Nosotros</h4>
        <p>
          Tenemos todo en Informática: Portátiles, Computadoras de escritorio, Impresoras, Tablets, Accesorios, Cámaras de seguridad, solo en CHCP Tecnología.
        </p>
        <p>Haz CLICK, lo tenemos...!</p>
      </div>
      <div class="footer-section">
        <h4>Contáctanos</h4>
        <p>Email: clickhereventas3@gmail.com</p>
        <p>Teléfono: 099 592 4867</p>
        <p>Dirección: Calle 12 Avenida 20 Esquina, Manta, Ecuador</p>
      </div>
      <div class="footer-section">
        <h4>Redes Sociales</h4>
        <ul class="social-media">
          <li v-for="red in redesSociales" :key="red.nombre">
            <a :href="red.url" target="_blank">
              <img :src="red.icono" :alt="red.nombre" class="social-icon" /> {{ red.nombre }}
            </a>
          </li>
        </ul>
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
    };
  },
};
</script>

<style scoped>
.footer-container {
  background: linear-gradient(135deg, #003366, #00509e);
  color: white;
  padding: 30px;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.footer-content {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-bottom: 30px;
  gap: 20px;
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
  color: #ffcc00;
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
  color: #ffcc00;
  text-decoration: none;
  display: flex;
  align-items: center;
  transition: color 0.3s;
}

.footer-section ul li a:hover {
  color: #ffffff;
}

.social-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.footer-bottom {
  border-top: 1px solid #ffcc00;
  padding-top: 15px;
  font-size: 14px;
  color: #ffcc00;
}
</style>