<template>
  <v-app>
    <v-main>
      <ApiConsumer/>
    </v-main>
  </v-app>
</template>

<script>
import ApiConsumer from './components/ApiConsumer.vue'

export default {
  name: 'App',

  components: {
    ApiConsumer
  },

  data: () => ({
    //
  }),
}
</script>
