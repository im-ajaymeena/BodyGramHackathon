<template>
  <form action="" class="form" @submit.prevent="createScan">
    <h1 class="font-bold">Input your data</h1>
    <div class="grid grid-cols-3">
      <div class="input-wrapper">
        <label for="name">Name: </label>
        <input name='name' id="name" type="text" v-model="formData.name">
      </div>
      <div class="input-wrapper  px-4">
        <label for="age">Age: </label>
        <input name='age' id="age" type="number" v-model="formData.age">
      </div>
      <div class="input-wrapper">
        <label for="gender">Gender: </label>
        <select name='gender' id="gender" v-model="formData.gender">
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
    </div>
    <div class="grid grid-cols-3">
      <div class="input-wrapper">
        <label for="height">Height(cm): </label>
        <input name='height' id="height" type="number" v-model="formData.height">
      </div>
      <div class="input-wrapper px-4">
        <label for="weight">Weight(kg): </label>
        <input name='weight' id="weight" type="number" v-model="formData.weight">
      </div>
    </div>
    <h1 class="font-semibold">Skinfold Measurement</h1>
    <div class="grid grid-cols-3">
      <div class="input-wrapper">
        <label for="height">Triceps: </label>
        <input name='height' id="height" type="number" v-model="formData.height">
      </div>
      <div class="input-wrapper px-4">
        <label for="weight">Subscapular: </label>
        <input name='weight' id="weight" type="number" v-model="formData.weight">
      </div>
    </div>
    <div class="grid grid-cols-3">
      <div class="input-wrapper">
        <label for="height">Supraspinale: </label>
        <input name='height' id="height" type="number" v-model="formData.height">
      </div>
      <div class="input-wrapper px-4">
        <label for="weight">Calf?: </label>
        <input name='weight' id="weight" type="number" v-model="formData.weight">
      </div>
    </div>
    <div class="grid grid-cols-2">
      <div class="input-wrapper">
        <label for="frontPhoto">Front Photo: </label>
        <input name='frontPhoto' id="frontPhoto" type="file" @change="handleImageUpload('frontImage', $event)"
          accept="image/*">
      </div>
      <div class="input-wrapper">
        <label for="rightPhoto">Side Photo: </label>
        <input name='rightPhoto' id="rightPhoto" type="file" @change="handleImageUpload('rightImage', $event)"
          accept="image/*">
      </div>
    </div>
    <button type="submit" class="button">submit</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios';
const formData = ref({
  name: '',
  height: 0,
  weight: 0,
  age: 0,
  gender: '',
})

const frontImage = ref<File | null>(null)
const rightImage = ref<File | null>(null)

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

function createScan() {
  const data = {
    user: {
      name: formData.value.name,
      height: formData.value.height * 10,
      weight: formData.value.weight * 1000,
      age: formData.value.age,
      gender: formData.value.gender
    },
    front_image: frontImage.value,
    right_image: rightImage.value
  }
  console.log(data);

  axios.post('/backendUrl/post_user_data', data)
    .then((response) => {
      console.log('Success:', response.data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


</script>

<style scoped>
.form {
  width: 80%;
  margin: auto;
  background-color: beige;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 5px 5px 10px 0px rgba(0, 0, 0, 0.1);
}

input {
  border-radius: 5px;
  padding: 1px 2px;
}

input:focus {
  box-shadow: 5px 5px 10px 0px rgba(0, 0, 0, 0.1);
}

.input-wrapper {
  margin-bottom: 16px;
  display: flex;
  justify-content: space-between;
}

.input-wrapper>label {
  min-width: 50px;
  padding-right: 8px;
}

.button {
  background-color: blue;
  border-radius: 8px;
  padding: 8px 16px;
  color: white;
  box-shadow: 5px 5px 10px 0px rgba(0, 0, 0, 0.1);
}
</style>
