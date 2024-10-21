import {BASE_API} from '../resources/api'
import axios from 'axios'

async function cadastrar(nome, email,senha) {
    try{
        const response = await axios.post(`${BASE_API}/usuarios/criar`, {
            nome: nome,
            email:email,
            senha:senha
        })

        return response.code

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function login(event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    const email = document.getElementById('usuario').value; // Captura o valor do input de email
    const senha = document.getElementById('senha').value;
    try{
        const response = await axios.post(`${BASE_API}/usuarios/home`, {
            email:email,
            senha:senha
        })

        if(response.code === 200){
            localStorage.setItem('usuario', response.dados)
        }

        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function buscar_usuarios() {
    try{
        const response = await axios.get(`${BASE_API}/usuarios/buscar`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function buscar_usuario_id(id) {
    try{
        const response = await axios.get(`${BASE_API}/usuarios/buscar:${id}`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

export default {cadastrar,login, buscar_usuarios, buscar_usuario_id}