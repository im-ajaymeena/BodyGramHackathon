<template>
  <h1>Hi I am result</h1>
  <div style="width: 750px; height: 750px; background:url(https://i.stack.imgur.com/Y1mnB.png)">
    <canvas id="somatograph" width="750" height="750"></canvas>
  </div>
</template>

<script setup lang="ts">
import Chart from 'chart.js/auto'
import { onMounted } from 'vue';

onMounted(() => {

  const result =
            {'Ectomorphy': 4,
            'Mesomorphy': 1.344,
            'Endomorphy': 4.6 }
  const volleyball =
            {'Ectomorphy': 3.4,
            'Mesomorphy': 2.7,
            'Endomorphy': 2.9 }
  const basketball =
            {'Ectomorphy': 3.7,
            'Mesomorphy': 2.7,
            'Endomorphy': 2.0 }
  const handball =
            {'Ectomorphy': 4.2,
            'Mesomorphy': 4.7,
            'Endomorphy': 1.8 }

  function plotResult(result: Array) {
    const x = result['Ectomorphy'] - result['Endomorphy']
    const y = 2 * result['Mesomorphy'] - (result['Endomorphy'] + result['Ectomorphy'])
    console.log({x, y});

    return {x, y}
  }

  const data = {
    datasets: [{
      label: 'You',
      data: [plotResult(result)],
      backgroundColor: 'rgb(255, 99, 132)'
    },
    {
    label: 'Altheletes',
    data: [plotResult(volleyball), plotResult(basketball), plotResult(handball)],
    backgroundColor: 'rgb(0, 0, 255)',
    datalabels: {
                align: 'end', // Position of the label relative to the point
                anchor: 'end', // Anchor point of the label
                font: {
                    weight: 'bold' // Label font weight
                },
                formatter: function(value, context) {
                    return context.dataset.data[context.dataIndex].label; // Display the label for each point
                }}
  }],
  };

  // const image = new Image();
  // image.src = 'https://i.stack.imgur.com/Y1mnB.png';

  // const plugin = {
  //       id: 'customCanvasBackgroundImage',
  //       beforeDraw: (chart) => {
  //         if (image.complete) {
  //           const ctx = chart.ctx;
  //           const { top, left, width, height } = chart.chartArea;

  //           // Calculate the dimensions to fit the entire chart area
  //           const aspectRatio = image.width / image.height;
  //           const chartAspectRatio = width / height;

  //           let imgWidth, imgHeight;

  //           if (aspectRatio > chartAspectRatio) {
  //             imgWidth = width;
  //             imgHeight = width / aspectRatio;
  //           } else {
  //             imgWidth = height * aspectRatio;
  //             imgHeight = height;
  //           }

  //           const x = left + width / 2 - imgWidth / 2;
  //           const y = top + height / 2 - imgHeight / 2;

  //           ctx.drawImage(image, x, y, imgWidth, imgHeight);
  //         } else {
  //           image.onload = () => chart.draw();
  //         }
  //       },
  //     };

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
            }
      },
      // plugins: [plugin]
    }
    );
  })
</script>
