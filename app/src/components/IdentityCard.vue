<template>
  <v-row dense>
    <v-col cols="7">
      <v-radio-group
          label="Identity Card Loyalty"
          inline
          :value="identity"
          @input="$emit('update:identity', $event.target.value)">
        <v-radio label="Human" value="human" color="blue"/>
        <v-radio label="Machine" value="machine" color="red"/>
        <v-radio label="Outlaw" value="outlaw" color="grey"/>
      </v-radio-group>
    </v-col>
    <v-col cols="5">
      <v-checkbox
          v-if="identity !== null"
          :label="alwaysLabel"
          :color="alwaysColour"
          :value="always"
          @input="$emit('update:always', $event.target.value)"/>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "IdentityCard",
  props: {
    identity: {
      type: String,
      required: true
    },
    always: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    alwaysLabel() {
      switch (this.identity) {
        case "human":
          return "Always Human";
        case "machine":
          return "Always Machine";
        case "outlaw":
          return "Always Outlaw";
      }
      return null;
    },
    alwaysColour() {
      switch (this.identity) {
        case "human":
          return "blue";
        case "machine":
          return "red";
        case "outlaw":
          return "grey";
      }
      return null;
    }
  }
}
</script>
