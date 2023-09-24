<style scoped>
.recommendation {
  border-radius: 5px;
  border: 2px solid rgb(200, 200, 246);
  background-color: rgba(240, 240, 240, 0.932);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 4px
}
.text-box {
  border: 1px solid gray;
  background-color: lightgray;
  margin: 4px;
  padding: 4px
}
</style>

<template>
  <div class="recommendation">
    <h1 class="font-bold">Recommendation</h1>
    <div class="text-box">
      <h2 class="font-semibold mb-2">Diet</h2>
      <p>{{ diet }}</p>
    </div>
    <div class="text-box">
      <h2 class="font-semibold mb-2">Excerise</h2>
      <p>{{ exercise }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref, defineProps, watch, onMounted} from 'vue'

const diet = ref('')
const exercise = ref('')

const coordinates = defineProps({
  coordinates: Object, // Define the type for the "result" prop
})

// watch(result, (newValue, oldValue) => {
//   setRecommendation(newValue)
// })
onMounted(() => {
  setRecommendation(coordinates.coordinates)
})

function setRecommendation(value) {
  console.log(value.coordinates);

  if (value['x'] <= 0 && value['y'] <= -value['x']) {
    // Endomorph
    diet.value = "Endomorphs have slower metabolisms so don’t burn calories as fast as ectomorphs and mesomorphs. Excess calories are more likely to convert to fat. Some believe you’re also less tolerant to carbohydrates, so the best diet for your body type may be one with a higher fat and protein intake and a lower carbohydrate intake to help you lose body fat while keeping your energy level up. /n If you're an endomorph, avoid crash dieting. It will only make your body cling to its fat reserves. Instead, adjust your diet so you're eating more frequent, smaller meals, no more than 5 hours apart. Try to eat slowly, and drink plenty of water. Eat lean proteins and high-fibre foods to help you feel full longer. And don't be fooled by the fat-free fad -- you need a little fat to stay healthy.";
    exercise.value = "Endomorphs should do at least 30 minutes of moderately-paced aerobic activity five days a week. Try walking, jogging, bicycling, dancing, or any other activity that gets your heart pumping. When the pounds start coming off, add weight training two or three times a week to tone and strengthen your muscles.";
  } else if (value['x'] > 0 && value['y'] <= value['x']) {
    // Ectomorph
    diet.value = "Ectomorphs tend to respond well to carbohydrates, so you can eat those freely. You’ll just want to choose healthy sources, including fibre-rich fruits, veggies, and whole grains. To optimize your health, reach for plenty of protein, including from lean animal sources and plants like nuts and seeds. Prioritizing protein will help with your muscle-building efforts. For snacks and meals, choose nutrient- and calorie-dense foods like nuts, dried fruits, sunflower seeds, and starchy vegetables, rather than lower-cal choices like fresh fruits and popcorn. Don't skimp on fat, either - make sure that 30% of your calories come from fat.";
    exercise.value = "When exercising, ectomorphs should keep cardio or aerobic training to a minimum while concentrating on muscle-building moves with fairly heavy weights.";
  } else {
    // Mesomorph
    diet.value = "According to the tenets of the body type diet, people with mesomorph bodies should follow a balanced and well-rounded diet that doesn’t cut out food groups unnecessarily - a diet divided fairly evenly between the macronutrients (carbs, protein, and fat). Mesomorphs tend to have good insulin sensitivity so they can eat a moderate amount of carbohydrates without wreaking havoc on their blood sugar levels. Genetically lucky mesomorphs may have an easier time than most staying slim and fit, but this can lead to a tendency to assume that they can handle an extra helping of dessert or a hiatus from the gym. But the same rules for health and well-being apply to them as to everyone else.";
    exercise.value = "While mesomorphs are generally strong and muscular, they also run the risk of unwanted weight gain if they get off track with their diet and focus on weight lifting alone. A mesomorph workout must incorporate regular cardiovascular exercise if the goal is to stay lean and slim.";
  }
}
</script>
