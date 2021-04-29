<template>
  <q-page class="row flex content-start justify-center q-mt-md">
    <div class="row flex flex-center">
      <p class="text-body1 col-12 text-center q-px-md q-pt-md">
        {{ $t("training.pageDescription") }}
      </p>


    </div>
  </q-page>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "TrainingPage",
  data() {
    return {
      interval: 0,
    };
  },
  mounted() {
    // This interval increments the query param every 60 seconds causing an image refresh
    setInterval(() => {
      this.interval++;
    }, 60000);
  },
  computed: {
  },
};
</script>

<style scoped>
.row {
  width: 100%;
  max-width: 100vw;
}
</style>
