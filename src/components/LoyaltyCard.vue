<template>
  <v-radio-group v-model="identityLoyalty" label="Identity Card Loyalty" inline>
    <v-radio label="Human" value="human" color="blue" />
    <v-radio label="Machine" value="machine" color="red" />
    <v-radio label="Outlaw" value="outlaw" color="grey" />
  </v-radio-group>
  <v-checkbox v-if="identityLoyalty !== null" label="X2" :color="identityColour()" />
</template>

<script>
export default {
  name: "LoyaltyCard",
  data() {
    return {
      identityLoyalty: null
    }
  },
  methods: {
    identityColour() {
      if (this.identityLoyalty === "human")
        return "blue";
      else if (this.identityLoyalty === "machine")
        return "red";
      else if (this.identityLoyalty === "outlaw")
        return "grey";
      return null;
    }
  }
}
</script>

<style scoped>

</style>