<template>
    <div class="text-start">
        <b-button v-b-toggle.sidebar-1><i class="fa fa-bars"></i></b-button>
        <b-sidebar
            id="sidebar-1"
            backbox
            shadow>
            <b-button-group vertical size="lg" class="G_Botoes">
                <b-button pill v-for="(item) in items" v-bind:key="item" class="Botoes">
                    {{ item.name }}
                </b-button>
                <b-button pill v-b-toggle.sidebar-1>Fechar</b-button>
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
            items:[
            {name:'Cadastro', type:true},
            {name:'Estoque', type:true},
            {name:'Vendas', type:true},
            {name:'Compras', type:true},
            {name:'Configurações', type:true}]
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
    #sidebar-1{
        height: fit-content;
    }
</style>