<template>
  <v-container fill-height>
    <v-row align="center" justify="center">
      <v-col>
        <h1>Human Punishment Loyalty Calculator</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <LoyaltyCard />
      </v-col>
      <v-col>
        <IdentityCard />
      </v-col>
      <v-col>
        <LoyaltyCard />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import IdentityCard from "@/components/IdentityCard.vue";
import LoyaltyCard from "@/components/LoyaltyCard.vue";

export default {
  name: "MainCalculator",
  components: {LoyaltyCard, IdentityCard}
}
</script>

<style scoped>

</style>