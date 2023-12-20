<template>
        <div class="sideBar" :class="{ 'isActive': this.$store.state.isActive }">
            <div class="sidebar-header" :class="{ 'isActive': this.$store.state.isActive }">
                <a class="logo-wrapper">
                    <img src="@/assets/logo_esquina.png" alt="Logo" :class="{ 'isActive': this.$store.state.isActive }">
                    <h2 :class="{ 'isActive': this.$store.state.isActive }">Bar da Esquina</h2>
                </a>
                <!-- <button class="toggle-btn" @click="toggle()">
                    <img src="../assets/expand.svg" alt="expand button">
                </button> -->
            </div>

            <div class="sidebar-links" :class="{ 'isActive': this.$store.state.isActive }">
                <a class="link active">
                    <img src="../assets/home.svg" alt="">
                    <span :class="{ 'isActive': this.$store.state.isActive }">Home</span>
                </a>
                <a class="link">
                    <img src="../assets/projects.svg" alt="">
                    <span :class="{ 'isActive': this.$store.state.isActive }">Cadastro</span>
                </a>
                <a class="link">
                    <img src="../assets/estoque.svg" alt="">
                    <span :class="{ 'isActive': this.$store.state.isActive }">Estoque</span>
                </a>
                <a class="link">
                    <img src="../assets/vendas.png" alt="">
                    <span :class="{ 'isActive': this.$store.state.isActive }">Vendas</span>
                </a>
            </div>


            <div class="sidebar-bottom" :class="{ 'isActive': this.$store.state.isActive }">
                <div class="sidebar-links" :class="{ 'isActive': this.$store.state.isActive }">
                    <a class="link">
                        <img src="../assets/settings.svg" alt="">
                        <span :class="{ 'isActive': this.$store.state.isActive }">Configurações</span>
                    </a>
                </div>

                <div class="user-profile" :class="{ 'isActive': this.$store.state.isActive }">
                    <div class="user-avatar">
                        <img src="../assets/user.svg" alt="">
                    </div>
                    <div class="user-details" :class="{ 'isActive': this.$store.state.isActive }">
                        <p class="username">Usuario</p>
                        <p class="user-email">email@gmail.com</p>
                    </div>
                </div>
            </div>
        </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
    name: "SiderBar",
    components: {
    },
    data() {
        return {
            //isActive:false,
            // imagens:{
            //     imagem1: url=''
            // }
            //array de objetos para os botoes laterais
        }
    },
    methods: {
        Abre_Cadastro() {

        },
        computed: {
            ...mapState(['isActive'])
            
        },
        toggle() {
            this.$store.commit('setIsActive');

            const toggleBtn = document.querySelector(".toggle-btn");
            toggleBtn.style.transform = this.$store.state.isActive ? "rotate(180deg)" : "rotate(0deg)";
        },
    },
    mounted() {

    },
}
</script>


<style lang="scss">
*,
*::before,
*::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

button,
a {
    all: unset;
    font: inherit;
    cursor: pointer;
    text-decoration: none !important;
}

a:hover {
    color: inherit !important;
}

.sideBar {
    width: 5rem;
    background-color: #ffffff;
    //padding: 1rem 0.75rem;
    border-radius: 0.75rem;
    display: flex;
    flex-direction: column;
    transition: width 500ms ease;
    &.isActive {
        width: 15rem;
    }
}

h2 {
    display: none;

    &.isActive {
        display: inline;
        font-size: 1.5rem;
    }
}

.sidebar-header,
.sidebar-links {
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    flex-direction: column;
    &.isActive {
        justify-content: start;
        align-items: stretch;
    }
}
.sidebar-links {
    flex-direction: column;
    margin-bottom: auto;
    gap: 0.6rem;
    padding-bottom: 1.5rem;
    padding-top: 1.5rem;
}
.sidebar-header {
    &.isActive {
        justify-content: start;
        align-items: stretch;
    }
}

.logo-wrapper {
    display: flex;
    justify-content: start;
    align-items: center;
    gap: 1.25rem;
    text-decoration: none !important;
}

a.logo-wrapper:hover {
    color: inherit !important;
}

.logo-wrapper>img {
    width: 60px;
    height: 60px;
    background-color: #f4f4f6;
    padding: 0.4rem;
    border-radius: 0.5rem;

    &.isActive {
        width: 100px;
        height: 100px;
    }
}

.sideBar.sidebar-links {
    border-top: 1px solid rgb(211, 211, 211);
}

.link {
    display: flex;
    padding: 0.6rem;
    border-radius: 0.5rem;
    gap: 1.5rem;
}

span {
    display: none;

    &.isActive {
        display: inline;
    }
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
    padding-top:5px;
    transition: transform 0.25s ease;
}
.toggle-btn:hover{
    background-color: antiquewhite;
}

.user-profile {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgb(211, 211, 211);

    &.isActive {
        justify-content: start;
        align-items: stretch;
    }
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
    display: none;

    .username {
        font-size: 0.85rem;
        font-weight: 600;
    }

    .user-email {
        font-size: 0.8rem;
    }

    &.isActive {
        display: inline;
    }

}</style>