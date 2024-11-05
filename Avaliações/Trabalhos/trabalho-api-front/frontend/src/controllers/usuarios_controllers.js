import {BASE_API} from '../resources/api'
import axios from 'axios'

async function cadastrar(nome, email,senha) {
    try{
        const formData = new FormData();
        formData.append("nome", nome);
        formData.append("email", email);
        formData.append("senha", senha);
      
        const response = await fetch("http://127.0.0.1:5000/usuarios/criar", {
          method: "POST",
          body: formData,
        });
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

export {cadastrar,login, buscar_usuarios, buscar_usuario_id}