<template>
  <v-container fill-height>
    <v-row align="center" justify="center">
      <v-col>
        <h1>Human Punishment Loyalty Calculator</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>

      </v-col>
      <v-col>
        <Identity />
      </v-col>
      <v-col>

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Identity from "@/components/Identity.vue";

export default {
  name: "MainCalculator",
  components: {Identity}
}
</script>

<style scoped>

</style>