<template>
  <v-radio-group v-model="identityLoyalty" label="Identity Card Loyalty" inline>
    <v-radio label="Human" value="human" color="blue" />
    <v-radio label="Machine" value="machine" color="red" />
    <v-radio label="Outlaw" value="outlaw" color="grey" />
  </v-radio-group>
  <v-checkbox v-if="identityLoyalty !== null" :label="alwaysLabel()" :color="alwaysColour()" />
</template>

<script>
export default {
  name: "IdentityCard",
  data() {
    return {
      identityLoyalty: null
    }
  },
  methods: {
    alwaysLabel() {
      if (this.identityLoyalty === "human")
        return "Always Human";
      else if (this.identityLoyalty === "machine")
        return "Always Machine";
      else if (this.identityLoyalty === "outlaw")
        return "Always Outlaw";
      return null;
    },
    alwaysColour() {
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