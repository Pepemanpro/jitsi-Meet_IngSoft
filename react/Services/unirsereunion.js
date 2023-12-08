const hola = document.querySelector('#hola')
const url = 'http://127.0.0.1:5000/aggmeet'
//const url = 'https://www.datos.gov.co/resource/ccvq-rp9s.json'
const formulario = document.querySelector('#aggmeetform')
const UserId = document.querySelector('#UserId')
const ReunionId = document.querySelector('#ReunionId')
const conf = {method:'POST',mode:'no-cors'}
const cargar = event => {
    event.preventDefault();
    getData();
}
class NetworkError extends Error {
    constructor (message) {
      super(message);
      this.name = 'NetworkError';
    }
  }
const getData = async() => {
    console.log(UserId)
    const query = url.concat(`?UserId=`,UserId.value).concat(`&ReunionId=`,ReunionId.value)
    console.log(query)
    const response = await fetch(query,conf)
    console.log(response.text())
    const valuee = await response.text();
    login(await valuee)
    // const response = Promise.allSettled([
    //     fetch(query, conf).then(response => response.json())])
    //     .then(([{ value, reason }]) =>{return { data: value, error: reason }});
    //   login(await response);
    };

const login = (response) => {
    console.log(response)
    console.log('holaaaa')
    //window.location.href = "inapp.html";
    hola.innerHTML = `<h1>${response}</h1>`
}
formulario.addEventListener('submit',cargar)