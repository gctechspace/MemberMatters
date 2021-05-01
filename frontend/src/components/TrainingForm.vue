<template>
  <div class="training-form">
        <q-form v-bind:id="id" v-bind:name="name" v-bind="questions" v-bind:key="id" @submit="onSubmit" @reset="onReset" class="q-gutter-md">
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
export default {
  name: "TrainingForm",
  props: {
    id:String,
    name:String,
    questions:Object
  },
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

      this.questions.map(function(q) {
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