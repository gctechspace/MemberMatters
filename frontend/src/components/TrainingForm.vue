<template>
  <div class="training-form">
    <q-form v-bind:id="id" v-bind:name="name" v-bind="formItems" v-bind:key="id" @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <div>
        <div v-for="formItem in formItems"  v-bind:key="formItem.id">
          
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
    </q-form>
  </div>
</template>

<script>
import icons from "../icons"
import Lodash from "lodash"
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
    onReset() {
      console.log(this.form)
    },
    formFunction: function () {
      var obj = {}
      this.formItems.map(function(q) {
        obj[q.id] = null
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
//   {
//     "type": "radio",
//     "formItem": "What is the colour of the laser cutter?",
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
//     "formItem": "where is the fire extinguisher?",
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
//     "formItem": "Can the laser cutter cut metal?",
//     "id":"cutMetal",
//     "answer": "false"
//   },
//   {
//     "type":"text",
//     "text":"# test markdown `ff`"
//   }
//   ]}