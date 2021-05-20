<template>
  <div class="training-form">
    <q-form v-bind:id="id" v-bind:name="name" v-bind="formItems" v-bind:key="id" @submit="onSubmit" @reset="onReset" class="q-gutter-md">

      <q-stepper
        v-for="(formStep, i) in formItems"
        v-bind:key="`formItem.stepName-${i}`"
        v-model="step"
        vertical
        color="primary"
        animated>
         <!-- TODO add dynamic icons -->
        <q-step
          :name="i+1"
          :title="formStep.stepName"
          :icon="icons[formStep.icon]"
          :done="step > i+1">
          <div>
            <div v-for="(formItem) in formStep.data"  v-bind:key="formItem.id">
              <!-- TODO add youtube youtube video embed -->
              <div v-if="formItem.type == 'radio'" class="q-pa-md">
                <q-img
                v-if="formItem.image"
                :src="formItem.image"
                spinner-color="primary"
                spinner-size="82px"
                style="height: 140px; max-width: 150px; marginBottom:10px"
                />
                <q-markdown style="marginBottom: 16px" :src="`${formItem.question}`"></q-markdown>
                <div class="q-gutter-sm">
                  <div  v-for="option in formItem.options" v-bind:key="option.id">
                    <q-radio lazy-rules="ondemand" dense v-model="form[formItem.id]" :val="option" :label="option"></q-radio>
                  </div>      
                </div>
              </div>

              <div v-if="formItem.type == 'select'" class="q-px-sm q-pt-sm">
                <div class="q-gutter-sm">
                <q-img
                v-if="formItem.image"
                :src="formItem.image"
                spinner-color="primary"
                spinner-size="82px"
                style="height: 140px; max-width: 150px; marginBottom:10px"
                />
                  
                  <q-select filled v-model="form[formItem.id]" :options="formItem.options" :label="formItem.question"></q-select>
                </div>
              </div>

              <div v-if="formItem.type == 'truefalse'" class="q-px-sm q-pt-sm">
                <q-img
                v-if="formItem.image"
                :src="formItem.image"
                spinner-color="primary"
                spinner-size="82px"
                style="height: 140px; max-width: 150px; marginBottom:10px"
                />
                <q-toggle :checked-icon="icons.success" :unchecked-icon="icons.close" v-model="form[formItem.id]" right-label :label="`${formItem.question}`" color="primary"/>
              </div>

              <div v-if="formItem.type == 'text'" class="q-px-sm q-pt-sm">
                <q-markdown :src="formItem.text"></q-markdown>
              </div>
            </div>
          </div>

          <q-toggle v-model="form.accept" label="I accept the license and terms" />
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
        <q-stepper-navigation>
          <q-btn v-if="step < formItems.length" @click="step++" color="primary" label="Continue"></q-btn>
          <q-btn v-if="step > 1" flat @click="step--" color="primary" label="Back" class="q-ml-sm"></q-btn>
        </q-stepper-navigation>
      </q-step>
      </q-stepper>
    </q-form>
  </div>
</template>

<script>
import icons from "../icons"
import { QMarkdown } from '@quasar/quasar-ui-qmarkdown'
export default {
  name: "TrainingForm",
  props: {
    id:Number,
    name:String,
    formItems:Array
  },
    components:{QMarkdown},
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
        accept:null,
      },
      step: 1
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
      //TODO add submission function
      console.log(this.form)
    },
    onReset() {
      console.log(this.form)
    },
    formFunction: function () {
      var obj = {}
      this.formItems.map((step) => {
        step.data.map((question)=>{
          if(!(question.type === "text")){
           obj[question.id] = null
          }
        })
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

// formItems example
// {
// "data":[
// {"stepName":"My first step",
// "icon":"tools",
// "data":[  {
//     "type": "radio",
//     "question": "What is the colour of the laser cutter?",
//     "id":"laserColor",
//     "image":"https://wiki.gctechspace.org/public/lasercutter.jpg",
//     "options": [
//       "red",
//       "blue",
//       "orange",
//       "purple"
//     ],
//     "answer": "red"
//   },
//   {
//     "type": "select",
//     "question": "where is the fire extinguisher?",
//     "id":"fireextinguisher",
//     "options": [
//     "cupboard",
//     "top shelf",
//     "draw"
//     ],
//     "answer": "draw"
//   },
//   {
//     "type": "truefalse",
//     "question": "Can the laser cutter cut metal?",
//     "id":"cutMetal",
//     "answer": "false"
//   },
//   {
//     "type":"text",
//     "text":"# test markdown `ff`"
//   }]},
//   {"stepName":"My second step",
// "icon":"tools",
// "data":[  {
//     "type": "radio",
//     "question": "What is the colour of the laser cutter?",
//     "id":"laserColor",
//     "image":"https://wiki.gctechspace.org/public/lasercutter.jpg",
//     "options": [
//       "red",
//       "blue",
//       "orange",
//       "purple"
//     ],
//     "answer": "red"
//   },
//   {
//     "type": "select",
//     "question": "where is the fire extinguisher?",
//     "id":"fireextinguisher",
//     "options": [
//     "cupboard",
//     "top shelf",
//     "draw"
//     ],
//     "answer": "draw"
//   },
//   {
//     "type": "truefalse",
//     "quesion": "Can the laser cutter cut metal?",
//     "id":"cutMetal",
//     "answer": "false"
//   },
//   {
//     "type":"text",
//     "text":"# test markdown `ff`"
//   }]}
  
//   ]}