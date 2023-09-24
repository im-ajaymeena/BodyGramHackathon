<template>
  <form action="" class="form" @submit.prevent="createScan">
    <h1 class="font-bold text-2xl mb-4">Input your data</h1>
    <div class="grid grid-cols-3 gap-4">
      <div class="input-wrapper">
        <label for="name" class="text-lg">Name:</label>
        <input name="name" id="name" type="text" v-model="userData.name" class="input">
      </div>
      <div class="input-wrapper">
        <label for="age" class="text-lg">Age:</label>
        <input name="age" id="age" type="number" v-model="userData.age" class="input">
      </div>
      <div class="input-wrapper">
        <label for="gender" class="text-lg">Gender:</label>
        <select name="gender" id="gender" v-model="userData.gender" class="input">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-4">
      <div class="input-wrapper">
        <label for="height" class="text-lg">Height (cm):</label>
        <input name="height" id="height" type="number" v-model="userData.height" class="input">
      </div>
      <div class="input-wrapper">
        <label for="weight" class="text-lg">Weight (kg):</label>
        <input name="weight" id="weight" type="number" v-model="userData.weight" class="input">
      </div>
    </div>
    <h1 class="font-semibold text-2xl mt-6 mb-4">Skinfold Measurement</h1>
    <div class="grid grid-cols-4 gap-4">
      <div class="input-wrapper">
        <label for="tricepsSF" class="text-lg">Triceps(mm):</label>
        <input name="tricepsSF" id="tricepsSF" type="number" v-model="userData.tricepsSF" class="input">
      </div>
      <div class="input-wrapper">
        <label for="subscapularSF" class="text-lg">Subscapular(mm):</label>
        <input name="subscapularSF" id="subscapularSF" type="number" v-model="userData.subscapularSF" class="input">
      </div>
      <div class="input-wrapper">
        <label for="supraspinaleSF" class="text-lg">Supraspinale(mm):</label>
        <input name="supraspinaleSF" id="supraspinaleSF" type="number" v-model="userData.supraspinaleSF" class="input">
      </div>
      <div class="input-wrapper">
        <label for="calfSF" class="text-lg">Calf(mm):</label>
        <input name="calfSF" id="calfSF" type="number" v-model="userData.calfSF" class="input">
      </div>
    </div>
    <div class="grid grid-cols-2 gap-4">
      <div class="input-wrapper">
        <label for="frontPhoto" class="text-lg">Front Photo:</label>
        <input name="frontPhoto" id="frontPhoto" type="file" @change="handleImageUpload('frontImage', $event)" class="file-input file-input-bordered w-full max-w-xs h-[48px]" accept="image/*">
      </div>
      <div class="input-wrapper">
        <label for="rightPhoto" class="text-lg">Side Photo:</label>
        <input name="rightPhoto" id="rightPhoto" type="file" @change="handleImageUpload('rightImage', $event)" class="file-input file-input-bordered w-full max-w-xs h-[48px]" accept="image/*">
      </div>
    </div>
    <button type="submit" class="btn bg-secondary">Submit</button>
  </form>
</template>

<script setup lang="ts">
import { ref, defineEmits } from 'vue';
import axios from 'axios';

const emit = defineEmits();

const backendUrl = 'http://localhost:8000';

const userData = ref({
  name: '',
  height: 0,
  weight: 0,
  age: 0,
  gender: '',
  tricepsSF: 0,
  subscapularSF: 0,
  supraspinaleSF: 0,
  calfSF: 0
});

const frontImage = ref<File | null>(null);
const rightImage = ref<File | null>(null);

function handleImageUpload(fieldName: string, event: Event) {
  const target = event.target as HTMLInputElement;
  if (target.files && target.files.length) {
    if (fieldName === 'frontImage') {
      frontImage.value = target.files[0];
    } else if (fieldName === 'rightImage') {
      rightImage.value = target.files[0];
    }
  }
}

async function createScan() {
  try {
    const formDataToSend = new FormData();

    formDataToSend.append('front_image', frontImage.value);
    formDataToSend.append('right_image', rightImage.value);
    formDataToSend.append('userData', JSON.stringify(userData.value));

    const response = await axios.post(backendUrl + '/post_user_data', formDataToSend);
    console.log('Success:', response.data);
    emit('setResult', response.data);
  } catch (error) {
    console.error('Error:', error);
  }
}
</script>

<style scoped>
.form {
  width: 80%;
  margin: auto;
  background-color: #fff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.input {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
  width: 100%;
}

.input:focus {
  border-color: #3490dc;
  outline: none;
}

.input-wrapper {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}

.label {
  font-size: 1.125rem;
  font-weight: bold;
}

.button {
  background-color: #3490dc;
  color: white;
  border-radius: 8px;
  padding: 12px 24px;
  font-size: 1.25rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #2779bd;
}
</style>
