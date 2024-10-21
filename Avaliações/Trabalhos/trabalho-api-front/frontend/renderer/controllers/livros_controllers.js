import {BASE_API} from '../resources/api'
import axios from 'axios'

async function buscar_livros() {
    try{
        const response = await axios.get(`${BASE_API}/livros/buscar`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function buscar_usuario_id(id) {
    try{
        const response = await axios.get(`${BASE_API}/livros/buscar:${id}`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

export default {buscar_livros, buscar_usuario_id}