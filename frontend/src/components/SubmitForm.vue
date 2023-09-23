<template>
  <form action="" class="form">
    <div class="flex">
      <div class="input-wrapper">
        <label for="name">Name</label>
        <input name='name' id="name" type="text">
      </div>
      <div class="input-wrapper  px-4">
        <label for="age">Age</label>
        <input name='age' id="age" type="number">
      </div>
    </div>
    <div class="flex">
      <div class="input-wrapper">
        <label for="height">Height</label>
        <input name='height' id="height" type="number">
      </div>
      <div class="input-wrapper px-4">
        <label for="weight">Weight</label>
        <input name='weight' id="weight" type="number">
      </div>
    </div>

    <div class="input-wrapper">
      <label for="frontPhoto">Front Photo</label>
      <input name='frontPhoto' id="frontPhoto" type="file">
    </div>
    <div class="input-wrapper">
      <label for="rightPhoto">Side Photo</label>
      <input name='rightPhoto' id="rightPhoto" type="file">
    </div>
    <button type="submit" class="button">submit</button>
  </form>
</template>

<script setup lang="ts">
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

  .input-wrapper {
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
    }

  .input-wrapper>label {
    min-width: 100px;
  }

  .button {
    background-color: blue;
    border-radius: 8px;
    padding:  8px 16px;
    color: white;
    box-shadow: 5px 5px 10px 0px rgba(0, 0, 0, 0.1);
  }
</style>
