<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-1 p-0 m-0">
                <div class="button-wraper">
                    <b-button v-b-toggle.sidebar-1 style="border-radius: 20px; margin-top: 20px;"><i class="fa fa-bars"></i></b-button>
                </div>
            </div>
            <div class="col-11">
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
        </div>
        
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
    .shadow{
        box-shadow: none !important;
    }
    .G_Botoes{
        width: 100%;
    }
    .Botoes{
        margin: 8px 0px;
    }
    #sidebar-1{
        height: fit-content;
    }
    .bg_light{
        background-color: transparent;
    }
    .button-wraper{
        width: fit-content;
        display: flex;
        flex-direction: column;
        background-color: #6c757d;
        height: 100vh;
        border-radius: 20px;
    }
</style>