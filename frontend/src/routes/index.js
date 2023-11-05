import { createRouter, createWebHistory} from 'vue-router';

// import Home from '../views/Home.vue';
// import About from '../views/About.vue';
// import Institutes from '../views/Institutes.vue';

const Home = () => import('../views/Home.vue');
const About = () => import('../views/About.vue');
const Institutes = () => import('../views/Institutes.vue');
const RegisterView = () => import('../views/Register.vue');
const LoginView = () => import('../views/Login.vue');
const InstituteDetail = () => import('../views/InstituteDetail.vue');
const DepartmentDetail = () => import('../views/DepartmentDetail.vue');
const TeacherDetail = () => import('../views/TeacherDetail.vue');
const TeacherListSearch = () => import('../views/TeachersListSearch.vue');
const ModerTeacherList = () => import('../views/ModerTeacherList.vue');
const ModerTeacherDetail = () => import('../views/ModerTeacherDetail.vue');
const AddTeacher = () => import('../views/AddTeacher.vue');

const routes = [
    { path : '/', component:Home, name: 'home'},
    { path : '/about', component:About, name: 'about'},
    { path : '/institutes', component:Institutes, name: 'institutes'},
    { path : '/institutes/:id', component:InstituteDetail, name: 'institute-detail'},
    { path : '/register', component:RegisterView, name: 'register'},
    { path : '/login', component:LoginView, name: 'login'},
    { path : '/institutes/:instituteId/department/:departmentId', component:DepartmentDetail, name:'department-detail'},
    { path : '/institutes/:instituteId/teachers/:teacherId', component:TeacherDetail, name:'teacher-detail'},
    {path : '/teachers', component:TeacherListSearch, name:'all-teachers'},
    {path : '/moderation', component:ModerTeacherList, name:'moder-list'},
    {path : '/moderation/:teacherId',component:ModerTeacherDetail, name:'moder-detail'},
    {path : '/add_teacher', component:AddTeacher}
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes
});

export default router;