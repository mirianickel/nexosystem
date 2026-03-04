<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EcoNexo's System - Produtividade Guiada e Inteligente</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2D5BFF;
            --primary-dark: #1A3FCC;
            --secondary: #00D9B4;
            --accent: #FF6B35;
            --dark: #0F172A;
            --gray: #64748B;
            --light-gray: #F1F5F9;
            --white: #FFFFFF;
            --gradient: linear-gradient(135deg, #2D5BFF 0%, #00D9B4 100%);
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'DM Sans', sans-serif;
            color: var(--dark);
            line-height: 1.6;
            overflow-x: hidden;
            background: var(--white);
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Sora', sans-serif;
            font-weight: 700;
            line-height: 1.2;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid rgba(45, 91, 255, 0.1);
            transition: all 0.3s ease;
        }

        nav.scrolled {
            box-shadow: var(--shadow-lg);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-family: 'Sora', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
            align-items: center;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .btn-nav {
            padding: 0.6rem 1.5rem;
            background: var(--gradient);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .btn-nav:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        /* Hero Section */
        #home {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding: 6rem 2rem 4rem;
            background: linear-gradient(135deg, #F8FAFF 0%, #F0F9FF 100%);
            position: relative;
            overflow: hidden;
        }

        #home::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(45, 91, 255, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            50% { transform: translate(-30px, 30px) rotate(5deg); }
        }

        .hero-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
            position: relative;
            z-index: 1;
        }

        .hero-content h1 {
            font-size: 3.5rem;
            margin-bottom: 1.5rem;
            color: var(--dark);
            animation: fadeInUp 0.8s ease-out;
        }

        .hero-content .highlight {
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-content p {
            font-size: 1.25rem;
            color: var(--gray);
            margin-bottom: 2rem;
            animation: fadeInUp 0.8s ease-out 0.2s backwards;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            animation: fadeInUp 0.8s ease-out 0.4s backwards;
        }

        .btn-primary, .btn-secondary {
            padding: 1rem 2rem;
            font-size: 1.1rem;
            font-weight: 600;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: var(--gradient);
            color: white;
            box-shadow: var(--shadow);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-lg);
        }

        .btn-secondary {
            background: white;
            color: var(--primary);
            border: 2px solid var(--primary);
        }

        .btn-secondary:hover {
            background: var(--primary);
            color: white;
        }

        .hero-visual {
            position: relative;
            animation: fadeIn 1s ease-out 0.6s backwards;
        }

        .visual-card {
            background: white;
            border-radius: 20px;
            padding: 2rem;
            box-shadow: var(--shadow-lg);
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease;
        }

        .visual-card:hover {
            transform: translateX(10px);
        }

        .visual-card h3 {
            color: var(--primary);
            margin-bottom: 0.5rem;
            font-size: 1.2rem;
        }

        .visual-card p {
            color: var(--gray);
            font-size: 0.95rem;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Features Section */
        #features {
            padding: 6rem 2rem;
            background: white;
        }

        .section-header {
            text-align: center;
            max-width: 700px;
            margin: 0 auto 4rem;
        }

        .section-header h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--dark);
        }

        .section-header p {
            font-size: 1.1rem;
            color: var(--gray);
        }

        .features-grid {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
        }

        .feature-card {
            background: var(--light-gray);
            padding: 2.5rem;
            border-radius: 16px;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            border-color: var(--primary);
            box-shadow: var(--shadow-lg);
            background: white;
        }

        .feature-icon {
            width: 60px;
            height: 60px;
            background: var(--gradient);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }

        .feature-card h3 {
            margin-bottom: 1rem;
            font-size: 1.4rem;
        }

        .feature-card p {
            color: var(--gray);
            line-height: 1.7;
        }

        /* Login Section */
        #login {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 6rem 2rem;
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            position: relative;
        }

        #login::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><rect width="1" height="1" fill="%232D5BFF" opacity="0.1"/></svg>') repeat;
            opacity: 0.3;
        }

        .login-container {
            background: white;
            border-radius: 24px;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            overflow: hidden;
            max-width: 900px;
            width: 100%;
            display: grid;
            grid-template-columns: 1fr 1fr;
            position: relative;
            z-index: 1;
        }

        .login-visual {
            background: var(--gradient);
            padding: 3rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: white;
        }

        .login-visual h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }

        .login-visual p {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-bottom: 2rem;
        }

        .login-stats {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }

        .stat {
            background: rgba(255, 255, 255, 0.2);
            padding: 1.5rem;
            border-radius: 12px;
            backdrop-filter: blur(10px);
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
        }

        .login-form {
            padding: 3rem;
        }

        .login-form h2 {
            margin-bottom: 0.5rem;
            font-size: 2rem;
        }

        .login-form p {
            color: var(--gray);
            margin-bottom: 2rem;
        }

        .form-tabs {
            display: flex;
            gap: 1rem;
            margin-bottom: 2rem;
        }

        .tab {
            flex: 1;
            padding: 0.8rem;
            background: var(--light-gray);
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .tab.active {
            background: var(--primary);
            color: white;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: var(--dark);
        }

        .form-group input {
            width: 100%;
            padding: 0.9rem;
            border: 2px solid var(--light-gray);
            border-radius: 8px;
            font-size: 1rem;
            transition: border-color 0.3s ease;
        }

        .form-group input:focus {
            outline: none;
            border-color: var(--primary);
        }

        .form-submit {
            width: 100%;
            padding: 1rem;
            background: var(--gradient);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .form-submit:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .form-footer {
            margin-top: 1.5rem;
            text-align: center;
            font-size: 0.9rem;
            color: var(--gray);
        }

        .form-footer a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }

        /* About Section */
        #about {
            padding: 6rem 2rem;
            background: var(--light-gray);
        }

        .about-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .about-content h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
        }

        .about-content p {
            font-size: 1.1rem;
            color: var(--gray);
            margin-bottom: 1.5rem;
            line-height: 1.8;
        }

        .about-values {
            display: grid;
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .value-item {
            display: flex;
            gap: 1rem;
            align-items: flex-start;
        }

        .value-icon {
            width: 40px;
            height: 40px;
            background: var(--gradient);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 800;
            flex-shrink: 0;
        }

        .value-text h4 {
            margin-bottom: 0.3rem;
            font-size: 1.1rem;
        }

        .value-text p {
            font-size: 0.95rem;
            margin: 0;
        }

        .about-image {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: var(--shadow-lg);
        }

        .team-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
        }

        .team-member {
            background: var(--light-gray);
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
        }

        .member-avatar {
            width: 80px;
            height: 80px;
            background: var(--gradient);
            border-radius: 50%;
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 2rem;
            font-weight: 800;
        }

        .team-member h4 {
            margin-bottom: 0.3rem;
        }

        .team-member p {
            font-size: 0.9rem;
            color: var(--gray);
            margin: 0;
        }

        /* LGPD Section */
        #lgpd {
            padding: 6rem 2rem;
            background: white;
        }

        .lgpd-container {
            max-width: 900px;
            margin: 0 auto;
        }

        .lgpd-container h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            text-align: center;
        }

        .lgpd-intro {
            text-align: center;
            color: var(--gray);
            margin-bottom: 3rem;
            font-size: 1.1rem;
        }

        .lgpd-content {
            background: var(--light-gray);
            padding: 3rem;
            border-radius: 16px;
            border-left: 4px solid var(--primary);
        }

        .lgpd-section {
            margin-bottom: 2.5rem;
        }

        .lgpd-section:last-child {
            margin-bottom: 0;
        }

        .lgpd-section h3 {
            color: var(--primary);
            margin-bottom: 1rem;
            font-size: 1.4rem;
        }

        .lgpd-section p {
            color: var(--dark);
            line-height: 1.8;
            margin-bottom: 1rem;
        }

        .lgpd-section ul {
            list-style: none;
            padding-left: 0;
        }

        .lgpd-section li {
            padding: 0.8rem 0;
            color: var(--dark);
            position: relative;
            padding-left: 2rem;
        }

        .lgpd-section li::before {
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--secondary);
            font-weight: 800;
            font-size: 1.2rem;
        }

        .contact-box {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            margin-top: 2rem;
            border: 2px solid var(--primary);
        }

        .contact-box h4 {
            margin-bottom: 1rem;
            color: var(--primary);
        }

        .contact-box p {
            margin: 0.5rem 0;
            color: var(--dark);
        }

        .contact-box a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
        }

        /* Footer */
        footer {
            background: var(--dark);
            color: white;
            padding: 3rem 2rem 2rem;
        }

        .footer-container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .footer-grid {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-brand h3 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .footer-brand p {
            color: var(--gray);
            line-height: 1.7;
        }

        .footer-links h4 {
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }

        .footer-links ul {
            list-style: none;
        }

        .footer-links li {
            margin-bottom: 0.8rem;
        }

        .footer-links a {
            color: var(--gray);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-links a:hover {
            color: var(--secondary);
        }

        .footer-bottom {
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            padding-top: 2rem;
            text-align: center;
        }

        .footer-bottom p {
            color: var(--gray);
            font-size: 0.9rem;
        }

        /* Responsive */
        @media (max-width: 968px) {
            .hero-container,
            .about-container,
            .login-container {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .features-grid {
                grid-template-columns: 1fr;
            }

            .footer-grid {
                grid-template-columns: 1fr 1fr;
            }

            .hero-content h1 {
                font-size: 2.5rem;
            }

            .nav-links {
                display: none;
            }
        }

        @media (max-width: 640px) {
            .footer-grid {
                grid-template-columns: 1fr;
            }

            .hero-buttons {
                flex-direction: column;
            }

            .login-stats {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav id="navbar">
        <div class="nav-container">
            <a href="#home" class="logo">EcoNexo</a>
            <ul class="nav-links">
                <li><a href="#home">Início</a></li>
                <li><a href="#features">Recursos</a></li>
                <li><a href="#about">Quem Somos</a></li>
                <li><a href="#lgpd">Privacidade</a></li>
                <li><a href="#login" class="btn-nav">Entrar</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home">
        <div class="hero-container">
            <div class="hero-content">
                <h1>
                    Produtividade <span class="highlight">Guiada</span> e Inteligente
                </h1>
                <p>
                    Descubra seu perfil de trabalho, receba tarefas personalizadas e alcance uma autonomia produtiva real com o suporte de IA.
                </p>
                <div class="hero-buttons">
                    <a href="#login" class="btn-primary">Começar Agora</a>
                    <a href="#features" class="btn-secondary">Saiba Mais</a>
                </div>
            </div>
            <div class="hero-visual">
                <div class="visual-card">
                    <h3>🎯 Executor</h3>
                    <p>Focado em ação rápida e resultados imediatos</p>
                </div>
                <div class="visual-card">
                    <h3>📋 Organizador</h3>
                    <p>Estrutura processos e planeja com precisão</p>
                </div>
                <div class="visual-card">
                    <h3>💡 Criativo</h3>
                    <p>Inova constantemente e explora novas ideias</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features">
        <div class="section-header">
            <h2>Como Funciona</h2>
            <p>Sistema completo para desenvolver sua autonomia produtiva</p>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Análise de Perfil</h3>
                <p>Questionário inteligente identifica se você é Executor, Organizador ou Criativo, revelando suas forças naturais de trabalho.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>Tarefas Personalizadas</h3>
                <p>Receba uma vitrine de tarefas adaptadas ao seu perfil, com execução guiada passo a passo pela IA.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <h3>IAP - Índice de Autonomia</h3>
                <p>Acompanhe sua evolução com o Índice de Autonomia Produtiva, medindo seu progresso real em cada sessão.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3>Assistente IA</h3>
                <p>Chat integrado com inteligência artificial para tirar dúvidas, receber dicas e ajustes personalizados durante a execução.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💾</div>
                <h3>Histórico Completo</h3>
                <p>Todas as suas sessões são salvas para você visualizar evolução, padrões e pontos de melhoria ao longo do tempo.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3>Segurança Total</h3>
                <p>Seus dados são protegidos conforme a LGPD, com total transparência sobre coleta, uso e armazenamento de informações.</p>
            </div>
        </div>
    </section>

    <!-- Login Section -->
    <section id="login">
        <div class="login-container">
            <div class="login-visual">
                <h2>Bem-vindo ao EcoNexo</h2>
                <p>Junte-se a milhares de pessoas que já descobriram seu potencial produtivo.</p>
                <div class="login-stats">
                    <div class="stat">
                        <div class="stat-number">12K+</div>
                        <div class="stat-label">Usuários Ativos</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">85%</div>
                        <div class="stat-label">Taxa de Conclusão</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">4.8★</div>
                        <div class="stat-label">Avaliação Média</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">50K+</div>
                        <div class="stat-label">Tarefas Completadas</div>
                    </div>
                </div>
            </div>
            <div class="login-form">
                <h2>Acesse sua conta</h2>
                <p>Entre ou crie uma conta para começar</p>
                
                <div class="form-tabs">
                    <button class="tab active" onclick="switchTab('login')">Entrar</button>
                    <button class="tab" onclick="switchTab('signup')">Criar Conta</button>
                </div>

                <form id="loginForm">
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" placeholder="seu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label>Senha</label>
                        <input type="password" placeholder="••••••••" required>
                    </div>
                    <button type="submit" class="form-submit">Entrar</button>
                    <div class="form-footer">
                        Esqueceu sua senha? <a href="#">Recuperar</a>
                    </div>
                </form>

                <form id="signupForm" style="display: none;">
                    <div class="form-group">
                        <label>Nome Completo</label>
                        <input type="text" placeholder="Seu nome" required>
                    </div>
                    <div class="form-group">
                        <label>Email</label>
                        <input type="email" placeholder="seu@email.com" required>
                    </div>
                    <div class="form-group">
                        <label>Senha</label>
                        <input type="password" placeholder="Mínimo 8 caracteres" required>
                    </div>
                    <button type="submit" class="form-submit">Criar Conta</button>
                    <div class="form-footer">
                        Ao criar conta, você concorda com nossa <a href="#lgpd">Política de Privacidade</a>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <div class="about-container">
            <div class="about-content">
                <h2>Quem Somos</h2>
                <p>
                    O <strong>EcoNexo's System</strong> nasceu da observação de um problema comum: muitas pessoas sabem o que precisam fazer, mas não sabem <em>como</em> começar ou manter a consistência.
                </p>
                <p>
                    Criamos uma plataforma que não apenas identifica seu perfil de trabalho natural (Executor, Organizador ou Criativo), mas também oferece <strong>execução guiada por IA</strong> — transformando intenção em ação real.
                </p>
                <p>
                    Nossa missão é simples: <strong>desenvolver autonomia produtiva real</strong> através de tecnologia acessível, personalizada e baseada em ciência comportamental.
                </p>

                <div class="about-values">
                    <div class="value-item">
                        <div class="value-icon">🎯</div>
                        <div class="value-text">
                            <h4>Foco no Resultado</h4>
                            <p>Medimos sucesso pela quantidade de tarefas concluídas, não apenas iniciadas.</p>
                        </div>
                    </div>
                    <div class="value-item">
                        <div class="value-icon">🤝</div>
                        <div class="value-text">
                            <h4>Personalização</h4>
                            <p>Cada pessoa é única. Nosso sistema se adapta ao seu jeito de trabalhar.</p>
                        </div>
                    </div>
                    <div class="value-item">
                        <div class="value-icon">🔐</div>
                        <div class="value-text">
                            <h4>Transparência Total</h4>
                            <p>Seus dados são seus. Total conformidade com LGPD e privacidade garantida.</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="about-image">
                <h3 style="margin-bottom: 1.5rem; text-align: center;">Nossa Equipe</h3>
                <div class="team-grid">
                    <div class="team-member">
                        <div class="member-avatar">M</div>
                        <h4>Mirian Nickel</h4>
                        <p>Co-fundadora & CEO</p>
                    </div>
                    <div class="team-member">
                        <div class="member-avatar">E</div>
                        <h4>Equipe Dev</h4>
                        <p>Tecnologia & Produto</p>
                    </div>
                    <div class="team-member">
                        <div class="member-avatar">P</div>
                        <h4>Psicologia</h4>
                        <p>Pesquisa & UX</p>
                    </div>
                    <div class="team-member">
                        <div class="member-avatar">A</div>
                        <h4>IA & Data</h4>
                        <p>Machine Learning</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- LGPD Section -->
    <section id="lgpd">
        <div class="lgpd-container">
            <h2>Lei Geral de Proteção de Dados</h2>
            <p class="lgpd-intro">
                Levamos sua privacidade a sério. Esta política explica como coletamos, usamos e protegemos seus dados pessoais em total conformidade com a LGPD (Lei nº 13.709/2018).
            </p>

            <div class="lgpd-content">
                <div class="lgpd-section">
                    <h3>1. Dados Coletados</h3>
                    <p>Para fornecer nossos serviços, coletamos apenas as informações essenciais:</p>
                    <ul>
                        <li><strong>Dados de cadastro:</strong> nome, email e senha (criptografada)</li>
                        <li><strong>Dados de perfil:</strong> respostas ao questionário de produtividade</li>
                        <li><strong>Dados de uso:</strong> histórico de tarefas completadas e IAP ao longo do tempo</li>
                        <li><strong>Dados técnicos:</strong> endereço IP, tipo de navegador (apenas para segurança)</li>
                    </ul>
                </div>

                <div class="lgpd-section">
                    <h3>2. Como Usamos Seus Dados</h3>
                    <p>Utilizamos suas informações exclusivamente para:</p>
                    <ul>
                        <li>Fornecer acesso personalizado à plataforma</li>
                        <li>Identificar seu perfil de produtividade (Executor, Organizador, Criativo)</li>
                        <li>Sugerir tarefas e orientações personalizadas via IA</li>
                        <li>Calcular e exibir seu Índice de Autonomia Produtiva (IAP)</li>
                        <li>Melhorar continuamente a experiência do usuário</li>
                        <li>Enviar notificações relevantes (com seu consentimento)</li>
                    </ul>
                </div>

                <div class="lgpd-section">
                    <h3>3. Armazenamento e Segurança</h3>
                    <p>Seus dados são protegidos com tecnologias de segurança de ponta:</p>
                    <ul>
                        <li>Criptografia SSL/TLS em todas as conexões</li>
                        <li>Senhas armazenadas com hash criptográfico (bcrypt)</li>
                        <li>Servidores seguros com backup diário</li>
                        <li>Acesso restrito apenas à equipe autorizada</li>
                        <li>Conformidade total com padrões internacionais de segurança</li>
                    </ul>
                </div>

                <div class="lgpd-section">
                    <h3>4. Seus Direitos (LGPD)</h3>
                    <p>Você tem total controle sobre seus dados e pode:</p>
                    <ul>
                        <li><strong>Acessar:</strong> solicitar cópia de todos os dados armazenados</li>
                        <li><strong>Corrigir:</strong> atualizar informações desatualizadas ou incorretas</li>
                        <li><strong>Deletar:</strong> excluir permanentemente sua conta e dados</li>
                        <li><strong>Portabilidade:</strong> exportar seus dados em formato legível</li>
                        <li><strong>Revogar consentimento:</strong> retirar autorização de uso a qualquer momento</li>
                        <li><strong>Oposição:</strong> opor-se a processamento de dados específicos</li>
                    </ul>
                </div>

                <div class="lgpd-section">
                    <h3>5. Compartilhamento de Dados</h3>
                    <p>
                        <strong>Nunca vendemos seus dados.</strong> Compartilhamento ocorre apenas quando estritamente necessário:
                    </p>
                    <ul>
                        <li>Provedores de infraestrutura cloud (servidores seguros)</li>
                        <li>Serviços de IA para processamento de chat (dados anonimizados)</li>
                        <li>Quando exigido por lei ou ordem judicial</li>
                    </ul>
                    <p>
                        Todos os parceiros assinam acordos de confidencialidade e proteção de dados.
                    </p>
                </div>

                <div class="lgpd-section">
                    <h3>6. Cookies e Rastreamento</h3>
                    <p>
                        Utilizamos cookies apenas para funcionalidade essencial (manter você logado) e análise de desempenho técnico. Você pode gerenciar cookies nas configurações do navegador.
                    </p>
                </div>

                <div class="lgpd-section">
                    <h3>7. Alterações nesta Política</h3>
                    <p>
                        Esta política pode ser atualizada periodicamente. Notificaremos mudanças significativas por email. Versão atual: <strong>Março de 2026</strong>.
                    </p>
                </div>

                <div class="contact-box">
                    <h4>📧 Entre em Contato - Encarregado de Dados (DPO)</h4>
                    <p>Para exercer seus direitos ou esclarecer dúvidas sobre privacidade:</p>
                    <p>
                        <strong>Email:</strong> <a href="mailto:privacidade@econexo.com">privacidade@econexo.com</a><br>
                        <strong>Tempo de resposta:</strong> Até 5 dias úteis
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>EcoNexo's System</h3>
                    <p>
                        Plataforma de produtividade guiada por IA que transforma seu potencial em resultados reais. Descubra seu perfil, execute tarefas e alcance autonomia produtiva.
                    </p>
                </div>
                <div class="footer-links">
                    <h4>Produto</h4>
                    <ul>
                        <li><a href="#features">Recursos</a></li>
                        <li><a href="#login">Começar Grátis</a></li>
                        <li><a href="#">Planos e Preços</a></li>
                        <li><a href="#">Roadmap</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Empresa</h4>
                    <ul>
                        <li><a href="#about">Quem Somos</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Carreiras</a></li>
                        <li><a href="#">Imprensa</a></li>
                    </ul>
                </div>
                <div class="footer-links">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="#lgpd">LGPD & Privacidade</a></li>
                        <li><a href="#">Termos de Uso</a></li>
                        <li><a href="#">Cookies</a></li>
                        <li><a href="mailto:privacidade@econexo.com">Contato DPO</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 EcoNexo's System. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <script>
        // Navbar scroll effect
        window.addEventListener('scroll', () => {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Tab switching
        function switchTab(tab) {
            const tabs = document.querySelectorAll('.tab');
            const loginForm = document.getElementById('loginForm');
            const signupForm = document.getElementById('signupForm');

            tabs.forEach(t => t.classList.remove('active'));
            
            if (tab === 'login') {
                tabs[0].classList.add('active');
                loginForm.style.display = 'block';
                signupForm.style.display = 'none';
            } else {
                tabs[1].classList.add('active');
                loginForm.style.display = 'none';
                signupForm.style.display = 'block';
            }
        }

        // Form submissions (placeholder)
        document.getElementById('loginForm').addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Funcionalidade de login será conectada ao backend da aplicação Streamlit!');
        });

        document.getElementById('signupForm').addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Funcionalidade de cadastro será conectada ao backend da aplicação Streamlit!');
        });

        // Smooth scroll
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>
</body>
</html>
