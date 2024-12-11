import { createRouter, createWebHistory } from 'vue-router';
import SesionUsuario from '../components/SesionUsuario.vue';
import RegistroUsuario from '../components/RegistroUsuario.vue';
import Home from '../components/Home.vue'; // Cambié '@/' a '../'
import ProductoDetalle from '../components/ProductoDetalle.vue';
import ListaMarcas from '@/components/ListaMarcas.vue';
import ReseñasProductos from '../components/ReseñasProductos.vue';


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
  },
  { 
    path: '/marcas', 
    component: ListaMarcas, // Usar el nuevo nombre del componente
    name: 'ListaMarcas' // Cambiar el nombre para la ruta
  }

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
