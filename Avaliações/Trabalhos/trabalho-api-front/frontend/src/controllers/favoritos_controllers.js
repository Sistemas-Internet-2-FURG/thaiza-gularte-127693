import {BASE_API} from '../resources/api'
import axios from 'axios'


async function favoritar(id_livro,id_usuario) {
    try{
        const response = await axios.post(`${BASE_API}/usuarios/criar`, {
            id_usuario: id_usuario,
            id_livro:id_livro
        })

        return response.code

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function buscar_favoritos() {
    try{
        const response = await axios.get(`${BASE_API}/favoritos/buscar`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

async function buscar_favorito_id(id) {
    try{
        const response = await axios.get(`${BASE_API}/favoritos/buscar:${id}`)
        return response

    }catch(error){
        console.log('Erro no cadastro do usuario: ', error)
    }
}

export default {favoritar, buscar_favorito_id, buscar_favoritos}