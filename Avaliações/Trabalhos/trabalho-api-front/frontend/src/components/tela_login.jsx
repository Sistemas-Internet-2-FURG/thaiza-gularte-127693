import React from 'react';
import { useNavigate } from 'react-router-dom'

function Login() {
  const navigate = useNavigate()
  return (
    <div style={styles.body}>
      <div style={styles.card}>
        <h3 style={styles.title}>Login</h3>
        <form>
          <div style={styles.formGroup}>
            <label htmlFor="email" style={styles.label}>Email</label>
            <input type="email" id="email" placeholder="Digite seu email" style={styles.input} />
          </div>

          <div style={styles.formGroup}>
            <label htmlFor="senha" style={styles.label}>Senha</label>
            <input type="password" id="senha" placeholder="Digite sua senha" style={styles.input} />
          </div>

          <button type="submit" style={styles.btnSubmit}>Entrar</button>
          <button onClick={() => {navigate('/')}} style={styles.btnSubmit}>Cadastrar</button>

        </form>
      </div>
    </div>
  );
}

// Estilos em um objeto de estilos
const styles = {
  body: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
    margin: 0,
    backgroundColor: '#1c1033',
    fontFamily: 'Arial, sans-serif',
  },
  card: {
    backgroundColor: '#2d1b4e',
    padding: '2rem',
    width: '350px',
    borderRadius: '8px',
    boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.3)',
    color: '#8fedb4',
    textAlign: 'center',
  },
  title: {
    marginBottom: '1.5rem',
    color: '#8fedb4',
  },
  formGroup: {
    marginBottom: '1rem',
    textAlign: 'left',
  },
  label: {
    display: 'block',
    fontWeight: 'bold',
    color: '#8fedb4',
    marginBottom: '0.5rem',
  },
  input: {
    width: '100%',
    padding: '0.5rem',
    border: 'none',
    borderRadius: '4px',
    backgroundColor: '#1c1033',
    color: '#8fedb4',
    fontSize: '1rem',
  },
  btnSubmit: {
    width: '100%',
    padding: '0.7rem',
    backgroundColor: '#28a745',
    border: 'none',
    borderRadius: '4px',
    color: '#fff',
    fontSize: '1rem',
    fontWeight: 'bold',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
    marginTop: '1rem',
  },
};

// Exporta o componente
export default Login;
