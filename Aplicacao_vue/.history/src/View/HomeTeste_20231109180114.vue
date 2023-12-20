<template>
    <div>
        <b-button v-b-toggle.sidebar-backdrop><i class="fa fa-bars" aria-hidden="true"></i></b-button>
        <b-sidebar
            id="sidebar-backdrop"
            :backdrop-variant="variant"
            backdrop
            shadow>

        </b-sidebar>
    </div>
</template>

<script>
  export default {
    data() {
      return {
        variant: 'dark',
        variants: [
          'transparent',
          'white',
          'light',
          'dark',
          'primary',
          'secondary',
          'success',
          'danger',
          'warning',
          'info',
        ]
      }
    }
  }
</script>