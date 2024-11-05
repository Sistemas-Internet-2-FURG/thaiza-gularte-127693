import {BASE_API} from '../resources/api'
import axios from 'axios'

async function buscar_comentarios() {
    try{
        const response = await axios.get(`${BASE_API}/comentarios/buscar`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function buscar_comentario_id(id) {
    try{
        const response = await axios.get(`${BASE_API}/comentarios/buscar:${id}`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

export default {buscar_comentario_id, buscar_comentarios}