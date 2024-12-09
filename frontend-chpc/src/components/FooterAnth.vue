<template>
    <footer class="footer-container">
      <div class="footer-content">
        <div class="footer-section">
          <h4>Sobre Nosotros</h4>
          <p>
            Somos una tienda comprometida con ofrecer los mejores productos y la mejor experiencia de compra en línea.
          </p>
        </div>
        <div class="footer-section">
          <h4>Enlaces Rápidos</h4>
          <ul>
            <li><a href="#">Inicio</a></li>
            <li><a href="#">Productos</a></li>
            <li><a href="#">Contacto</a></li>
            <li><a href="#">Términos y Condiciones</a></li>
          </ul>
        </div>
        <div class="footer-section">
          <h4>Contáctanos</h4>
          <p>Email: soporte@tienda.com</p>
          <p>Teléfono: +1 234 567 890</p>
          <p>Dirección: 123 Calle Principal, Ciudad</p>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 Tienda. Todos los derechos reservados.</p>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "FooterAnth",
  };
  </script>
  
  <style scoped>
  .footer-container {
    background-color: #003366;
    color: white;
    padding: 20px;
    text-align: center;
  }
  
  .footer-content {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }
  
  .footer-section {
    flex: 1;
    min-width: 200px;
    margin: 10px;
  }
  
  .footer-section h4 {
    margin-bottom: 10px;
    font-size: 16px;
    font-weight: bold;
  }
  
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section ul li {
    margin: 5px 0;
  }
  
  .footer-section ul li a {
    color: white;
    text-decoration: none;
  }
  
  .footer-section ul li a:hover {
    text-decoration: underline;
  }
  
  .footer-bottom {
    border-top: 1px solid #fff;
    padding-top: 10px;
    font-size: 14px;
  }
  </style>
  