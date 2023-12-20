<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-1 p-0 m-0">
                <div class="button-wraper">
                    <b-button v-b-toggle.sidebar-1 style="border-radius: 20px; margin-top: 5px;"><i class="fa fa-bars"></i></b-button>
                </div>
            </div>
            
            <div class="col-11">
                <b-sidebar id="sidebar-1">
                    <b-button-group vertical size="lg" class="G_Botoes">
                        <b-button pill v-for="(item) in items" v-bind:key="item" class="Botoes">
                            {{ item.name }}
                        </b-button>
                        <b-button pill v-b-toggle.sidebar-1>Fechar</b-button>
                    </b-button-group>
                </b-sidebar>
                <div class="TopBar" style="background-color:#6c757d;">
                    <div class="Icone">
                        <i class="fa fa-beer">

                        </i>
                    </div>
                    <div class="TopBar2">
                        <h2>ESTOQUE</h2>
                    </div>
                </div>
            </div>
        </div>
        
    </div>
</template>

<script>
    export default {
        data(){
        return {
            isActive: false,
            // imagens:{
            //     imagem1: url=''
            // }
            //array de objetos para os botoes laterais
        }
    },
}

</script>

<style lang="scss">
header.b-sidebar-header {
    display: none !important;
}

.shadow {
    box-shadow: none !important;
}

.G_Botoes {
    width: 100%;
}

.Botoes {
    margin: 8px 0px;
}

#sidebar-1 {
    height: fit-content;
}

.bg_light {
    background-color: transparent;
}

.button-wraper {
    width: fit-content;
    display: flex;
    flex-direction: column;
    background-color: #6c757d;
    height: 100vh;
    border-radius: 20px;
    margin-left: 3px;
    width: 50px;
}</style>