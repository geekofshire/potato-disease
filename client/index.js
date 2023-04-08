const url="http://localhost:8080/predict"

const form = document.getElementById('myForm');
const input = document.getElementById('myImage');

//var button=document.getElementById('submit');
var class_name=document.querySelector('div.class_name');
var confidence=document.querySelector('div.confidence');

//button.addEventListener('onclick',getprediction)

function getprediction(){
  const file=input.files[0];
  const formData=new FormData();
  formData.append('image',file,file.name);

  $.post(url,file,function(data,status){
    console.log(status);
    class_name.textContent="Class: "+data.class;
    confidence.textContent="Confidence: "+data.confidence;
  })
}

// form.addEventListener('submit', (e) => {
//   e.preventDefault();
//   const file = input.files[0];
//   const formData = new FormData();
//   formData.append('image', file, file.name);
//   fetch(url, {
//     method: 'POST',
//     body: formData
//   })
//   .then(response => {
//     if (!response.ok) {
//       throw new Error('Network response was not ok');
//     }
//     return response.json();
//   })
//   .then(data => {
//     console.log(data);
//   })
//   .catch(error => {
//     console.error('There was a problem with the fetch operation:', error);
//   });
// });


