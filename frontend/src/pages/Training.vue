<template>
  <q-page class="row flex content-start justify-center q-mt-md">
    <div class="row flex flex-center">
      <p class="text-body1 col-12 text-center q-px-md q-pt-md">
        {{ $t("training.pageDescription") }}
      </p>
    </div>

      <q-form
      @submit="onSubmit"
      @reset="onReset"
      class="q-gutter-md"
      >
    
  <div class="q-pa-md q-gutter-sm">

    <div v-for="question in questions"  v-bind:key="question.id">
      
      
      <div v-if="question.type == 'radio'" class="q-px-sm q-pt-sm">
        {{question.question}}

        <div class="q-gutter-sm">
          <div  v-for="option in question.options" v-bind:key="question.id">
            <q-radio dense v-model="form[question.id]" :val="option" :label="option"></q-radio>
          </div>      
          <div class="q-px-sm q-pt-sm"> Your selection is: <strong>{{ form[question.id] }}</strong></div>  
        </div>

      </div>

      <div v-if="question.type == 'select'" class="q-px-sm q-pt-sm">

        <div class="q-gutter-sm">
          <q-select filled v-model="form[question.id]" :options="question.options" :label="question.question"></q-select>
        </div>
      </div>

      <div v-if="question.type == 'truefalse'" class="q-px-sm q-pt-sm">

        <div class="q-gutter-sm">
          {{question.question}}
          <q-toggle v-model="form[question.id]" right-label :label="`${(form[question.id]==null) ? 'true/false' : form[question.id] }`" color="primary"/>
          <!-- <q-toggle v-model="form[question.id]" label="'tf' order" color="primary" /> -->
        </div>
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

  </q-page>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "TrainingPage",
  data() {
    return {
    test: function () {
           var obj = {}
            questions.map(function(q) {
            (obj[q.id] == "cutMetal") ? obj[q.id] = 10 : obj[q.id] = null
            
        });
      return obj
    },
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
   
      questions:[
        {
        "type": "text",
        "textType":"name",
        "paramId": "fname",
        "label": "First Name",
        id:1
      },
      {
        "type": "text",
        "textType":"name",
        "paramId": "lastname",
        "label": "Last Name",
        id:2
      },
      {
        "type": "radio",
        "question": "What is the colour of the laser cutter",
        "id":"laserColor",
        "options": [
          "red",
          "blue",
          "orange"
        ],
        "answer": "orange"
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
        "question": "Can you cut metal?",
        "id":"cutMetal",
        "answer": "true"
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
       
  },
};
</script>

<style scoped>
.row {
  width: 100%;
  max-width: 100vw;
}
</style>
