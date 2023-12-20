<template>
    <div>
        <b-button v-b-toggle.sidebar-1><i class="fa fa-bars"></i></b-button>
        <b-sidebar
            id="sidebar-1"
            backbox
            shadow>
            <b-button-group vertical size="lg" class="G_Botoes">
                <b-button v-for="(item) in items" v-bind:key="item" class="Botoes">
                    {{ item }}
                </b-button>
                <b-button v-b-toggle.sidebar-1>Fechar</b-button>
            </b-button-group>
        </b-sidebar>
    </div>
</template>

<script>
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