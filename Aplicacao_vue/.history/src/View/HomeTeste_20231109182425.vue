<template>
    <div>
        <b-button v-b-toggle.sidebar-backdrop><i class="fa fa-bars"></i></b-button>
        <b-sidebar
            id="sidebar-backdrop"
            :backdrop-variant="variant"
            backdrop
            width="170px"
            shadow>
            <b-button-group vertical size="lg">
                <b-button v-for="(item) in items" v-bind:key="item">
                    {{ item }}
                </b-button>
            </b-button-group>
            
        </b-sidebar>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        items:[
            'Cadastro',
            'Estoque',
            'Vendas',
            'Compras',
            'Configurações'
        ]
      }
    }
  }
</script>