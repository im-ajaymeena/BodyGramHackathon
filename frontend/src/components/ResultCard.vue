<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { SearchResult } from '../api/api'
import axios, { AxiosResponse } from 'axios'

const props = defineProps<{ result: SearchResult}>()
const text = ref("")

onMounted (() => {
  console.log(props.result.content_type, "contect")
  if (props.result.content_type === 'TEXT') {
    axios.get(props.result.content_url).then((response) => {
      console.log(response.data)
      text.value = response.data
    })
  }
})


</script>

<template>

  <div class="card w-96 bg-base-100 shadow-xl">
  <figure  v-show="result.content_type === 'IMAGE'"  class="px-10 pt-10">
    <img :src="result.content_url"  class="rounded-xl" />
  </figure>
  <div class="card-body items-center text-center">
    <p>{{ text }}</p>
    <span class="badge">{{ result.content_type }}</span>
  </div>
  <div v-show="result.content_type === 'AUDIO'" class="card-body items-center text-center">
    <audio controls :src="result.content_url"></audio>
  </div>
</div>
</template>
