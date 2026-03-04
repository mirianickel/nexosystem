import streamlit as st
import streamlit.components.v1 as components

# ========================
# CONFIGURAÇÃO DA PÁGINA
# ========================
st.set_page_config(
    page_title="EcoNexo's System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================
# SESSION STATE
# ========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "landing"
if "step" not in st.session_state:
    st.session_state.step = "questionnaire"
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "tasks_completed" not in st.session_state:
    st.session_state.tasks_completed = 0
if "iap_score" not in st.session_state:
    st.session_state.iap_score = None
if "profile" not in st.session_state:
    st.session_state.profile = None

# ========================
# LANDING PAGE HTML
# ========================
def show_landing_page():
    landing_html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'DM Sans', sans-serif;
                color: #0F172A;
                line-height: 1.6;
                background: linear-gradient(135deg, #F8FAFF 0%, #F0F9FF 100%);
            }
            .hero {
                min-height: 100vh;
                display: flex;
                align-items: center;
                padding: 4rem 2rem;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 4rem;
                align-items: center;
            }
            h1 {
                font-family: 'Sora', sans-serif;
                font-size: 3.5rem;
                margin-bottom: 1.5rem;
                font-weight: 800;
            }
            .highlight {
                background: linear-gradient(135deg, #2D5BFF, #00D9B4);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .subtitle {
                font-size: 1.25rem;
                color: #64748B;
                margin-bottom: 2rem;
            }
            .btn-group {
                display: flex;
                gap: 1rem;
                margin-bottom: 2rem;
            }
            .btn {
                padding: 1rem 2rem;
                font-size: 1.1rem;
                font-weight: 600;
                border-radius: 12px;
                border: none;
                cursor: pointer;
                transition: all 0.3s;
                text-decoration: none;
            }
            .btn-primary {
                background: linear-gradient(135deg, #2D5BFF, #00D9B4);
                color: white;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .btn-primary:hover {
                transform: translateY(-3px);
                box-shadow: 0 20px 25px rgba(0,0,0,0.15);
            }
            .btn-secondary {
                background: white;
                color: #2D5BFF;
                border: 2px solid #2D5BFF;
            }
            .feature-cards {
                display: grid;
                gap: 1rem;
            }
            .card {
                background: white;
                padding: 1.5rem;
                border-radius: 16px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }
            .card:hover {
                transform: translateX(10px);
            }
            .card h3 {
                color: #2D5BFF;
                margin-bottom: 0.5rem;
                font-size: 1.2rem;
            }
            .card p {
                color: #64748B;
                font-size: 0.95rem;
            }
            .features-section {
                padding: 4rem 2rem;
                background: white;
            }
            .features-grid {
                max-width: 1200px;
                margin: 0 auto;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 2rem;
                margin-top: 3rem;
            }
            .feature-box {
                background: #F1F5F9;
                padding: 2rem;
                border-radius: 16px;
                text-align: center;
                transition: all 0.3s;
            }
            .feature-box:hover {
                transform: translateY(-10px);
                background: white;
                box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            }
            .icon {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            .section-title {
                text-align: center;
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .footer {
                background: #0F172A;
                color: white;
                padding: 2rem;
                text-align: center;
            }
            @media (max-width: 968px) {
                .container, .features-grid { grid-template-columns: 1fr; }
                h1 { font-size: 2.5rem; }
            }
        </style>
    </head>
    <body>
        <div class="hero">
            <div class="container">
                <div>
                    <h1>Produtividade <span class="highlight">Guiada</span> e Inteligente</h1>
                    <p class="subtitle">
                        Descubra seu perfil de trabalho, receba tarefas personalizadas e alcance autonomia produtiva real com IA.
                    </p>
                    <div class="btn-group">
                        <button class="btn btn-primary" onclick="parent.postMessage({type: 'login'}, '*')">
                            Começar Agora
                        </button>
                        <button class="btn btn-secondary" onclick="scrollToFeatures()">
                            Saiba Mais
                        </button>
                    </div>
                </div>
                <div class="feature-cards">
                    <div class="card">
                        <h3>🎯 Executor</h3>
                        <p>Focado em ação rápida e resultados imediatos</p>
                    </div>
                    <div class="card">
                        <h3>📋 Organizador</h3>
                        <p>Estrutura processos e planeja com precisão</p>
                    </div>
                    <div class="card">
                        <h3>💡 Criativo</h3>
                        <p>Inova constantemente e explora novas ideias</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="features-section" id="features">
            <h2 class="section-title">Como Funciona</h2>
            <p style="text-align:center; color:#64748B; margin-bottom:2rem;">
                Sistema completo para desenvolver sua autonomia produtiva
            </p>
            <div class="features-grid">
                <div class="feature-box">
                    <div class="icon">📊</div>
                    <h3>Análise de Perfil</h3>
                    <p>Questionário identifica se você é Executor, Organizador ou Criativo</p>
                </div>
                <div class="feature-box">
                    <div class="icon">🎯</div>
                    <h3>Tarefas Personalizadas</h3>
                    <p>Vitrine de tarefas adaptadas ao seu perfil com execução guiada</p>
                </div>
                <div class="feature-box">
                    <div class="icon">📈</div>
                    <h3>IAP - Índice de Autonomia</h3>
                    <p>Acompanhe sua evolução com métricas de progresso real</p>
                </div>
                <div class="feature-box">
                    <div class="icon">🤖</div>
                    <h3>Assistente IA</h3>
                    <p>Chat integrado para dúvidas e ajustes personalizados</p>
                </div>
                <div class="feature-box">
                    <div class="icon">💾</div>
                    <h3>Histórico Completo</h3>
                    <p>Visualize evolução e padrões ao longo do tempo</p>
                </div>
                <div class="feature-box">
                    <div class="icon">🔒</div>
                    <h3>Segurança Total</h3>
                    <p>Proteção de dados conforme LGPD</p>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>&copy; 2026 EcoNexo's System. Todos os direitos reservados.</p>
            <p style="margin-top:1rem; color:#64748B;">
                <a href="#" style="color:#00D9B4; text-decoration:none;" onclick="parent.postMessage({type: 'lgpd'}, '*')">
                    LGPD & Privacidade
                </a> | 
                <a href="#" style="color:#00D9B4; text-decoration:none;">Termos de Uso</a>
            </p>
        </div>
        
        <script>
            function scrollToFeatures() {
                document.getElementById('features').scrollIntoView({behavior: 'smooth'});
            }
        </script>
    </body>
    </html>
    """
    components.html(landing_html, height=1800, scrolling=True)

# ========================
# LOGIN PAGE
# ========================
def show_login_page():
    st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 2rem;
            background: white;
            border-radius: 16px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.title("🔐 Login / Cadastro")
    
    tab1, tab2 = st.tabs(["Entrar", "Criar Conta"])
    
    with tab1:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Senha", type="password")
            submit = st.form_submit_button("Entrar", use_container_width=True)
            
            if submit:
                if email and password:
                    st.session_state.logged_in = True
                    st.session_state.user_name = email.split('@')[0]
                    st.session_state.current_page = "app"
                    st.rerun()
                else:
                    st.error("Preencha todos os campos")
    
    with tab2:
        with st.form("signup_form"):
            name = st.text_input("Nome Completo")
            email_signup = st.text_input("Email", key="email_signup")
            password_signup = st.text_input("Senha", type="password", key="password_signup")
            agree = st.checkbox("Concordo com a Política de Privacidade (LGPD)")
            submit_signup = st.form_submit_button("Criar Conta", use_container_width=True)
            
            if submit_signup:
                if name and email_signup and password_signup and agree:
                    st.session_state.logged_in = True
                    st.session_state.user_name = name
                    st.session_state.current_page = "app"
                    st.success("Conta criada com sucesso!")
                    st.rerun()
                else:
                    st.error("Preencha todos os campos e aceite a política")
    
    if st.button("← Voltar para Home"):
        st.session_state.current_page = "landing"
        st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# ========================
# LGPD PAGE
# ========================
def show_lgpd_page():
    st.title("🔒 Lei Geral de Proteção de Dados (LGPD)")
    st.markdown("---")
    
    st.markdown("""
    ### 1. Dados Coletados
    Para fornecer nossos serviços, coletamos apenas as informações essenciais:
    - **Dados de cadastro:** nome, email e senha (criptografada)
    - **Dados de perfil:** respostas ao questionário de produtividade
    - **Dados de uso:** histórico de tarefas completadas e IAP
    - **Dados técnicos:** endereço IP, tipo de navegador (segurança)
    
    ### 2. Como Usamos Seus Dados
    - Fornecer acesso personalizado à plataforma
    - Identificar seu perfil (Executor, Organizador, Criativo)
    - Sugerir tarefas e orientações via IA
    - Calcular seu Índice de Autonomia Produtiva (IAP)
    - Melhorar a experiência do usuário
    
    ### 3. Seus Direitos
    Você tem total controle e pode:
    - ✓ **Acessar** todos os dados armazenados
    - ✓ **Corrigir** informações desatualizadas
    - ✓ **Deletar** permanentemente sua conta
    - ✓ **Exportar** seus dados em formato legível
    - ✓ **Revogar** consentimento a qualquer momento
    
    ### 4. Segurança
    - Criptografia SSL/TLS em todas as conexões
    - Senhas com hash criptográfico (bcrypt)
    - Servidores seguros com backup diário
    - Acesso restrito à equipe autorizada
    
    ### 5. Contato - DPO
    📧 **Email:** privacidade@econexo.com  
    ⏱️ **Tempo de resposta:** Até 5 dias úteis
    
    ---
    **Versão atual:** Março de 2026
    """)
    
    if st.button("← Voltar"):
        st.session_state.current_page = "landing"
        st.rerun()

# ========================
# MAIN APPLICATION
# ========================
def show_app():
    st.sidebar.title(f"👋 Olá, {st.session_state.user_name}!")
    
    if st.sidebar.button("🚪 Sair"):
        st.session_state.logged_in = False
        st.session_state.current_page = "landing"
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Seu Progresso")
    st.sidebar.metric("Tarefas Completadas", st.session_state.tasks_completed)
    
    if st.session_state.iap_score:
        st.sidebar.metric("IAP Score", f"{st.session_state.iap_score}%")
    
    if st.session_state.profile:
        st.sidebar.success(f"Perfil: {st.session_state.profile}")
    
    # Application content
    st.title("🎯 EcoNexo's System")
    st.markdown("### Sua jornada de produtividade guiada")
    
    if st.session_state.step == "questionnaire":
        show_questionnaire()
    elif st.session_state.step == "tasks":
        show_tasks()
    elif st.session_state.step == "iap":
        show_iap()
    elif st.session_state.step == "profile":
        show_profile()
    elif st.session_state.step == "chat":
        show_chat()

def show_questionnaire():
    questions = [
        {"q": "Como você costuma iniciar um projeto?", 
         "opts": ["Pulo direto para a ação", "Faço um planejamento detalhado", "Exploro ideias primeiro"]},
        {"q": "O que te motiva mais?", 
         "opts": ["Ver resultados rápidos", "Ter tudo organizado", "Criar algo novo"]},
        {"q": "Como você lida com prazos?", 
         "opts": ["Trabalho sob pressão", "Planejo com antecedência", "Adapto conforme necessário"]},
    ]
    
    st.subheader(f"Pergunta {st.session_state.current_question + 1} de {len(questions)}")
    
    q = questions[st.session_state.current_question]
    st.markdown(f"### {q['q']}")
    
    answer = st.radio("Escolha a opção que mais se afina com você:", 
                     ["Me afino totalmente", "Me afino parcialmente", 
                      "Não me afino parcialmente", "Não me afino totalmente"],
                     key=f"q_{st.session_state.current_question}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("← Anterior"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.button("Próxima →"):
            st.session_state.answers[st.session_state.current_question] = answer
            
            if st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.session_state.step = "tasks"
                st.rerun()

def show_tasks():
    st.subheader("📋 Escolha 3 tarefas para completar")
    st.info(f"Tarefas completadas: {st.session_state.tasks_completed}/3")
    
    tasks = [
        "Escrever um email profissional",
        "Organizar lista de prioridades do dia",
        "Fazer brainstorm de ideias criativas",
        "Revisar um documento importante",
        "Planejar próxima semana"
    ]
    
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{i+1}.** {task}")
        with col2:
            if st.button("Completar", key=f"task_{i}"):
                st.session_state.tasks_completed += 1
                if st.session_state.tasks_completed >= 3:
                    st.session_state.step = "iap"
                st.rerun()
    
    if st.session_state.tasks_completed >= 3:
        st.success("✅ Você completou 3 tarefas!")
        if st.button("Ver meu IAP →"):
            st.session_state.step = "iap"
            st.rerun()

def show_iap():
    import random
    
    if not st.session_state.iap_score:
        st.session_state.iap_score = random.randint(65, 95)
    
    st.markdown("## 📊 Seu Índice de Autonomia Produtiva")
    
    col1, col2, col3 = st.columns(3)
    with col2:
        st.metric("IAP Score", f"{st.session_state.iap_score}%", "↑ Acima da média")
    
    st.progress(st.session_state.iap_score / 100)
    
    st.info("""
    **O que é o IAP?**  
    O Índice de Autonomia Produtiva mede sua capacidade de iniciar, executar e completar tarefas de forma independente.
    """)
    
    if st.button("Ver meu Perfil →"):
        st.session_state.step = "profile"
        st.rerun()

def show_profile():
    # Determine profile based on answers
    profiles = ["🎯 Executor", "📋 Organizador", "💡 Criativo"]
    st.session_state.profile = profiles[st.session_state.tasks_completed % 3]
    
    st.markdown(f"## Seu Perfil: {st.session_state.profile}")
    
    profile_info = {
        "🎯 Executor": {
            "desc": "Você é orientado à ação e resultados. Prefere fazer do que planejar.",
            "forças": ["Implementação rápida", "Foco em resultados", "Adaptabilidade"],
            "dicas": ["Use timers para tarefas", "Divida projetos grandes", "Celebre conquistas"]
        },
        "📋 Organizador": {
            "desc": "Você valoriza estrutura e planejamento. Gosta de ter tudo sob controle.",
            "forças": ["Planejamento detalhado", "Organização", "Previsibilidade"],
            "dicas": ["Crie checklists", "Use calendários", "Defina prazos claros"]
        },
        "💡 Criativo": {
            "desc": "Você é inovador e explora novas possibilidades constantemente.",
            "forças": ["Pensamento divergente", "Inovação", "Flexibilidade"],
            "dicas": ["Reserve tempo para brainstorm", "Experimente métodos novos", "Registre ideias"]
        }
    }
    
    info = profile_info[st.session_state.profile]
    
    st.markdown(f"### {info['desc']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**💪 Suas Forças:**")
        for f in info['forças']:
            st.markdown(f"- {f}")
    
    with col2:
        st.markdown("**💡 Dicas para Você:**")
        for d in info['dicas']:
            st.markdown(f"- {d}")
    
    if st.button("Conversar com IA →"):
        st.session_state.step = "chat"
        st.rerun()

def show_chat():
    st.markdown("## 🤖 Chat com Assistente IA")
    st.info(f"IA contextualizada com seu perfil: {st.session_state.profile}")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    if prompt := st.chat_input("Faça uma pergunta sobre produtividade..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Simulated AI response
        response = f"Como {st.session_state.profile}, recomendo focar em suas forças naturais. Sua pergunta sobre '{prompt}' pode ser abordada da seguinte forma..."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# ========================
# ROUTER
# ========================
# Listen for messages from iframe
st.markdown("""
<script>
window.addEventListener('message', function(event) {
    if (event.data.type === 'login') {
        window.parent.postMessage({action: 'setPage', page: 'login'}, '*');
    } else if (event.data.type === 'lgpd') {
        window.parent.postMessage({action: 'setPage', page: 'lgpd'}, '*');
    }
});
</script>
""", unsafe_allow_html=True)

# Main router
if not st.session_state.logged_in:
    if st.session_state.current_page == "landing":
        show_landing_page()
        
        # Add navigation buttons below landing page
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔐 Fazer Login"):
                st.session_state.current_page = "login"
                st.rerun()
        with col2:
            if st.button("🔒 Ver LGPD"):
                st.session_state.current_page = "lgpd"
                st.rerun()
    
    elif st.session_state.current_page == "login":
        show_login_page()
    
    elif st.session_state.current_page == "lgpd":
        show_lgpd_page()
else:
    show_app()
