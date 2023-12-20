<template>
    <aside :class="`${isActive && 'isActive'}`">
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
        name:'teste_component',
        data(){
            return{
                isActive:false
            }
        },
        methods:{
            toggle(){
                this.isActive = !this.isActive;
            }
        },
    }
</script>

<style lang="scss" scoped>
aside{
    display:Flex;
    flex-direction: column;
    width: 4rem;
    min-height: 100vh;
    overflow: hidden;
    padding:1rem;

    background-color: darkcyan;
    color: white;
    
    transition: 0.2s ease-out;

    .logo{
        margin-bottom: 1rem;

        img{
            width: 2rem;
        }
    }
    @media(max-width: 768px){
        position:fixed;
        z-index: 99;
    }
    .isActive{
        width: 100vh !important;
        .menu-toggle-wrap {
			top: -3rem;
			
			.menu-toggle {
				transform: rotate(-180deg);
			}
		}

		h3, .button .text {
			opacity: 1;
		}

		.button {
			.material-icons {
				margin-right: 1rem;
			}
		}

		.footer {
			opacity: 0;
		}
    }
    
}
</style>