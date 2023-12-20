<template>
    <div>
        <b-button v-b-toggle.sidebar-1><i class="fa fa-bars"></i></b-button>
        <b-sidebar
            id="sidebar-1"
            backbox
            shadow>
            <b-button-group vertical size="lg" class="G_Botoes">
                <ul>
                    <li @click="Abre_Cadastro">Cadastro</li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
                <b-button v-b-toggle.sidebar-1>Fechar</b-button>
            </b-button-group>
        </b-sidebar>
    </div>
</template>

<script>
    import Home from '../components/Home.vue'
    export default {
    name:"HomeTeste",
    components:{
        
    },
    data() {
      return {
            Cadastro:Boolean,
            Estoque:Boolean,
            Vendas:Boolean,
            Compras:Boolean,
            Configurações:Boolean
      }
    },
    methods:{
        Abre_Cadastro(){
            this.Cadastro = true
            console.log(this.Cadastro)
        }
    }
  }
</script>
<style lang="scss">
    header.b-sidebar-header{
        display: none !important;
    }
    .G_Botoes{
        width: 100%;
    }
</style>