<template>
  <div v-if="banners && banners.length > 0" class="carousel">
    <!-- Banners -->
    <div
      v-for="(banner, index) in banners"
      :key="banner.id"
      :class="['carousel-item', { active: index === activeBanner }]"
    >
      <img
        :src="getFullImageUrl(banner.imagen_url)"
        :alt="banner.titulo"
        class="banner-image"
      />
    </div>
    
    <!-- Flechas de navegación -->
    <button class="carousel-arrow left" @click="prevBanner">‹</button>
    <button class="carousel-arrow right" @click="nextBanner">›</button>
    
    <!-- Indicadores -->
    <div class="carousel-indicators">
      <span
        v-for="(banner, index) in banners"
        :key="`indicator-${index}`"
        :class="{ active: index === activeBanner }"
        @click="setBanner(index)"
      ></span>
    </div>
  </div>
  <div v-else>
    <p>Cargando banners...</p>
  </div>
</template>

<script>
export default {
  name: "CarouselBanner",
  props: {
    banners: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      activeBanner: 0,
      intervalId: null,
    };
  },
  mounted() {
    this.startCarousel();
  },
  beforeUnmount() {
    this.stopCarousel();
  },
  methods: {
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
  },
};
</script>

<style scoped>
.carousel {
  position: relative;
  width: 851px;
  height: 315px;
  margin: 20px auto;
  overflow: hidden;
  border-radius: 8px;
  transition: transform 0.5s ease-in-out; /* Transición para el contenedor */
}

.carousel:hover {
  transform: scale(1.05); /* Aumenta el tamaño del contenedor principal */
}

.carousel-item {
  position: relative; /* Cambiado a relative para permitir escalado completo */
  display: none;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 0.5s ease-in-out;
}

.carousel-item.active {
  display: block;
  opacity: 1;
}

.banner-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  gap: 5px;
}

.carousel-indicators span {
  width: 10px;
  height: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  cursor: pointer;
}

.carousel-indicators .active {
  background-color: #fff;
}
</style>
