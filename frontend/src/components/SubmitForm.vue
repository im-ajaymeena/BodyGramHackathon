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
        <label for="height" class="text-lg">Height (mm):</label>
        <input name="height" id="height" type="number" v-model="userData.height" class="input">
      </div>
      <div class="input-wrapper">
        <label for="weight" class="text-lg">Weight (gram):</label>
        <input name="weight" id="weight" type="number" v-model="userData.weight" class="input">
      </div>
    </div>
    <h1 class="font-semibold text-2xl mt-6 mb-4">Skinfold Measurement</h1>
    <div class="grid grid-cols-4 gap-4">
      <div class="input-wrapper">
        <label for="tricepsSF" class="text-lg">Triceps(mm):</label>
        <input name="tricepsSF" id="tricepsSF" type="number" v-model="userData.triceps_skinfold" class="input">
      </div>
      <div class="input-wrapper">
        <label for="subscapularSF" class="text-lg">Subscapular(mm):</label>
        <input name="subscapularSF" id="subscapularSF" type="number" v-model="userData.subscapular_skinfold" class="input">
      </div>
      <div class="input-wrapper">
        <label for="supraspinaleSF" class="text-lg">Supraspinale(mm):</label>
        <input name="supraspinaleSF" id="supraspinaleSF" type="number" v-model="userData.supraspinale_skinfold" class="input">
      </div>
      <!-- we dont need cald for now -->
      <!-- <div class="input-wrapper">
        <label for="calfSF" class="text-lg">Calf(mm):</label>
        <input name="calfSF" id="calfSF" type="number" v-model="userData.calfSF" class="input">
      </div> -->
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
    <button type="submit" class="btn text-white bg-blue-700 hover:bg-blue-800">
    <div v-if="loading">
    <svg aria-hidden="true" role="status" class="inline w-4 h-4 mr-3 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
    </svg>
      <span class="sr-only">Loading...</span>
    </div>
    Submit</button>
  </form>
</template>

<script setup lang="ts">
import { ref, defineEmits } from 'vue';
import axios from 'axios';
// import { LogarithmicScale } from 'chart.js/dist';

const emits = defineEmits(['setResult']);

const backendUrl = 'http://localhost:8000';
const loading = ref(false);

const userData = ref({
  name: 'Hilary',
  height: 1610,
  weight: 40000,
  age: 31,
  gender: 'female',
  triceps_skinfold: 10,
  subscapular_skinfold: 10,
  supraspinale_skinfold: 10,
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
  console.log(fieldName, rightImage, frontImage, "handleImageUpload")
}

async function createScan() {
  try {
    loading.value = true

    const formDataToSend = new FormData();

    formDataToSend.append('front_image', frontImage.value);
    formDataToSend.append('right_image', rightImage.value);
    // formDataToSend.append('userData', JSON.stringify(userData.value));

    axios.post(
        backendUrl + '/post_user_data', 
        formDataToSend, 
        {
            headers: {
                'Content-Type': 'multipart/form-data'
            },
            params: {
                name: userData.value.name,
                height: userData.value.height,
                weight: userData.value.weight,
                age: userData.value.age,
                gender: userData.value.gender,
                triceps_skinfold: userData.value.triceps_skinfold,
                subscapular_skinfold: userData.value.subscapular_skinfold,
                supraspinale_skinfold: userData.value.supraspinale_skinfold,
            }
        }
    )
    .then((res) => {
        console.log(res)
        loading.value = false
        emits('setResult', res.data)
    }).catch(() => {
        alert('Input Data is not valid')
        loading.value = false
    })
    } catch (error) {
      loading.value = false
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
