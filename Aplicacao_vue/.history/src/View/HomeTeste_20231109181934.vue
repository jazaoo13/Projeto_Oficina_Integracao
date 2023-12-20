<template>
    <div>
        <b-button v-b-toggle.sidebar-backdrop><i class="fa fa-bars" aria-hidden="true"></i></b-button>
        <b-sidebar
            id="sidebar-backdrop"
            :backdrop-variant="variant"
            backdrop
            shadow>
            <b-button-group vertical>
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