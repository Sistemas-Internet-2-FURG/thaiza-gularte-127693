import {BASE_API} from '../resources/api'
import axios from 'axios'

async function buscar_livros() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/livros/buscar`, {
            method: "GET",
        });

        if (!response.ok) {
            // Se a resposta não for OK, lance um erro
            throw new Error(`Erro: ${response.status}`);
        }

        const data = await response.json(); // Converta a resposta para JSON
        return data; // Retorne os dados que foram retornados pela API
    } catch (error) {
        console.log('Erro ao buscar livros: ', error);
    }
}
async function buscar_livro_id(id) {
    try{
        const response = await axios.get(`http://127.0.0.1:5000/livros/buscar/${id}`)
        return response

    }catch(error){
        console.log('Erro ao pegar livro por id: ', error)
    }
}

export  {buscar_livros, buscar_livro_id}