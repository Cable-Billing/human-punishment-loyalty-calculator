<template>
  <v-row dense>
    <v-col cols="7">
      <v-radio-group v-model="identityLoyalty" label="Identity Card Loyalty" inline>
        <v-radio label="Human" value="human" color="blue"/>
        <v-radio label="Machine" value="machine" color="red"/>
        <v-radio label="Outlaw" value="outlaw" color="grey"/>
      </v-radio-group>
    </v-col>
    <v-col cols="5">
      <v-checkbox v-if="identityLoyalty !== null" label="X2" :color="identityColour()" v-model="x2" />
    </v-col>
  </v-row>
  <v-row dense>
    <v-col>
      <v-img />
    </v-col>
  </v-row>
</template>

<script>
import path from "path";

export default {
  name: "LoyaltyCard",
  data() {
    return {
      identityLoyalty: null,
      x2: false
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
    },
    selectionChanged() {
      this.$emit("selection-changed", [this.identityLoyalty, this.x2]);
    },
    loyaltyCardImagePath() {
      //require('../assets/loyalty-cards.png')
      if (this.identityLoyalty === "human")
        return path.join(__dirname, 'src', 'assets', 'loyalty-cards.png');
      else if (this.identityLoyalty === "machine")
        return path.join(__dirname, 'src', 'assets', 'loyalty-cards.png');
      else if (this.identityLoyalty === "outlaw")
        return path.join(__dirname, 'src', 'assets', 'loyalty-cards.png');
    }
  },
  watch: {
    identityLoyalty() {
      this.selectionChanged();
    },
    x2() {
      this.selectionChanged();
    }
  }
}
</script>

<style scoped>
.loyalty-card {
  width: 450px;
  height: 630px;
  mask-image: ;
}
</style>