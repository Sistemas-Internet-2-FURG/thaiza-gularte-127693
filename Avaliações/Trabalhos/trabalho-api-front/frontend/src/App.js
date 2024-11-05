// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Cadastro from './pages/cadastro';
import Home from './pages/home';
import Login from './pages/login';

function App() {
  return (
    <Router>
      <Routes>
        {/* Definindo a rota '/' para a página de cadastro */}
        <Route path="/" element={<Cadastro />} />
        
        {/* Definindo a rota '/home' para a página principal ou dashboard */}
        <Route path="/home" element={<Home />} />
        
        {/* Definindo a rota '/login' para a página de login */}
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
