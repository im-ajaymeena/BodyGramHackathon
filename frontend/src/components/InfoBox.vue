<style scopped>
.info-box {
  border-radius: 5px;
  border: 2px solid rgb(200, 200, 246);
  background-color: rgba(240, 240, 240, 0.932);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.info-item {
  border-radius: 5px;
  border: 2px solid rgb(211, 146, 246);
  background-color: rgb(222, 222, 255);
  display: flex;
  justify-content: space-around;
  margin: 8px 4px;
  padding: 4px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>

<template>
  <div class="info-box">
    <div class="grid grid-cols-5">
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Name </h3>
        <p class="px-2">{{ result.name }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Age </h3>
        <p class="px-2">{{ result.age }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Gender </h3>
        <p class="px-2">{{ result.gender }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Height (cm) </h3>
        <p class="px-2">{{ result.height/10 }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Weight (kg)</h3>
        <p class="px-2">{{ result.weight/1000 }}</p>
      </div>
    </div>

    <div class="grid grid-cols-3">
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Mesomorphy </h3>
        <p class="px-2">{{ result.mesomorphy.toFixed(2) }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Endomorphy </h3>
        <p class="px-2">{{ result.endomorphy.toFixed(2) }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Ectomorphy </h3>
        <p class="px-2">{{ result.ectomorphy.toFixed(2) }}</p>
      </div>
    </div>
    <div class="grid grid-cols-3">
      <div class="info-item">
        <h3 class="px-2 font-semibold"> BMI </h3>
        <p class="px-2">{{ result.bmi.toFixed(2) }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Body fat percentage </h3>
        <p class="px-2">{{ result.body_fat_percentage.toFixed(2) }}</p>
      </div>
      <div class="info-item">
        <h3 class="px-2 font-semibold"> Skeletal muscle mass (unit?)</h3>
        <p class="px-2">{{ result.skeletal_muscle_mass }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {defineProps} from 'vue'

const props = defineProps({
  result: Object
})

</script>
