async function comentario_feito(id_livro, id_usuario, comentario) {
    try {
        const formData = new FormData();
        formData.append("usuario_id", id_usuario);
        formData.append("livro_id", id_livro);
        formData.append("comentario", comentario);
        const response = await fetch(`http://127.0.0.1:5000/comentarios/criar`, {
            method: "POST",
            body: formData,
        });

        const data = await response.json();  // Converta a resposta para JSON
        return data.code;  // Retorne o código da resposta

    } catch (error) {
        console.log('Erro ao comentar o livro: ', error);
    }
}

async function buscar_comentarios() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/comentarios/buscar`, {
            method: "GET",
        });
        const data = await response.json();  // Converta a resposta para JSON
        return data;  // Retorne os dados dos comentários

    } catch (error) {
        console.log('Erro ao buscar os comentários: ', error);
    }
}

async function buscar_comentario_id(id) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/comentarios/buscar/${id}`, {
            method: "GET",  // Mudei para GET, pois é uma requisição de busca
        });
        const data = await response.json();  // Converta a resposta para JSON
        return data;  // Retorne os dados

    } catch (error) {
        console.log('Erro ao buscar o comentário: ', error);
    }
}

export { comentario_feito, buscar_comentario_id, buscar_comentarios };
