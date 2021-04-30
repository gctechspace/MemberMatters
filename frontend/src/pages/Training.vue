<template>
  <q-page class="content-start justify-center q-mt-md">
    <div class="row flex flex-center">
      <p class="text-body1 col-12 text-center q-px-md q-pt-md">
        {{ $t("training.pageDescription") }}
      </p>
    </div>

    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <div>
        <div v-for="question in questions"  v-bind:key="question.id">
          
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
      questions:[
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