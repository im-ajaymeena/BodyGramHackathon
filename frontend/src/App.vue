<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import ResultCard from './components/ResultCard.vue'
import { SearchResult } from './api/api'
import SubmitForm from './components/SubmitForm.vue';
import ResultChart from './components/ResultChart.vue';


const backendUrl = import.meta.env.VITE_APP_BACKEND_URL as string

const searchTerm = ref("")
const isLoading = ref(false)
const results = ref(<SearchResult[]>[])
const gcs_signed_url = ref("")
const query_filename = ref("")
const uploaded_filename = ref("")
const rawFile = ref()
const fileType = ref("")
const textFileContent = ref("");
const showOverlay = ref(false)
const uploadedFileUrl = ref("")
const isDarkMode = ref(false)
const collection_name = ref("")

const search = () => {
  isLoading.value = true

  axios.get<SearchResult[]>(backendUrl + '/search/text', {
    params: {
      query: searchTerm.value
    }
  }).then((response) => {
    console.log("completedddddddddd---------------")
    results.value = response.data
    console.log(results.value, "resi")
    isLoading.value = false
  })
}



const handleToggleChange = (event: any) => {
  if (event.target.checked){
    isDarkMode.value = false
  }
  else{
    isDarkMode.value = true
  }
}

const handleFileChange = (event: any) => {
  fileType.value = ''
  query_filename.value = event.target.files[0].name;
  rawFile.value =  event.target.files[0]

  const fileExtension = event.target.files[0].name.split('.').pop().toLowerCase();
  const reader = new FileReader();

  if (['jpg', 'jpeg', 'png', 'gif'].includes(fileExtension)) {
    fileType.value = 'image';
    reader.onload = (e) => {
      uploadedFileUrl.value = e.target.result;
    };
    reader.readAsDataURL(rawFile.value);
  } else if (['mp3', 'wav'].includes(fileExtension)) {
    reader.onload = () => {
      uploadedFileUrl.value = reader.result;
      fileType.value = 'audio';
    };
    reader.readAsDataURL(rawFile.value);
  } else if (['mp4', 'mov'].includes(fileExtension)) {
    reader.onload = (e) => {
      uploadedFileUrl.value = e.target.result;
      fileType.value = 'video';
    };
    reader.readAsDataURL(rawFile.value);
  } else if (['txt'].includes(fileExtension)) {
    reader.onload = (e) => {
      textFileContent.value = e.target.result;
      fileType.value = 'text';
    };
    reader.readAsText(rawFile.value);
  }
}

const uploadFile = () => {
  isLoading.value = true
  const fileExtension = query_filename.value.split('.').pop();
  const fileContentType = "multipart/form-data"

  axios.get(backendUrl + '/fileUpload/start', {
    params: {
      ext: fileExtension,
      content_type: fileContentType,
    }
  }).then((response) => {
    gcs_signed_url.value = response.data["signed_url"],
    uploaded_filename.value = response.data["file_name"]
  })

  axios.put(gcs_signed_url.value, rawFile.value, {
    headers: {
      'Content-Type': fileContentType,
    },
  }).then(() => {
    axios.get(backendUrl + '/fileUpload/complete', {
      params: {
        file_name: uploaded_filename.value
      }
    }).then(() => {
      results.value = response.data
      isLoading.value = false
    })
  });
}

const openOverlay = () => {
  showOverlay.value = true;
}

const closeOverlay = () => {
  showOverlay.value = false;
}

onMounted(() => {

  let urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('token')) {
    let token = urlParams.get('token')
    if (token){
      localStorage.setItem('jwt', token);
    }
    window.history.pushState({}, document.title, window.location.pathname);
  }

  axios.get(backendUrl + '/select_collection', {
    params: {
      selected_collection_name: collection_name.value
    }
  }).then((response) => {
    console.log("loaded collection", response.data)
  })

})

</script>

<template>
  <div :class="{'bg-gradient-to-tl from-blue-100 to-blue-100': !isDarkMode}" class="min-h-screen" :data-theme="isDarkMode ? 'dark' : 'fantasy'">
    <div class="pb-6 pt-6 pr-6 relative flex flex-row-reverse flex-nowrap gap-5" >
        <div class="flex items-center">
    <input type="checkbox" class="toggle" checked @change="handleToggleChange"/>
  </div>
      <button class="btn" @click="login">
        Login
      </button>
      <button class="btn" @click="uploadFile">Upload</button>
      <button class="btn text-white" @click="openOverlay">Preview</button>
      <input type="file" class="file-input w-full max-w-xs" @change="handleFileChange" :disabled="isLoading"/>
    </div>

    <div v-if="showOverlay" class="fixed inset-0 flex items-center justify-center z-50">
      <div class="overlay">
        <button class="overlay-close" @click="closeOverlay">&times;</button>
        <div v-if="fileType === 'image'" >
          <img :src="uploadedFileUrl" alt="Uploaded Image" class="mx-auto text-center" />
        </div>
        <div v-if="fileType === 'text'" class="rounded shadow">
          <div class="card w-3/5 bg-base-100 shadow-xl mx-auto text-center mt-100">
            {{ textFileContent }}
          </div>
        </div>
        <div>
          <video v-if="fileType === 'video'" controls class="mx-auto text-center">
            <source :src="uploadedFileUrl" type="video/mp4">
          </video>
        </div>
        <div>
          <audio v-if="fileType === 'audio'" controls class="mx-auto text-center">
            <source :src="uploadedFileUrl" type="audio/mpeg">
          </audio>
        </div>
      </div>
    </div>

    <div class="flex flex-col items-center justify-center">
      <div class="py-2 px-3">
        <div class="input-group">

        </div>
      </div>
    </div>

    <div class="pt-20 px-20 grid grid-cols-3 gap-9  justify-items-center">
      <div v-for="(r, i) in results" :key="i">
        <ResultCard :result="r"/>
      </div>
    </div>

    <SubmitForm />
    <ResultChart />

  </div>
</template>

<style scoped>
.overlay {
  position: fixed;
  background: rgba(0, 0, 0, 0.8);
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow-y: auto;
}

.overlay-close {
  position: fixed;
  top: 20px;
  right: 20px;
  color: white;
  font-size: 34px;
  background: transparent;
  border: none;
  outline: none;
  cursor: pointer;
}

.overlay-close:hover {
  color: red;
}

.overlay img,
.overlay video,
.overlay audio,
.overlay .card {
  max-width: 60%;
  max-height: 60%;
  min-width: 15vw; /* Set minimum width to 25% of the viewport width */
  min-height: 15vh; /* Set minimum height to 25% of the viewport height */
  border-radius: 4px;
  overflow: auto;
}

.btn {
  color: white;
}

</style>
