import React from 'react';

function TelaInicial({ nomeUsuario }) {
  return (
    <div style={styles.body}>
      <header style={styles.header}>
        <h1>Bem-vindo, {nomeUsuario}</h1>
      </header>

      <div style={styles.container}>
        <div style={styles.bookList}>
          <h2>Lista de Livros</h2>
          <ul style={styles.ul}>
            <li style={styles.listItem}>Livro 1</li>
            <li style={styles.listItem}>Livro 2</li>
            <li style={styles.listItem}>Livro 3</li>
            <li style={styles.listItem}>Livro 4</li>
            <li style={styles.listItem}>Livro 5</li>
          </ul>
        </div>

        <div style={styles.sidebar}>
          <div style={styles.favorites}>
            <h2>Livros Favoritos</h2>
            <ul style={styles.ul}>
              <li style={styles.listItem}>Livro Favorito 1</li>
              <li style={styles.listItem}>Livro Favorito 2</li>
            </ul>
          </div>

          <div style={styles.comments}>
            <h2>Comentários</h2>
            <p>Este é um espaço para comentários sobre os livros.</p>
          </div>
        </div>
      </div>
    </div>
  );
}

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
    backgroundColor: '#4caf50',
    margin: '5px 0',
    padding: '10px',
    borderRadius: '5px',
  },
};

// Exporta o componente
export default TelaInicial;
