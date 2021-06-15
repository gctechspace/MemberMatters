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
          :name="i"
          :title="formStep.stepName"
          :icon="icons[formStep.icon]"
          :done="step > i+1">
          <div>
            <div v-for="(formItem) in formStep.data"  v-bind:key="formItem.id">
              <!-- TODO add youtube youtube video embed -->
              <div v-if="formItem.type == 'radio'" class="q-pa-md" :style="{borderStyle: 'solid', borderColor: `${(touched && !form[formItem.id]) ? 'red' : 'transparent'}`, marginTop:'10px', borderWidth:'1px', borderRadius:'16px'}">
                <q-img
                v-if="formItem.image"
                :src="formItem.image"
                spinner-color="primary"
                spinner-size="82px"
                style="height: 140px; max-width: 150px; marginBottom:10px"
                />
                <q-markdown :style="{marginBottom: '16px'}" :src="`${formItem.question}`"></q-markdown>
                <div class="q-gutter-sm">
                  <div  v-for="option in formItem.options" v-bind:key="option.id">
                    <q-radio dense v-model="form[formItem.id]" :val="option" :label="option"></q-radio>
                  </div>      
                    <q-markdown v-if="(touched && !form[formItem.id])" :style="{marginBottom: '16px', color:'red'}" src="Please complete the question"></q-markdown>
                </div>
              </div>

              <div v-if="formItem.type == 'select'" :style="{borderStyle: 'solid', borderColor: `${(touched && !form[formItem.id]) ? 'red' : 'transparent'}`, marginTop:'10px', paddingBottom:'10px', borderWidth:'1px', borderRadius:'16px'}" class="q-px-sm q-pt-sm" >
                <div class="q-gutter-sm">
                <q-img
                v-if="formItem.image"
                :src="formItem.image"
                spinner-color="primary"
                spinner-size="82px"
                style="height: 140px; max-width: 150px; marginBottom:10px"
                />
                  
                  <q-select filled v-model="form[formItem.id]" :options="formItem.options" :label="formItem.question"
                  lazy-rules :rules="[ val => val && val.length > 0 || 'Please complete the question']"
                  ></q-select>
                </div>
              </div>

              <div v-if="formItem.type == 'truefalse'" class="q-px-sm q-pt-sm" :style="{borderStyle: 'solid', borderColor: `${(touched && !form[formItem.id] == null) ? 'red' : 'transparent'}`,  marginTop:'10px', borderWidth:'1px', borderRadius:'16px'}">
                <q-img
                v-if="formItem.image"
                :src="formItem.image"
                spinner-color="primary"
                spinner-size="82px"
                style="height: 140px; max-width: 150px; marginBottom:10px"
                />
                <q-toggle :checked-icon="icons.success" :unchecked-icon="icons.close" v-model="form[formItem.id]" right-label :label="`${formItem.question}`" color="primary"/>
                <q-markdown v-if="(touched && form[formItem.id]== null)" :style="{marginBottom: '16px', color:'red'}" src="Please complete the question"></q-markdown>
              </div>

              <div v-if="formItem.type == 'text'" class="q-px-sm q-pt-sm">
                <q-markdown :src="formItem.text"></q-markdown>
              </div>
            </div>
          </div>

            <!-- <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" /> -->
            <div v-if="step == stepTotal">
                <q-toggle :checked-icon="icons.success" :unchecked-icon="icons.close" v-model="form.accept" right-label label="I accept the license and terms" color="primary"/>
                <q-markdown v-if="(touched && !form.accept)" :style="{marginBottom: '16px', color:'red'}" src="Submission can not be submitted without accepting terms and conditions"></q-markdown>
            </div>
        <q-stepper-navigation>
          <q-btn v-if="step == stepTotal" @click="continueFunction" label="submit" type="submit" color="primary-btn" :loading="buttonLoading" :disable="buttonLoading"/>

          <q-btn v-if="step < stepTotal" @click="continueFunction" type="submit" color="primary-btn" label="Continue" :loading="buttonLoading" :disable="buttonLoading"></q-btn>
          
          <q-btn v-if="step > 0" flat @click="step--" color="primary" label="Back" class="q-ml-sm"></q-btn>
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
      step: 0,
      stepTotal:0,
      touched:false
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
      if(!this.form.accept){
        console.log("Can not continue if you do not accept terms and conditions")
      }

      console.log(this.form)
    },
    onReset() {
      console.log(this.form)
    },
    continueFunction: function(){
      var nextPage = true
      this.formItems[this.step].data.map((item) =>{
        if(item.id){
          var a = this.form[item.id]
          if(a || a == false || a == 0){
         }else {
          nextPage = false
          this.touched = true
        }
        }
      })
      if (nextPage){ 
        this.touched = false
        if(this.step == this.stepTotal){
          onSubmit()
        }else this.step++
        
      }else console.log("please complete each question")
    },
    formFunction: function () {
      var obj = {}
      var objSelect = {}
      this.formItems.map((step) => {
        this.stepTotal++
        step.data.map((question)=>{
          if(!(question.type === "text")){
           obj[question.id] = null
           objSelect[question.id] = null
          }
        })
      });
      this.form = {...this.form, ...obj}
      this.stepTotal--
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
//     "id":"fireExtinguisher",
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
//     "question": "What Wattage is our laser cutter",
//     "id":"wattage",
//     "options": [
//       "50W",
//       "100W",
//       "60W",
//       "120W"
//     ],
//     "answer": "100W"
//   },
//   {
//     "type": "select",
//     "question": "What material can't you laser cut?",
//     "id":"badmaterial",
//     "options": [
//     "acrylic plastic",
//     "pla plastic",
//     "pvc plastic"
//     ],
//     "answer": "pvc plastic"
//   },
//   {
//     "type": "truefalse",
//     "question": "Is the laser cutter water cooled?",
//     "id":"watercooled",
//     "answer": "true"
//   },
//   {
//     "type":"text",
//     "text":"# some awesome text here `oh yeah!`"
//   }]},
//   {"stepName":"My second step",
// "icon":"tools",
// "data":[  {
//     "type": "radio",
//     "question": "What type of glasses should you use when using the laser cutter?",
//     "id":"glasses",
//     "options": [
//       "sun glasses",
//       "clear glasses",
//       "sunnies",
//       "certified laser glasses"
//     ],
//     "answer": "certified laser glasses"
//   },
//   {
//     "type": "select",
//     "question": "What do you do if the laser cutter gets stuck",
//     "id":"emergency",
//     "options": [
//     "call for help",
//     "emergency stop",
//     "kick it until it stops"
//     ],
//     "answer": "emergency stop"
//   },
//   {
//     "type": "truefalse",
//     "question": "Can the laser cutter be left unattended?",
//     "id":"unattended",
//     "answer": "false"
//   }]}
  
//   ]}