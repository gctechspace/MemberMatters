<template>
  <q-page class="content-start justify-center q-mt-md">

    <q-tabs v-model="tab" class="text-primary">
      <q-tab key="home" name="home" :icon="icons.info" label="Getting started" />
      <q-tab v-for="device in devices"  v-bind:key="device.id" :name="device.name" :icon="icons.tools" :label="device.name" />
    </q-tabs>

    <q-tab-panels v-model="tab" animated>

      <q-tab-panel key="`welcome-tab`" name="home">
      <div class="text-h6">Welcome to the training page</div>
      Here you will find a variety of quizzes to prepare to be inducted in all our machines and devices
      </q-tab-panel>
      <q-tab-panel v-for="device in devices" v-bind:key="`${device.id}-tab`" :name="device.name">
      <div class="text-h6">{{device.name}}</div>

      <q-form v-bind:key="device.id" @submit="onSubmit" @reset="onReset" class="q-gutter-md">
        <div>
          <div v-for="question in device.questions"  v-bind:key="question.id">
            
            <div v-if="question.type == 'radio'" class="q-pa-md">
              {{question.question}}

              <div class="q-gutter-sm">
                <div  v-for="option in question.options" v-bind:key="option.id">
                  <q-radio dense v-model="form[question.id]" :val="option" :label="option"></q-radio>
                </div>      
              </div>
            </div>

            <div v-if="question.type == 'select'" class="q-px-sm q-pt-sm">
              <div class="q-gutter-sm">
                <q-select filled v-model="form[question.id]" :options="question.options" :label="question.question"></q-select>
              </div>
            </div>

            <div v-if="question.type == 'truefalse'" class="q-px-sm q-pt-sm">
                <q-toggle :checked-icon="icons.success" :unchecked-icon="icons.close" v-model="form[question.id]" right-label :label="`${question.question}`" color="primary"/>
            </div>
          </div>
        </div>

          <q-toggle v-model="accept" label="I accept the license and terms" />

          <div>
              <q-btn
              :label="$t('button.submit')"
              type="submit"
              color="primary-btn"
              :loading="buttonLoading"
              :disable="buttonLoading"
              />
            <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
          </div>
      </q-form>
      </q-tab-panel>
    </q-tab-panels>

  </q-page>
</template>

<script>
import icons from "../icons"
export default {
  name: "TrainingPage",
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
        printer:null  
      },
      tab:"home",
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
    }, 60000),
    this.formFunction()

  },
  methods:{
    onSubmit() {
      console.log(this.form)
    },
    formFunction: function () {
      var obj = {}
      this.questions.map(function(q) {
        (obj[q.id] == "cutMetal") ? obj[q.id] = 10 : obj[q.id] = null
      });
      this.form = {...this.form, ...obj}
    }
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