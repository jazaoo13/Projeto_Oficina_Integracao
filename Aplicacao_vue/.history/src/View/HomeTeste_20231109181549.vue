<template>
    <div>
        <b-button v-b-toggle.sidebar-backdrop><i class="fa fa-bars" aria-hidden="true"></i></b-button>
        <b-sidebar
            id="sidebar-backdrop"
            :backdrop-variant="variant"
            backdrop
            shadow>
            <b-button v-for="item in items" v-bind:key="id">{{ item.title }}
            </b-button>
        </b-sidebar>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        items:[
            {id:1, title: 'Cadastro'},
            {id:2, title: 'Estoque'},
            {id:3, title: 'Vendas'},
            {id:4, title: 'Compras'},
            {id:5, title: 'Configurações'}
        ]
      }
    }
  }
</script>