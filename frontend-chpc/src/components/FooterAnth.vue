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
 /* Estilos relacionados con el header */
.header {
  font-family: 'Roboto', sans-serif;
}

.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #000; /* Negro en lugar de blanco */
  padding: 10px 20px;
}

.logo img {
  width: 100px;
  height: 70px;
  object-fit: cover;
  border-radius: 5px;
}

.search-bar {
  flex: 1;
  display: flex;
  align-items: center;
  margin: 0 20px;
}

.search-bar input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd; /* Tonalidad gris suave */
  border-radius: 5px 0 0 5px;
}

.search-bar button {
  padding: 10px 20px;
  background-color: #ffa726; /* Naranja suave */
  border: none;
  color: white;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  transition: background 0.3s ease;
}

.search-bar button:hover {
  background-color: #fb8c00; /* Tonalidad más oscura */
}

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

.social-icon {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

.footer-bottom {
  border-top: 1px solid #ffa726; /* Naranja suave */
  padding-top: 15px;
  font-size: 14px;
  color: #ffa726;
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

  </style>
