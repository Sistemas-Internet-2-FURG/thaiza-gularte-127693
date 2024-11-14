import React, { useEffect } from 'react';

// Definindo o componente HeartJump
const HeartJump = ({ onAnimationEnd }) => {
  useEffect(() => {
    const timer = setTimeout(onAnimationEnd, 600); // Duração da animação
    return () => clearTimeout(timer);
  }, [onAnimationEnd]);

  return <div style={styles.heart}>❤️</div>;
};

// Estilos do coração
const styles = {
  heart: {
    color: 'red',
    fontSize: '3rem',
    position: 'fixed', // Fixa o coração na tela
    top: '50%',        // Centraliza na tela
    left: '50%',
    transform: 'translate(-50%, -50%)',
    animation: 'jump 0.6s ease', // Define a animação
  },
  '@keyframes jump': {
    '0%, 100%': { transform: 'scale(1) translateY(0)' },
    '50%': { transform: 'scale(1.2) translateY(-10px)' },
  },
};

export default HeartJump;
