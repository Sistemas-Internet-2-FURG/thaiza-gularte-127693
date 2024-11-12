import {BASE_API} from '../resources/api'
import axios from 'axios'

async function cadastrar(nome, email, senha) {
    try {
        const formData = new FormData();
        formData.append("nome", nome);
        formData.append("email", email);
        formData.append("senha", senha);
        const response = await fetch(`${BASE_API}/usuarios/criar`, {
          method: "POST",
          body: formData,
        });

        // Retorna o objeto `response` completo para análise no código principal
        return response;

    } catch (error) {
        console.log('Erro no cadastro do usuário: ', error);
        throw error;  // Lança o erro para ser capturado na função chamadora
    }
}


async function login(email, senha) {
    try {
        const formData = new FormData();
        formData.append("email", email);
        formData.append("senha", senha);

        const response = await fetch(`${BASE_API}/usuarios/home`, {
            method: "POST",
            body: formData,
        });

        console.log('AUBREYYYYYYYYYYYYYYYYYYYYYYYYY', response)
        // Checa se a resposta foi bem-sucedida no nível HTTP
        if (!response.ok) {
            throw new Error('Erro ao fazer login: ' + response.statusText);
        }

        // Extrai o JSON da resposta
        const data = await response.json();

        // Verifica o código de resposta dentro do JSON retornado
        if (data.code === 200) {
            localStorage.setItem('usuario', JSON.stringify(data.dados))
            localStorage.setItem('token', JSON.stringify(data.token));
        }

        return data;

    } catch (error) {
        console.log('Erro no acesso do usuario:', error);
        throw error;
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