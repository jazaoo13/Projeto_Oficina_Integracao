<template>
    <div>
        <nav :class="isActive ? 'nav_do_jazao' : 'nav' ">
            <div class="teste">
            </div>
            <div class="sidebar-header" :class="{ 'active': isActive }">
                <a class="logo-wrapper">
                    <img src="@/assets/html5.svg" alt="Logo">
                    <h2 :class="isActive ? 'texto_on' : 'texto_off'">Sua Logo Aqui</h2>
                </a>
                <button class="toggle-btn" @click="toggle()">
                    <img src="../assets/expand.svg" alt="expand button">
                </button>
            </div>

            <div class="sidebar-links" :class="{ 'active': isActive }">
                <a class="link active">
                    <img src="../assets/home.svg" alt="">
                    <span :class="isActive ? 'texto_on' : 'texto_off'">Home</span>
                </a>
                <a class="link" >
                    <img src="../assets/projects.svg" alt="">
                    <span :class="isActive ? 'texto_on' : 'texto_off'">Cadastro</span>
                </a>
                <a class="link">
                    <img src="../assets/estoque.svg" alt="">
                    <span :class="isActive ? 'texto_on' : 'texto_off'">Estoque</span>
                </a>
                <a class="link">
                    <img src="../assets/vendas.png" alt="">
                    <span :class="isActive ? 'texto_on' : 'texto_off'">Vendas</span>
                </a>
            </div>


            <div class="sidebar-bottom" :class="{ 'active': isActive }">
                <div class="sidebar-links">
                    <a class="link">
                        <img src="../assets/settings.svg" alt="">
                        <span :class="isActive ? 'texto_on' : 'texto_off'">Configurações</span>
                    </a>
                </div>

                <div class="user-profile">
                    <div class="user-avatar">
                        <img src="../assets/user.svg" alt="">
                    </div>
                    <div class="user-details hidden">
                        <p class="username">Usuario</p>
                        <p class="user-email">email@gmail.com</p>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: "HomeTeste",
    components: {
        
    },
    data(){
        return {
            isActive: false,
            // imagens:{
            //     imagem1: url=''
            // }
            //array de objetos para os botoes laterais
        }
    },
    methods: {
        Abre_Cadastro() {

        },
        toggle() {
            this.isActive = !this.isActive;
            const toggleBtn = document.querySelector(".toggle-btn");
            toggleBtn.style.transform = this.isActive ? "rotate(180deg)" : "rotate(0deg)";
        },
    },
    mounted() {
    },
}
</script>


<style lang="scss">
// .teste{
//     width: 100%;
//     height: 60px;
//     background-color: white;
//     position: fixed;
//     top: 10px;
// }
body {
    height: 100vh;
    background: radial-gradient(circle at 50% 50%, #192233 20%, #000);
    padding: 0.375rem;
    font-family: Poppins, sans-serif;
    position: relative;
}

button,
a {
    all: unset;
    font: inherit;
    cursor: pointer;
}

nav {
    position: fixed;
    width: 5rem;
    height: calc(100vh - 0.75rem);
    background-color: #ffffff;
    padding: 1rem 0.75rem;
    border-radius: 0.75rem;
    display: flex;
    flex-direction: column;
    transition: width 500ms ease;
}
.nav_do_jazao {
    width: 15rem;
    
}

.sidebar-header,
.sidebar-links {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.sidebar-header {
    margin-bottom: 1.5rem;
}

.logo-wrapper {
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1.25rem;
}

.logo-wrapper>img {
    width: 3.25rem;
    height: 3.25rem;
    background-color: #f4f4f6;
    padding: 0.4rem;
    border-radius: 0.5rem;
}

.sidebar-links {
    flex-direction: column;
    margin-bottom: auto;
    gap: 0.6rem;
    padding-top: 1.5rem;
}

nav>.sidebar-links {
    border-top: 1px solid rgb(211, 211, 211);
}

body.active .sidebar-links,
body.active .sidebar-header,
body.active .user-profile {
    justify-content: start;
    align-items: stretch;
}

.link {
    display: flex;
    padding: 0.6rem;
    border-radius: 0.5rem;
    gap: 1.5rem;
}

.texto_off {
    display: none;
}

.texto_on {
    display: inline;
}

.link:hover,
.link.active:hover {
    background-color: #e4e4e8;
}

.link.active {
    background-color: #f4f4f6;
}

.link>img {
    width: 24px;
    height: 24px;
}

.sidebar-bottom .sidebar-links {
    padding-bottom: 1.5rem;
}

.toggle-btn {
    position: absolute;
    top: 10px;
    right: -50px;
    padding: 0.5rem;
    background-color: #fff;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: transform 0.25s ease;
}

body.active .toggle-btn {
    transform: rotate(180deg);
}

.user-profile {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgb(211, 211, 211);
}

.user-avatar {
    width: 48px;
    height: 48px;
    cursor: pointer;
    transition: scale 0.2s ease;
}

.user-avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.user-avatar:hover {
    scale: 1.1;
}

.user-details {
    align-self: center;
    overflow: hidden;
}

.user-details .username {
    font-size: 0.85rem;
    font-weight: 600;
}

.user-details .user-email {
    font-size: 0.8rem;
}
</style>