<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <EntryPointComponent/>
  </div>
</template>

<script>
// @ is an alias to /src
import EntryPointComponent from '@/components/EntryPointComponent.vue'

export default {
  name: 'Home',
  components: {
    EntryPointComponent
  }
}
</script>
