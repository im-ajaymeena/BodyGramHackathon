<template>

  <div :class="{'bg-gradient-to-tl from-blue-100 to-blue-100': !isDarkMode}" class="min-h-screen" :data-theme="isDarkMode ? 'dark' : 'fantasy'">
    <header class="bg-gradient-to-r from-green-400 to-blue-500 p-7 mb-20 text-white ">
      <div class="flex items-center"> <!-- Added a flex container for alignment -->
        <h1 class="text-5xl font-bold">ShapeShift</h1>
        <!-- <img src="./assets/logo.png" class="w-auto h-40 pr-4" alt="Logo" /> -->
      </div>
    </header>
    <!-- when no result -->
    <div v-if="!resultData">
      <SubmitForm 
        @setResult="setResultData" 
        />
    </div>
      <!-- v-if="!resultData" -->

    <!-- when there is a result -->
    <div class="result-info" v-if="resultData">
      <InfoBox :result="resultData" />
      <div class="flex result-info" >
        <ResultChart :result="resultData"/>
        <RecommendationBox :result="resultData"/>
      </div>
      <div class="text-end pt-5 pr-20">
        <button @click="resetForm" class="btn btn-sm">Click to reset</button>
      </div>
    </div>
    <footer class="bg-gray-800 text-white py-2 mt-20">
      <div class="container mx-auto flex justify-between items-center">
        <!-- Left-aligned contact information -->
        <div>
          <div class="grid grid-cols-2 gap-4">
            <div class="text-center">
              <h3 class="text-xl font-semibold">Ajay</h3>
              <a href="https://www.linkedin.com/in/johndoe" target="_blank" class="text-blue-400 hover:text-blue-600">LinkedIn</a>
            </div>
            <div class="text-center">
              <h3 class="text-xl font-semibold">Donald </h3>
              <a href="https://www.linkedin.com/in/janesmith" target="_blank" class="text-blue-400 hover:text-blue-600">LinkedIn</a>
            </div>
          </div>
        </div>
        <!-- Right-aligned "Sponsored by BodyGram" -->
        <div >
          <p class="text-left text-lg">Sponsored by: </p>
          <a href="https://bodygram.com/ja/" target="_blank" class="text-blue-400 text-6xl hover:text-blue-600">Bodygram</a>
        </div>
      </div>
    </footer>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'
import SubmitForm from './components/SubmitForm.vue';
import ResultChart from './components/ResultChart.vue';
import RecommendationBox from './components/RecommendationBox.vue'
import InfoBox from './components/InfoBox.vue';

const resultData = ref(null)

function setResultData(data) {
  // resultData.value = data
  console.log(data)
  console.log('resultData:', resultData.value);
  resultData.value = data
  console.log('resultData:', resultData.value);
}

// function plotResult(result) {
//     const x = result['ectomorphy'] - result['endomorphy']
//     const y = 2 * result['mesomorphy'] - (result['endomorphy'] + result['ectomorphy'])
//     return { x, y }
//   }

function resetForm() {
  resultData.value = null
}

const isDarkMode = ref(false);

onMounted(() => {
  // You can add code here to toggle dark mode based on user preferences
});

// watch(resultData, (newResultData, oldResultData) => {
//   coordinates.value = plotResult(newResultData)
// });

// {"name": "ajay",
// "height": 1720,
// "weight": 66000,
// "age": 26,
// "gender": "male",
// "skeletal_muscle_mass": 30906,
// "body_fat_percentage": 16.863,
// "mesomorphy": 3.74719999999999,
// "endomorphy": 3.446762651422772,
// "ectomorphy": 5.574793914125344,
// "bmi": 0.02,
// "reference_somatotype_data": [
//   {
//     "type": "Kayaking",
//     "mesomorphy": 3.82,
//     "endomorphy": 3.38,
//     "ectomorphy": 3.87
//   },
//   {
//     "type": "Basketball",
//     "mesomorphy": 4.09,
//     "endomorphy": 2.77,
//     "ectomorphy": 3
//   },
//   {
//     "type": "Boxing",
//     "mesomorphy": 3.7,
//     "endomorphy": 2.3,
//     "ectomorphy": 2.3
//   },
//   {
//     "type": "Football",
//     "mesomorphy": 3.57,
//     "endomorphy": 2.64,
//     "ectomorphy": 3
//   }
// ]}

</script>

<style scoped>
/* Create a container for the content */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Style the header */
.header {
  background-color: #3490dc;
  color: white;
  padding: 1rem 0;
  text-align: center;
}

.header h1 {
  font-size: 2rem;
  font-weight: bold;
  margin: 0;
}

/* Style the main content */
.main-content {
  padding: 2rem 0;
}

/* Style buttons */
.btn {
  background-color: #3490dc;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #2779bd;
}

/* Style form inputs */
.input {
  border: 1px solid #ccc;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  width: 100%;
}

.result-info>div {
  margin: 4px
}
/* Add more styles as needed for your app */
</style>


