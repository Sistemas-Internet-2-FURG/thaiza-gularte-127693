async function favoritar(id_livro, id_usuario) {
    try {
        const formData = new FormData();
        formData.append("usuario_id", id_usuario);  // Use o nome correto
        formData.append("livro_id", id_livro);  // Use o nome correto
        const response = await fetch(`http://127.0.0.1:5000/favoritos/criar`, {
            method: "POST",
            body: formData,
        });

        const data = await response.json();  // Converta a resposta para JSON
        return data.code;  // Retorne o código da resposta

    } catch (error) {
        console.log('Erro ao favoritar o livro: ', error);
    }
}

async function buscar_favoritos() {
    try {
        const response = await fetch(`http://127.0.0.1:5000/favoritos/buscar`, {
            method: "GET",
        });
        const data = await response.json();  // Converta a resposta para JSON
        return data;  // Retorne os dados dos favoritos

    } catch (error) {
        console.log('Erro ao buscar os favoritos: ', error);
    }
}

async function buscar_favorito_id(id) {
    try { 
        const response = await fetch(`http://127.0.0.1:5000/favoritos/buscar/${id}`, {  // Corrigido para buscar pelo ID
            method: "GET",
        });
        const data = await response.json();  // Converta a resposta para JSON
        return data;  // Retorne os dados

    } catch (error) {
        console.log('Erro ao buscar o favorito: ', error);
    }
}

export {favoritar, buscar_favorito_id,buscar_favoritos}