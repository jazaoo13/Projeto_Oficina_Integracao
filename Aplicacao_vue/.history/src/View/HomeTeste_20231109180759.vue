<template>
    <div>
        <b-button v-b-toggle.sidebar-backdrop><i class="fa fa-bars" aria-hidden="true"></i></b-button>
        <b-sidebar
            id="sidebar-backdrop"
            :backdrop-variant="variant"
            backdrop
            shadow>
            <v-list>
                <template v-for="(item) in items">
                    <v-list-tile :key="item">
                        {{ item }}
                    </v-list-tile>
                </template>
            </v-list>
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