import { createRouter, createWebHistory } from 'vue-router';
import SesionUsuario from '../components/SesionUsuario.vue';
import RegistroUsuario from '../components/RegistroUsuario.vue';
import Home from '../components/Home.vue'; // Cambié '@/' a '../'
import ProductoDetalle from '../components/ProductoDetalle.vue';
import ReseñasProductos from '../components/ReseñasProductos.vue'; // Importa el nuevo componente

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
    path: '/producto/:id/reseñas', 
    component: ReseñasProductos, 
    name: 'ReseñasProductos' 
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
