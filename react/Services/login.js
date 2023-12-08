const hola = document.querySelector('#hola')
const url = 'http://127.0.0.1:5000/login'
//const url = 'https://www.datos.gov.co/resource/ccvq-rp9s.json'
const formulario = document.querySelector('#loginform')
const email = document.querySelector('#email')
const password = document.querySelector('#password')
const conf = {method:'GET',mode:'no-cors'}
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
    console.log(email)
    const query = url.concat(`?email=`,email.value).concat(`&password=`,password.value)
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