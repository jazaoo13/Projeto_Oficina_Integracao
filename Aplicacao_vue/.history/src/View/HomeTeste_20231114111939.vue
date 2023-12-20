<template>
    <div>
        <nav :class="{ 'isActive': isActive }">
            <div class="teste">
            </div>
            <div class="sidebar-header" :class="{ 'isActive': isActive }">
                <a class="logo-wrapper">
                    <img src="@/assets/html5.svg" alt="Logo">
                    <h2 :class="{'isActive': isActive }">Sua Logo Aqui</h2>
                </a>
                <button class="toggle-btn" @click="toggle()">
                    <img src="../assets/expand.svg" alt="expand button">
                </button>
            </div>

            <div class="sidebar-links" :class="{ 'isActive': isActive }">
                <a class="link active">
                    <img src="../assets/home.svg" alt="">
                    <span :class="{ 'isActive': isActive }">Home</span>
                </a>
                <a class="link" >
                    <img src="../assets/projects.svg" alt="">
                    <span :class="{ 'isActive': isActive }">Cadastro</span>
                </a>
                <a class="link">
                    <img src="../assets/estoque.svg" alt="">
                    <span :class="{ 'isActive': isActive }">Estoque</span>
                </a>
                <a class="link">
                    <img src="../assets/vendas.png" alt="">
                    <span :class="{ 'isActive': isActive }">Vendas</span>
                </a>
            </div>


            <div class="sidebar-bottom" :class="{ 'active': isActive }">
                <div class="sidebar-links">
                    <a class="link">
                        <img src="../assets/settings.svg" alt="">
                        <span :class="{ 'isActive': isActive }">Configurações</span>
                    </a>
                </div>

                <div class="user-profile" :class="{ 'isActive': isActive }">
                    <div class="user-avatar">
                        <img src="../assets/user.svg" alt="">
                    </div>
                    <div class="user-details">
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
    &.isActive{
        width:15rem;
    }
}
h2{
    display: none;
    text-decoration: none;
    color: inherit;
    &.isActive{
        display:inline;
    }
}
.sidebar-header,
.sidebar-links {
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    &.isActive{
        justify-content: start;
        align-items: stretch;
    }
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

.link {
    display: flex;
    padding: 0.6rem;
    border-radius: 0.5rem;
    gap: 1.5rem;
}
span{
    display: none;
    &.isActive{
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

.user-profile {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1.5rem;
    padding-top: 1.5rem;
    border-top: 1px solid rgb(211, 211, 211);
    &.isActive{
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
    .username {
        font-size: 0.85rem;
        font-weight: 600;
    }
    .user-email {
        font-size: 0.8rem;
    }
    // &.isActive{
        
    // }

}
</style>