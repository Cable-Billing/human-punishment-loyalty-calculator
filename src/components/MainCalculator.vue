<template>
  <v-container fill-height>
    <v-row align="center" justify="center">
      <v-col>
        <h1>Human Punishment Loyalty Calculator</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <LoyaltyCard @selection-changed="leftLoyaltyChanged" />
      </v-col>
      <v-col>
        <IdentityCard @selection-changed="identityChanged" />
      </v-col>
      <v-col>
        <LoyaltyCard @selection-changed="rightLoyaltyChanged" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import IdentityCard from "@/components/IdentityCard.vue";
import LoyaltyCard from "@/components/LoyaltyCard.vue";

export default {
  name: "MainCalculator",
  components: {LoyaltyCard, IdentityCard},
  methods: {
    identityChanged(params) {
      console.log(params);
    },
    leftLoyaltyChanged(params) {
      console.log(params);
    },
    rightLoyaltyChanged(params) {
      console.log(params);
    }
  }
}
</script>

<style scoped>

</style>