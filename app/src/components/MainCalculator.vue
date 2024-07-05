<template>
  <v-container fill-height>
    <v-row align="center" justify="center">
      <v-col>
        <h1>Human Punishment Loyalty Calculator</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <LoyaltyCard
            v-model:loyalty="loyaltyLeft"
            v-model:x2="x2Left"/>
      </v-col>
      <v-col>
        <IdentityCard
            v-model:identity="identity"
            v-model:always="always"/>
      </v-col>
      <v-col>
        <LoyaltyCard
            v-model:loyalty="loyaltyRight"
            v-model:x2="x2Right"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import IdentityCard from "@/components/IdentityCard.vue";
import LoyaltyCard from "@/components/LoyaltyCard.vue";

export default {
  name: "MainCalculator",
  components: {
    LoyaltyCard,
    IdentityCard
  },
  data() {
    return {
      loyaltyLeft: null,
      x2Left: false,
      identity: null,
      always: false,
      loyaltyRight: null,
      x2Right: false
    }
  }
}
</script>
