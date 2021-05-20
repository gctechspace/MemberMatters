<template>
  <q-page class="content-start justify-center q-mt-md">
    <q-tabs v-model="tab" class="text-primary">
      <q-tab key="home" name="home" :icon="icons.info" label="Getting started" />
      <q-tab v-for="device in devices"  v-bind:key="device.pk" :name="device.pk" :icon="icons.tools" :label="device.fields.name" />
    </q-tabs>
    <q-tab-panels v-model="tab" animated>

      <q-tab-panel key="`welcome-tab`" name="home">
      <div class="text-h6">Welcome to the training page</div>
      Here you will find a variety of quizzes to prepare to be inducted in all our machines and devices
      </q-tab-panel>
      
      <q-tab-panel v-for="device in devices" v-bind:key="`${device.pk}-tab`" :name="device.pk">
      <div class="text-h6">{{device.fields.name}}</div>
      <training-form :formItems="device.fields.data.data" :name="device.fields.name" :id="device.pk" />
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script>
import icons from "../icons"
import TrainingForm from "../components/TrainingForm"
import { QMarkdown } from '@quasar/quasar-ui-qmarkdown'
export default {
  name: "TrainingPage",
  components: { TrainingForm, QMarkdown},
  data() {
    return {
      interval: 0,
      failed: false,
      error: false,
      errorExists: false,
      complete: false,
      buttonLoading: false,
      isPwd: true,
      form: {
        22: null,
        printer:null,
        accept:null  
      },
      tab:"home",
      devices:[],
      input: "My first line  \n My second line  \nMy third line  \nMy last line"
    };
  },
  mounted() {
    // This interval increments the query param every 60 seconds causing an image refresh
    setInterval(() => {
      this.interval++;
    }, 60000),
    this.getQuizzes()
  },
  methods:{
    onSubmit() {
      console.log(this.form)
    },
    onReset() {
      console.log(this.form)
    },
    getQuizzes() {
    this.$axios
      .get("/api/quiz/")
      .then((response) => {
        this.devices = response.data
        console.log(response.data)
      })
      .catch((e) => {
        console.log(e);
      });
    },
  },
  computed: {  
    icons() {
      return icons;
    },
  },
};
</script>

<style scoped>
.row {
  width: 100%;
  max-width: 100vw;
}
</style>