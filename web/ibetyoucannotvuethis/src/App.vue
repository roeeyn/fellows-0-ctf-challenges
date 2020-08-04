<template>
  <div id="app">
    <EntryPointView/>
    <AboutView/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import EntryPointView from "./views/EntryPointView.vue";
import AboutView from "./views/About.vue";

@Component({
  components: {
    EntryPointView,
    AboutView
  }
})
export default class App extends Vue {}
</script>

<style>

</style>
