import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom'
import {cadastrar} from '../controllers/usuarios_controllers'
import {home} from '../controllers/usuarios_controllers'

function Cadastro() {

  const [nome, setNome] = useState('')
  const [email, setEmail] = useState('')
  const [senha, setSenha] = useState('')
  const navigate = useNavigate()

  async function verificarToken(token) {
    const token_valido = await home(token)

    if(token_valido.status === 200){
      return true
    } else {
      return false
    }
  }

  useEffect(() => {
    const token = localStorage.getItem('token')
    const tokenValido = verificarToken(token)
    if (tokenValido === true) {
      console.log('Token está valido!!')
      navigate('/home')
    } else {
      console.log('Token invalido/expirado! Mnada de volta pro login.')
      localStorage.clear()
      navigate('/');
    }
}, [navigate]);

  const cadastrar_usuario = async (e) => {
    e.preventDefault(); // Impede o reload da página ao submeter o form
    console.log('Iniciando cadastro do usuário...');
    
    try {
        const response = await cadastrar(nome, email, senha); // Agora `response` é o objeto completo

        console.log('Resposta da API:', response);
        
        if (response.status === 200) { // Verifica se o código de status é 200
            console.log('Usuário cadastrado.');
            navigate('/login'); // Redireciona para a tela de login após o cadastro
        } else {
            const errorMsg = await response.json(); // Lê a mensagem de erro do JSON, se houver
            console.log('Erro ao cadastrar usuário:', errorMsg.msg || "Erro desconhecido");
        }
    } catch (error) {
        console.error('Erro ao tentar cadastrar o usuário:', error);
        console.log('Ocorreu um erro ao tentar cadastrar o usuário.');
    }
};

  return (
    <div style={styles.body}>
      <div style={styles.card}>
        <h3 style={styles.title}>Cadastro</h3>
        <form onSubmit={cadastrar_usuario}>
          <div style={styles.formGroup}>
            <label htmlFor="nome" style={styles.label}>Nome</label>
            <input type="text" id="nome" placeholder="Digite seu nome" style={styles.input} onChange={(e) => setNome(e.target.value)} />
          </div>

          <div style={styles.formGroup}>
            <label htmlFor="email" style={styles.label}>Email</label>
            <input type="email" id="email" placeholder="Digite seu email" style={styles.input} onChange={(e) => setEmail(e.target.value)}/>
          </div>

          <div style={styles.formGroup}>
            <label htmlFor="senha" style={styles.label}>Senha</label>
            <input type="password" id="senha" placeholder="Crie uma senha" style={styles.input} onChange={(e) => setSenha(e.target.value)} />
          </div>
          <button type="submit" style={styles.btnSubmit}>Cadastrar</button>
          <button type='button' onClick={() => {navigate('/login')}} style={styles.btnSubmit}>Acesar</button>
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
    backgroundColor: '#ccd0cf',
    fontFamily: 'Arial, sans-serif',
  },
  card: {
    backgroundColor: '#4a5c6a',
    padding: '2rem',
    width: '350px',
    borderRadius: '8px',
    boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.3)',
    color: '#06141b',
    textAlign: 'center',
  },
  title: {
    marginBottom: '1.5rem',
    color: '#06141b',
  },
  formGroup: {
    marginBottom: '1rem',
    textAlign: 'left',
  },
  label: {
    display: 'block',
    fontWeight: 'bold',
    color: '#06141b',
    marginBottom: '0.5rem',
  },
  input: {
    width: '100%',
    padding: '0.5rem',
    border: 'none',
    borderRadius: '4px',
    backgroundColor: '#9ba8ab',
    color: '#06141b',
    fontSize: '1rem',
  },
  btnSubmit: {
    width: '100%',
    padding: '0.7rem',
    backgroundColor: '#ccd0cf',
    border: 'none',
    borderRadius: '4px',
    color: '#06141b',
    fontSize: '1rem',
    fontWeight: 'bold',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
    marginTop: '1rem',
  },
};

// Exporta o componente
export default Cadastro;
