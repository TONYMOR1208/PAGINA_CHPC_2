<template>
  <div class="carousel-banner">
    <div v-if="banners.length" class="carousel">
      <div
        v-for="(banner, index) in banners"
        :key="banner.id"
        class="carousel-item"
        :class="{ active: activeBanner === index }"
      >
        <img
          :src="getFullImageUrl(banner.imagen_url)"
          :alt="banner.titulo"
          class="banner-image"
          @load="handleImageLoad"
        />
      </div>

      <!-- Controles del carrusel -->
      <button class="carousel-arrow left" @click="prevBanner">&#10094;</button>
      <button class="carousel-arrow right" @click="nextBanner">&#10095;</button>

      <!-- Indicadores -->
      <div class="carousel-indicators">
        <span
          v-for="(banner, index) in banners"
          :key="index"
          :class="{ active: activeBanner === index }"
          @click="setBanner(index)"
        ></span>
      </div>
    </div>

    <div v-else class="no-banners">
      <p>No hay banners disponibles.</p>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "CarouselBanner",
  data() {
    return {
      banners: [],
      activeBanner: 0,
      intervalId: null,
    };
  },
  async created() {
    await this.fetchBanners();
    this.startCarousel();
  },
  beforeUnmount() {
    this.stopCarousel();
  },
  methods: {
    async fetchBanners() {
      try {
        const response = await axios.get("http://localhost:5000/tienda/banners");
        this.banners = response.data.data;
      } catch (error) {
        console.error("Error al obtener los banners:", error);
      }
    },
    startCarousel() {
      if (this.banners && this.banners.length > 0) {
        this.intervalId = setInterval(() => {
          this.nextBanner();
        }, 6000);
      }
    },
    stopCarousel() {
      if (this.intervalId) clearInterval(this.intervalId);
    },
    getFullImageUrl(relativeUrl) {
      return `http://localhost:5000${relativeUrl}`;
    },
    prevBanner() {
      this.activeBanner =
        (this.activeBanner - 1 + this.banners.length) % this.banners.length;
    },
    nextBanner() {
      this.activeBanner = (this.activeBanner + 1) % this.banners.length;
    },
    setBanner(index) {
      this.activeBanner = index;
    },
    handleImageLoad(event) {
      event.target.classList.add("loaded"); // Añade la clase `loaded` al cargar la imagen
    },
  },
};
</script>

<style>

.carousel {
  position: relative;
  width: 1024px; /* Ancho aumentado */
  height: 400px; /* Altura aumentada */
  margin: 20px auto;
  overflow: hidden;
  border-radius: 12px; /* Esquinas más redondeadas */
}

.carousel:hover {
  transform: scale(1.05); /* Efecto de agrandamiento al pasar el mouse */
  transition: transform 0.5s ease-in-out;
}

.carousel {
  position: relative;
  width: 851px; /* Ancho de la imagen */
  height: 315px; /* Altura de la imagen */
  margin: 20px auto;
  overflow: hidden;
  border-radius: 12px; /* Bordes redondeados */
}

.carousel-item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transform: scale(0.9);
  transition: transform 1s ease-in-out, opacity 1s ease-in-out;
}

.carousel-item.active {
  opacity: 1;
  z-index: 2;
  transform: scale(1);
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 0.8s ease-in-out, transform 0.8s ease-in-out;
}

.banner-image.loaded {
  opacity: 1;
}

.carousel-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 24px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
}

.carousel-arrow.left {
  left: 10px;
}

.carousel-arrow.right {
  right: 10px;
}

.carousel-arrow:hover {
  background-color: rgba(0, 0, 0, 0.7);
}

.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 8px;
}

.carousel-indicators span {
  width: 12px;
  height: 12px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  cursor: pointer;
}

.carousel-indicators .active {
  background-color: #fff;
}

.no-banners {
  text-align: center;
  color: #888;
  font-size: 1.2rem;
  margin-top: 2rem;
}


</style>
