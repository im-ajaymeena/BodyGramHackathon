<template>
  <h1>Result Somatograph</h1>
  <div class="background">
    <canvas id="somatograph" width="750" height="750"></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Chart from 'chart.js/auto'
import { onMounted } from 'vue';
import ChartDataLabels from 'chartjs-plugin-datalabels'

Chart.register(ChartDataLabels);


const althelete = ref([
  {
    "type": "Kayaking",
    "mesomorphy": 3.82,
    "endomorphy": 3.38,
    "ectomorphy": 3.87
  },
  {
    "type": "Basketball",
    "mesomorphy": 4.09,
    "endomorphy": 2.77,
    "ectomorphy": 3
  },
  {
    "type": "Boxing",
    "mesomorphy": 3.7,
    "endomorphy": 2.3,
    "ectomorphy": 2.3
  },
  {
    "type": "Football",
    "mesomorphy": 3.57,
    "endomorphy": 2.64,
    "ectomorphy": 3
  }
])

onMounted(() => {

  const result =
  {
    'ectomorphy': 4,
    'mesomorphy': 1.344,
    'endomorphy': 4.6
  }

  function plotResult(result: Array) {
    const x = result['ectomorphy'] - result['endomorphy']
    const y = 2 * result['mesomorphy'] - (result['endomorphy'] + result['ectomorphy'])
    console.log({ x, y });
    return { x, y }
  }

  const data = {
    datasets: [{
      label: 'You',
      data: [{label: "You", x: plotResult(result).x, y: plotResult(result).y}],
      backgroundColor: 'rgb(255, 99, 132)'
    },
    {
      data: althelete.value.map(item => ({
        label: item.type,
        x: plotResult(item).x,
        y: plotResult(item).y
      })),
      backgroundColor: 'rgb(0, 0, 255)'
    }],
  };

  console.log(data);
  new Chart(
    document.getElementById('somatograph'),
    {
      type: 'scatter',
      data: data,
      options: {
        scales: {
          x: {
            type: 'linear',
            position: 'bottom',
            min: -8, // Set the minimum value for the x-axis
            max: 9,  // Set the maximum value for the x-axis
          },
          y: {
            min: -11, // Set the minimum value for the y-axis
            max: 16,  // Set the maximum value for the y-axis
          }
        },
        plugins: {
          datalabels: {
            align: 'right', // Position of the label relative to the point
            anchor: 'start', // Anchor point of the label
            font: {
              weight: 'bold' // Label font weight
            },
            formatter: function (value, context) {
              return context.dataset.data[context.dataIndex].label; // Display the label for each point
            }
          }
        }
      },
    }
  );
})
</script>

<style>
.background {
  background-size: 101%;
  background-position: top 5px right -15px;
  width: 750px;
  height: 750px;
  background-image: url(https://i.stack.imgur.com/Y1mnB.png);
  /* background-image: url(~@/assets/somatograph.png) */
}
</style>
