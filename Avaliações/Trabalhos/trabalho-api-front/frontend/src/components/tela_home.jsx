import React, {useEffect, useState} from 'react'
import { useNavigate } from 'react-router-dom'
import {buscar_livros, buscar_livro_id} from '../controllers/livros_controllers'
import {favoritar, buscar_favoritos} from '../controllers/favoritos_controllers'
import {comentario_feito, buscar_comentarios} from '../controllers/comentarios_controllers'

function TelaInicial() {
    const navigate = useNavigate()
    const [livros, setLivros] = useState([]);
    const [usuario, setUsuario] = useState([])
    const [comentarios, setComentarios] = useState([])
    const [favoritos, setFavoritos] = useState([])
    const [showCommentPopup, setShowCommentPopup] = useState(false);
    const [currentBookId, setCurrentBookId] = useState(null);
    const [commentText, setCommentText] = useState('');
    
    useEffect(() => {
      const us = JSON.parse(localStorage.getItem('DadosUsuario'));
      setUsuario(us)
      if (!us) {
          navigate('/login');
      } else {
          pegar_dados_banco(); 
      }
  }, [navigate]);

  const handleCommentClick = (livroId) => {
    setCurrentBookId(livroId);
    setShowCommentPopup(true);
  };

  const handleCommentSubmit = async (e) => {
    e.preventDefault();
    const comentar = await comentario_feito(usuario[1], currentBookId, commentText)
    setCommentText('');
    setShowCommentPopup(false);
  };



  const pegar_dados_banco = async () => {
      const livros = await buscar_livros()
      if (livros && livros.code === 200) {
          setLivros(livros.dados)
      } else {
          console.error('Erro ao listar livros:', livros.msg)
      }

      const coms = await buscar_comentarios()
      if (coms && coms.code === 200) {
          setComentarios(coms.dados)
      } else {
          console.error('Erro ao listar coms:', coms)
      }

      const favoritos = await buscar_favoritos()
      const favs = []
      if (favoritos && favoritos.code === 200) { 
          favoritos.dados.map(async (fav) => {
            const livro = await buscar_livro_id(fav.livro_id);
            favs.push({
              usuario: fav.usuario_id,
              titulo: livro.data.dados[1]
            })
          })
          setFavoritos(favs)
      } else {
          console.error('Erro ao listar favoritos:', favoritos)
      }

  };



  return (
    <div style={styles.body}>
      <header style={styles.header}>
        <h1>Bem-vindo, {usuario[1]}</h1>
      </header>

      <div style={styles.container}>
        <div style={styles.bookList}>
          <h2>Lista de Livros</h2>
          <ul style={styles.ul}>
            {livros.map((livro) => (
              <li style={styles.listItem} key={livro.id}>
                <span>{livro.titulo} ({livro.ano_publicacao})</span>

                <div style={styles.buttonContainer}>
                  <button 
                    onClick={() => handleCommentClick(livro.id)} 
                    style={styles.favoritarButton}
                  >
                    Comentar
                  </button>

                  <button 
                    onClick={() => {favoritar(livro.id, usuario[0])}} 
                    style={styles.favoritarButton}
                  >
                    Favoritar
                  </button>
                </div>
              </li>
            ))}
          </ul>
        </div>

        <div style={styles.sidebar}>
          <div style={styles.favorites}>
            <h2>Livros Favoritos</h2>
            <ul style={styles.ul}>
              {favoritos.map((favorito) => (
                <li key={favorito.usuario}>
                  {favorito.titulo}
                </li>
              ))}
            </ul>
          </div>

          <div style={styles.comments}>
            <h2>Comentários</h2>
            <ul style={styles.ul}>
              {comentarios.map((comentario) => (
                <li className={styles.listItem} key={comentario.id}>
                  Comentário de {comentario.usuario_id}: <br></br>
                  {comentario.comentario} {/* Acesse a propriedade 'comentario' */}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {showCommentPopup && (
        <div style={styles.popup}>
          <div style={styles.popupContent}>
            <h3>Adicionar Comentário</h3>
            <form onSubmit={handleCommentSubmit}>
              <textarea
                value={commentText}
                onChange={(e) => setCommentText(e.target.value)}
                rows="4"
                style={styles.textarea}
                placeholder="Digite seu comentário..."
                required
              />
              <div style={styles.buttonGroup}>
                <button type="submit" style={styles.submitButton}>Enviar</button>
                <button type="button" onClick={() => setShowCommentPopup(false)} style={styles.cancelButton}>Cancelar</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};

// Estilos em um objeto de estilos
const styles = {
  body: {
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#121212',
    color: '#ffffff',
    margin: 0,
    padding: 0,
  },
  header: {
    backgroundColor: '#6a1b9a',
    padding: '20px',
    textAlign: 'center',
  },
  container: {
    display: 'flex',
    padding: '20px',
  },
  bookList: {
    flex: 2,
    marginRight: '20px',
  },
  sidebar: {
    flex: 1,
  },
  favorites: {
    backgroundColor: '#3f51b5',
    marginBottom: '20px',
    padding: '15px',
    borderRadius: '5px',
  },
  comments: {
    backgroundColor: '#3f51b5',
    padding: '15px',
    borderRadius: '5px',
  },
  ul: {
    listStyleType: 'none',
    padding: 0,
  },
  listItem: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '10px',
  },
  buttonContainer: {
    display: 'flex',
    justifyContent: 'flex-end', // Alinha os botões à direita
  },
  favoritarButton: {
    marginLeft: '10px',
    padding: '5px 10px',
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  popup: {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    zIndex: 1000,
  },
  popupContent: {
    backgroundColor: 'white',
    padding: '20px',
    borderRadius: '5px',
    width: '400px',
  },
  textarea: {
    width: '100%',
    marginBottom: '10px',
    borderRadius: '5px',
    border: '1px solid #ccc',
    padding: '5px',
  },
  buttonGroup: {
    display: 'flex',
    justifyContent: 'space-between',
  },
  submitButton: {
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    padding: '10px',
    cursor: 'pointer',
  },
  cancelButton: {
    backgroundColor: '#f44336',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    padding: '10px',
    cursor: 'pointer',
  },
};

// Exporta o componente
export default TelaInicial;
