import { createRouter, createWebHistory } from 'vue-router';
import SesionUsuario from '../components/SesionUsuario.vue';
import RegistroUsuario from '../components/RegistroUsuario.vue';
import Home from '../components/Home.vue'; // Cambié '@/' a '../'
import ProductoDetalle from '../components/ProductoDetalle.vue'; 

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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
