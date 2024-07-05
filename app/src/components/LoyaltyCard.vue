<template>
  <v-row dense>
    <v-col cols="7">
      <v-radio-group
          label="Card Loyalty"
          inline
          :value="loyalty"
          @input="$emit('update:loyalty', $event.target.value)">
        <v-radio label="Human" value="human" color="blue"/>
        <v-radio label="Machine" value="machine" color="red"/>
        <v-radio label="Outlaw" value="outlaw" color="grey"/>
      </v-radio-group>
    </v-col>
    <v-col cols="5">
      <v-checkbox
          v-if="loyalty != null"
          label="x2"
          :color="loyaltyColour"
          :value="x2"
          @input="$emit('update:x2', $event.target.value)"/>
    </v-col>
  </v-row>
  <v-row dense>
    <v-col>
      <v-img/>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "LoyaltyCard",
  props: {
    loyalty: {
      type: String,
      required: true
    },
    x2: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    loyaltyColour() {
      switch (this.loyalty) {
        case "human":
          return "blue";
        case "machine":
          return "red";
        case "outlaw":
          return "grey";
      }
    }
  }
}
</script>
