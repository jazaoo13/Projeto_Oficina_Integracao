<template>
    <aside :class="`${isActive ? 'isActive' : 'notActive'}`">
        <div class="logo">
            <img src="../assets/html5.svg" alt="HTML5">
        </div>
        <div class="menu-toggle-wrap">
            <button class="menu-toggle" @click="toggle()">
                <span class="material-icons">keyboard_double_arrow_right</span>
            </button>

        </div>

    </aside>
</template>

<script>
export default {
    name: 'teste_component',
    data() {
        return {
            isActive: false
        }
    },
    methods: {
        toggle() {
            this.isActive = !this.isActive;
        }
    },
}
</script>

<style lang="scss" scoped>
aside {
    display: Flex;
    flex-direction: column;
    //width: 5vw; // vw = View Width
    min-height: 100vh; // vh = view heigt
    overflow: hidden;
    padding: 1rem;

    background-color: darkcyan;
    color: white;

    transition: 0.2s ease-out;

    .logo {
        margin-bottom: 1rem;

        img {
            width: 2rem;
        }
    }
    &.notActive {
        width: 40%;
    }

    &.isActive {
        width: 4rem;
    }
}

// @media(max-width: 768px) {
//     .notActive {
//         width: 50px;
//     }
// }
</style>