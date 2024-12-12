import { createRouter, createWebHistory } from 'vue-router';
import SesionUsuario from '../components/SesionUsuario.vue';
import RegistroUsuario from '../components/RegistroUsuario.vue';
import Home from '../components/Home.vue'; // Cambié '@/' a '../'
import ProductoDetalle from '../components/ProductoDetalle.vue';
import ListaMarcas from '@/components/ListaMarcas.vue';
import CarouselBanner from '@/components/CarouselBanner.vue';

import RedesSociales from '@/components/RedesSociales.vue';
import ServicioTecnico from '@/components/ServicioTecnico.vue';

const routes = [
  { path: '/', redirect: '/home' },
  { 
    path: '/login', 
    component: SesionUsuario,
    beforeEnter: (to, from, next) => {
      const isAuthenticated = !!localStorage.getItem('access_token');
      if (isAuthenticated) {
        next('/home');
      } else {
        next();
      }
    }
  },
  { 
    path: '/registro', 
    component: RegistroUsuario,
    beforeEnter: (to, from, next) => {
      const isAuthenticated = !!localStorage.getItem('access_token');
      if (isAuthenticated) {
        next('/home');
      } else {
        next();
      }
    }
  },
  { 
    path: '/home', 
    component: Home, 
    name: 'HomePage' // Se añade el nombre a la ruta
  },
  { 
    path: '/producto/:id', 
    component: ProductoDetalle, 
    name: 'ProductoDetalle' 
  },

  { 
    path: '/marcas', 
    component: ListaMarcas, // Usar el nuevo nombre del componente
    name: 'ListaMarcas' // Cambiar el nombre para la ruta
  },
  {
    path: '/redes-sociales', // Corregido de 'patch' a 'path'
    component: RedesSociales,
    name: 'RedesSociales'
  },
  {
    path : '/servicio-tecnico',
    component: ServicioTecnico,
    name: 'ServicioTecnico'
  },
  {
    path: '/carousel-banner',
    component: CarouselBanner,
    name: 'CarouselBanner'  
  }


];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
