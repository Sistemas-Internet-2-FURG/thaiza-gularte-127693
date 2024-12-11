import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { login } from '../controllers/usuarios_controllers';

function Login() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [senhaBanco, setSenhaBanco] = useState('');
  const [emailValido, setEmailValido] = useState(false);
  const [mensagemErro, setMensagemErro] = useState('');
  const [corEmail, setCorEmail] = useState('#11212d'); // Cor inicial neutra
  const [corSenha, setCorSenha] = useState('#11212d'); // Cor inicial neutra
  const [senhaValida, setSenhaValida] = useState(false); // Controla a visibilidade do botão
  const [mostrarBotaoFalso, setMostrarBotaoFalso] = useState(true); // Controla o botão falso

  const navigate = useNavigate();

  const verificarEmail = async (email) => {
    setEmail(email); // Atualiza o estado imediatamente
    if (!email.includes('@') || email.length < 5) {
      // Requisito mínimo básico para email
      setCorEmail('#ff4d4d'); // Vermelho se o email parecer inválido
      setEmailValido(false);
      setMensagemErro('Formato de email inválido');
      return;
    }

    try {
      const response = await fetch('http://localhost:5000/usuarios/verificar_email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email }),
      });

      const data = await response.json();

      if (response.status === 200) {
        setEmailValido(true);
        setSenhaBanco(data.senha);
        setMensagemErro('');
        setCorEmail('#008000'); // Verde se válido
      } else {
        setEmailValido(false);
        setMensagemErro('Email não encontrado');
        setCorEmail('#ff4d4d'); // Vermelho se inválido
      }
    } catch (error) {
      console.error('Erro ao verificar email:', error);
      setMensagemErro('Erro ao verificar email');
      setCorEmail('#ff4d4d'); // Vermelho no erro
    }
  };

  const validarSenha = (senhaDigitada) => {
    setSenha(senhaDigitada);  // Atualiza o estado da senha enquanto o usuário digita
    
    // Mostra a mensagem de erro e esconde o botão falso quando o usuário começa a digitar a senha
    if (senhaDigitada.length > 0) {
      setMostrarBotaoFalso(false); // Esconde o botão falso assim que o usuário começa a digitar a senha
    }
    
    // Se a senha não começar com o que foi digitado, aplica cor vermelha
    if (!senhaBanco.startsWith(senhaDigitada)) {
      setMensagemErro('Senha incorreta');
      setCorSenha('#ff4d4d'); // Vermelho se a senha estiver errada
      setSenhaValida(false); // Mantém o botão escondido
    } else {
      setMensagemErro('');  // Limpa a mensagem de erro se a senha estiver correta
      setCorSenha('#008000'); // Verde se a senha estiver correta
      setSenhaValida(true); // Exibe o botão
    }
  };

  const realizar_login = async (e) => {
    e.preventDefault();

    if (!emailValido) {
      setMensagemErro('Verifique o email antes de prosseguir');
      setCorEmail('#ff4d4d');
      return;
    }

    try {
      const response = await login(email, senha);

      if (response.code === 200) {
        navigate('/home');
      } else {
        setMensagemErro(response.msg || 'Erro desconhecido');
      }
    } catch (error) {
      console.error('Erro no login:', error);
      setMensagemErro('Erro ao realizar login');
    }
  };

  return (
    <div style={styles.body}>
      <div style={styles.card}>
        <h3 style={styles.title}>Login</h3>
        <form onSubmit={realizar_login}>
          <div style={styles.formGroup}>
            <label htmlFor="email" style={styles.label}>Email</label>
            <input
              type="email"
              id="email"
              placeholder="Digite seu email"
              style={{ ...styles.input, borderColor: corEmail }}
              value={email}
              onChange={(e) => verificarEmail(e.target.value)} // Valida enquanto digita
            />
          </div>
          <div style={styles.formGroup}>
            <label htmlFor="senha" style={styles.label}>Senha</label>
            <input
              type="password"
              id="senha"
              placeholder="Digite sua senha"
              style={{ ...styles.input, borderColor: corSenha }}
              value={senha}
              disabled={!emailValido}
              onChange={(e) => validarSenha(e.target.value)} // Valida enquanto digita
            />
          </div>
          {mensagemErro && <p style={styles.error}>{mensagemErro}</p>}
          
          {/* Exibe o botão falso com a mensagem enquanto o usuário não começar a digitar */}
          {mostrarBotaoFalso && (
            <button type="button" style={styles.btnFalso} disabled>
              Entrar
            </button>
          )}

          {/* Botão de entrar só visível se a senha for válida */}
          {senhaValida && <button type="submit" style={styles.btnSubmit}>Entrar</button>}
          <button onClick={() => { navigate('/'); }} style={styles.btnSubmit}>Cadastrar</button>
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
    color: '#ccd0cf',
  },
  formGroup: {
    marginBottom: '1rem',
    textAlign: 'left',
  },
  label: {
    display: 'block',
    fontWeight: 'bold',
    color: '#ccd0cf',
    marginBottom: '0.5rem',
  },
  input: {
    width: '93%',
    padding: '0.5rem',
    border: '2px solid', // Define a espessura da borda
    borderRadius: '4px',
    backgroundColor: '#9ba8ab',
    color: '#06141b',
    fontSize: '1rem',
    transition: 'border-color 0.1s ease', // Transição suave para a cor da borda
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
  btnFalso: {
    width: '100%',
    padding: '0.7rem',
    backgroundColor: '#ccd0cf',  // Fundo vermelho claro
    border: 'none',
    borderRadius: '4px',
    color: '#06141b',  // Texto vermelho mais escuro
    fontSize: '1rem',
    fontWeight: 'bold',
    cursor: 'not-allowed',
    marginTop: '1rem',
  },
  error: {
    backgroundColor: '#f8d7da',  // Fundo vermelho claro
    color: '#721c24',  // Texto vermelho mais escuro
    padding: '0.5rem',
    borderRadius: '4px',
    fontSize: '1rem',
    textAlign: 'center',
    marginTop: '1rem',
  },
};

export default Login;
