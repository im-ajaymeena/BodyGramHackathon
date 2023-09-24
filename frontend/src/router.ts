import Vue from 'vue';
import VueRouter from 'vue-router';
import ResultChart from './components/ResultChart.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/result-chart',
    name: 'result-chart',
    component: ResultChart,
    props: true, // Allows passing route params as props
  },
];

const router = new VueRouter({
  routes,
});

export default router;
