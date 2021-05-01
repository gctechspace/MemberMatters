<template>
  <q-page class="content-start justify-center q-mt-md">
    <q-tabs v-model="tab" class="text-primary">
      <q-tab key="home" name="home" :icon="icons.info" label="Getting started" />
      <q-tab v-for="device in devices"  v-bind:key="device.id" :name="device.id" :icon="icons.tools" :label="device.name" />
    </q-tabs>
    <q-tab-panels v-model="tab" animated>

      <q-tab-panel key="`welcome-tab`" name="home">
      <div class="text-h6">Welcome to the training page</div>
      Here you will find a variety of quizzes to prepare to be inducted in all our machines and devices
      </q-tab-panel>
      
      <q-tab-panel v-for="device in devices" v-bind:key="`${device.id}-tab`" :name="device.id">
      <div class="text-h6">{{device.name}}</div>
      <training-form :questions="device.questions" :name="device.name" :id="device.id" />
      </q-tab-panel>
      
    </q-tab-panels>
  </q-page>
</template>

<script>
import icons from "../icons"
import Lodash from "lodash"
import TrainingForm from "../components/TrainingForm"
export default {
  name: "TrainingPage",
  components: { TrainingForm},
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
      tab:"VacuumFormer",
      devices:
      [
        {
          id:"laserCutter",
          name: "Laser Cutter",
          "questions":[
          {
            "type": "radio",
            "question": "What is the colour of the laser cutter",
            "id":"laserColor",
            "options": [
              "red",
              "blue",
              "orange",
              "purple"
            ],
            "answer": "red"
          },
          {
            "type": "select",
            "question": "where is the fire extinguisher?",
            "id":"fireextinguisher",
            "options": [
            "cupboard",
            "top shelf",
            "draw"
            ],
            "answer": "draw"
          },
          {
            "type": "truefalse",
            "question": "Can the laser cutter cut metal?",
            "id":"cutMetal",
            "answer": "false"
          }
          ]
        },
        {
          id:"3dPrinter",
          name: "3D Printer",
          "questions":[
          {
            "type": "radio",
            "question": "What is the colour of the 3d printer",
            "id":"3dPrinterColor",
            "options": [
              "red",
              "blue",
              "orange",
              "purple"
            ],
            "answer": "red"
          },
          {
            "type": "truefalse",
            "question": "Can I use whipper snipper cord as filament?",
            "id":"cordasfilament",
            "answer": "false"
          }
          ]
        },
        {
          id:"VacuumFormer",
          name: "vacuum Former",
          "questions":[
          {
            "type": "radio",
            "question": "What plastic is most flexible?",
            "id":"flexiblePlastic",
            "options": [
              "hips",
              "acrylic",
              "abs",
              "pla"
            ],
            "answer": "hips"
          },
          {
            "type": "select",
            "question": "What is the easiest material to use on the 3d printer",
            "options": [
            "abs",
            "pla",
            "hips",
            ],
            "answer": "pla"
          },
          {
            "type": "truefalse",
            "question": "Can you use metal to vacuum form?",
            "id":"vacuumMetal",
            "answer": "false"
          }
          ]
        }
      ]
    };
  },
  mounted() {
    // This interval increments the query param every 60 seconds causing an image refresh
    setInterval(() => {
      this.interval++;
    }, 60000)
  },
  methods:{
    onSubmit() {
      console.log(this.form)
    },
    onReset() {
      console.log(this.form)
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