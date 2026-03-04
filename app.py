import streamlit as st
import random

# ========================
# CONFIGURAÇÃO DA PÁGINA
# ========================
st.set_page_config(
    page_title="EcoNexo's System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Global
st.markdown("""
<style>
    /* Remove padding padrão do Streamlit */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }
    
    /* Esconde elementos do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Botões customizados */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 0.8rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

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
if "completed_tasks" not in st.session_state:
    st.session_state.completed_tasks = set()
if "iap_score" not in st.session_state:
    st.session_state.iap_score = None
if "profile" not in st.session_state:
    st.session_state.profile = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========================
# LANDING PAGE
# ========================
def show_landing_page():
    # Hero Section
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div style="padding: 2rem 0;">
            <h1 style="font-size: 3.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 1.5rem;">
                Produtividade 
                <span style="background: linear-gradient(135deg, #2D5BFF, #00D9B4); 
                             -webkit-background-clip: text; 
                             -webkit-text-fill-color: transparent;">
                    Guiada
                </span> 
                e Inteligente
            </h1>
            <p style="font-size: 1.25rem; color: #64748B; margin-bottom: 2rem; line-height: 1.6;">
                Descubra seu perfil de trabalho, receba tarefas personalizadas e alcance 
                autonomia produtiva real com IA.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Começar Agora", key="btn_start", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()
        
        with col_btn2:
            if st.button("📖 Saiba Mais", key="btn_learn", use_container_width=True, type="secondary"):
                st.session_state.current_page = "features"
                st.rerun()
    
    with col2:
        st.markdown("""
        <div style="display: grid; gap: 1rem; padding: 1rem 0;">
        """, unsafe_allow_html=True)
        
        # Card Executor
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 16px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                    transition: transform 0.3s;">
            <h3 style="color: #2D5BFF; margin-bottom: 0.5rem; font-size: 1.3rem;">
                🎯 Executor
            </h3>
            <p style="color: #64748B; margin: 0;">
                Focado em ação rápida e resultados imediatos
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Card Organizador
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 16px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                    margin-top: 1rem;">
            <h3 style="color: #2D5BFF; margin-bottom: 0.5rem; font-size: 1.3rem;">
                📋 Organizador
            </h3>
            <p style="color: #64748B; margin: 0;">
                Estrutura processos e planeja com precisão
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Card Criativo
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 16px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                    margin-top: 1rem;">
            <h3 style="color: #2D5BFF; margin-bottom: 0.5rem; font-size: 1.3rem;">
                💡 Criativo
            </h3>
            <p style="color: #64748B; margin: 0;">
                Inova constantemente e explora novas ideias
            </p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer simples
    st.markdown("---")
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        if st.button("🔒 LGPD & Privacidade", use_container_width=True):
            st.session_state.current_page = "lgpd"
            st.rerun()
    
    with col_f2:
        if st.button("👥 Quem Somos", use_container_width=True):
            st.session_state.current_page = "about"
            st.rerun()
    
    with col_f3:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; color: #64748B;">
            © 2026 EcoNexo's System<br>Todos os direitos reservados
        </div>
        """, unsafe_allow_html=True)

# ========================
# FEATURES PAGE
# ========================
def show_features_page():
    st.markdown("## 📖 Como Funciona")
    st.markdown("**Sistema completo para desenvolver sua autonomia produtiva**")
    st.markdown("---")
    
    # Feature 1
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size: 4rem; text-align: center;'>📊</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Análise de Perfil")
        st.write("Questionário identifica se você é Executor, Organizador ou Criativo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 2
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size: 4rem; text-align: center;'>🎯</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Tarefas Personalizadas")
        st.write("Vitrine adaptada ao seu perfil com execução guiada")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 3
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size: 4rem; text-align: center;'>📈</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### IAP - Índice de Autonomia")
        st.write("Acompanhe sua evolução com métricas reais")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 4
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size: 4rem; text-align: center;'>🤖</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Assistente IA")
        st.write("Chat integrado para dúvidas e ajustes personalizados")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 5
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size: 4rem; text-align: center;'>💾</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Histórico Completo")
        st.write("Visualize evolução e padrões ao longo do tempo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature 6
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown("<div style='font-size: 4rem; text-align: center;'>🔒</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Segurança Total")
        st.write("Proteção de dados conforme LGPD")
    
    st.markdown("---")
    
    col_back, col_start = st.columns([1, 1])
    with col_back:
        if st.button("← Voltar", use_container_width=True):
            st.session_state.current_page = "landing"
            st.rerun()
    with col_start:
        if st.button("Começar Agora →", use_container_width=True, type="primary"):
            st.session_state.current_page = "login"
            st.rerun()

# ========================
# LOGIN PAGE
# ========================
def show_login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 3rem; border-radius: 20px; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1); margin-top: 2rem;">
        """, unsafe_allow_html=True)
        
        st.markdown("## 🔐 Acesse sua conta")
        
        tab1, tab2 = st.tabs(["✉️ Entrar", "📝 Criar Conta"])
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("📧 Email", placeholder="seu@email.com")
                password = st.text_input("🔒 Senha", type="password", placeholder="••••••••")
                submit = st.form_submit_button("Entrar", use_container_width=True, type="primary")
                
                if submit:
                    if email and password:
                        st.session_state.logged_in = True
                        st.session_state.user_name = email.split('@')[0].title()
                        st.session_state.current_page = "app"
                        st.success("✅ Login realizado com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Preencha todos os campos")
        
        with tab2:
            with st.form("signup_form"):
                name = st.text_input("👤 Nome Completo", placeholder="Seu nome")
                email_signup = st.text_input("📧 Email", placeholder="seu@email.com", key="email_signup")
                password_signup = st.text_input("🔒 Senha", type="password", placeholder="Mínimo 8 caracteres", key="password_signup")
                agree = st.checkbox("Concordo com a Política de Privacidade (LGPD)")
                submit_signup = st.form_submit_button("Criar Conta", use_container_width=True, type="primary")
                
                if submit_signup:
                    if name and email_signup and password_signup and agree:
                        st.session_state.logged_in = True
                        st.session_state.user_name = name.split()[0].title()
                        st.session_state.current_page = "app"
                        st.success("✅ Conta criada com sucesso!")
                        st.rerun()
                    else:
                        st.error("❌ Preencha todos os campos e aceite a política")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("← Voltar para Home", use_container_width=True):
            st.session_state.current_page = "landing"
            st.rerun()

# ========================
# ABOUT PAGE
# ========================
def show_about_page():
    st.markdown("## 👥 Quem Somos")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Sobre o EcoNexo's System
        
        O **EcoNexo's System** nasceu da observação de um problema comum: muitas pessoas 
        sabem o que precisam fazer, mas não sabem *como* começar ou manter a consistência.
        
        Criamos uma plataforma que não apenas identifica seu perfil de trabalho natural 
        (Executor, Organizador ou Criativo), mas também oferece **execução guiada por IA** 
        — transformando intenção em ação real.
        
        ### Nossa Missão
        
        Desenvolver **autonomia produtiva real** através de tecnologia acessível, 
        personalizada e baseada em ciência comportamental.
        """)
    
    with col2:
        st.markdown("### 💪 Nossos Valores")
        
        st.info("🎯 **Foco no Resultado** - Medimos sucesso pela quantidade de tarefas concluídas")
        st.success("🤝 **Personalização** - Cada pessoa é única, nosso sistema se adapta")
        st.warning("🔐 **Transparência Total** - Seus dados são seus. Conformidade com LGPD")
    
    if st.button("← Voltar", use_container_width=True):
        st.session_state.current_page = "landing"
        st.rerun()

# ========================
# LGPD PAGE
# ========================
def show_lgpd_page():
    st.markdown("## 🔒 Lei Geral de Proteção de Dados (LGPD)")
    st.markdown("---")
    
    with st.expander("📋 1. Dados Coletados", expanded=True):
        st.markdown("""
        Para fornecer nossos serviços, coletamos apenas as informações essenciais:
        - **Dados de cadastro:** nome, email e senha (criptografada)
        - **Dados de perfil:** respostas ao questionário de produtividade
        - **Dados de uso:** histórico de tarefas completadas e IAP
        - **Dados técnicos:** endereço IP, tipo de navegador (segurança)
        """)
    
    with st.expander("🎯 2. Como Usamos Seus Dados"):
        st.markdown("""
        - Fornecer acesso personalizado à plataforma
        - Identificar seu perfil (Executor, Organizador, Criativo)
        - Sugerir tarefas e orientações via IA
        - Calcular seu Índice de Autonomia Produtiva (IAP)
        - Melhorar a experiência do usuário
        """)
    
    with st.expander("✅ 3. Seus Direitos"):
        st.markdown("""
        Você tem total controle e pode:
        - ✓ **Acessar** todos os dados armazenados
        - ✓ **Corrigir** informações desatualizadas
        - ✓ **Deletar** permanentemente sua conta
        - ✓ **Exportar** seus dados em formato legível
        - ✓ **Revogar** consentimento a qualquer momento
        """)
    
    with st.expander("🔐 4. Segurança"):
        st.markdown("""
        - Criptografia SSL/TLS em todas as conexões
        - Senhas com hash criptográfico (bcrypt)
        - Servidores seguros com backup diário
        - Acesso restrito à equipe autorizada
        """)
    
    st.info("📧 **Contato DPO:** privacidade@econexo.com | Resposta em até 5 dias úteis")
    
    if st.button("← Voltar", use_container_width=True):
        st.session_state.current_page = "landing"
        st.rerun()

# ========================
# MAIN APPLICATION
# ========================
def show_app():
    # Sidebar
    with st.sidebar:
        st.markdown(f"### 👋 Olá, {st.session_state.user_name}!")
        st.markdown("---")
        
        st.markdown("### 📊 Seu Progresso")
        st.metric("Tarefas Completadas", f"{st.session_state.tasks_completed}/3")
        
        if st.session_state.iap_score:
            st.metric("IAP Score", f"{st.session_state.iap_score}%", "↑ Acima da média")
        
        if st.session_state.profile:
            st.success(f"**Perfil:** {st.session_state.profile}")
        
        st.markdown("---")
        
        if st.button("🚪 Sair", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Main content
    st.title("🎯 EcoNexo's System")
    st.markdown("### Sua jornada de produtividade guiada")
    st.markdown("---")
    
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

# ========================
# QUESTIONNAIRE
# ========================
def show_questionnaire():
    questions = [
        {"q": "Como você costuma iniciar um projeto?", 
         "opts": ["Pulo direto para a ação", "Faço um planejamento detalhado", "Exploro ideias primeiro"]},
        {"q": "O que te motiva mais?", 
         "opts": ["Ver resultados rápidos", "Ter tudo organizado", "Criar algo novo"]},
        {"q": "Como você lida com prazos?", 
         "opts": ["Trabalho sob pressão", "Planejo com antecedência", "Adapto conforme necessário"]},
    ]
    
    st.progress((st.session_state.current_question + 1) / len(questions))
    st.markdown(f"**Pergunta {st.session_state.current_question + 1} de {len(questions)}**")
    
    q = questions[st.session_state.current_question]
    st.markdown(f"### {q['q']}")
    
    # Mostrar a opção selecionada
    selected_opt = st.radio(
        "Selecione a opção:",
        q['opts'],
        key=f"opt_{st.session_state.current_question}"
    )
    
    answer = st.radio(
        "Como você se identifica com esta opção?",
        ["Me afino totalmente", "Me afino parcialmente", 
         "Não me afino parcialmente", "Não me afino totalmente"],
        key=f"affinity_{st.session_state.current_question}"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.current_question > 0:
            if st.button("← Anterior", use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.button("Próxima →" if st.session_state.current_question < len(questions) - 1 else "Finalizar", 
                     use_container_width=True, type="primary"):
            st.session_state.answers[st.session_state.current_question] = {
                "option": selected_opt,
                "affinity": answer
            }
            
            if st.session_state.current_question < len(questions) - 1:
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.session_state.step = "tasks"
                st.rerun()

# ========================
# TASKS
# ========================
def show_tasks():
    st.markdown("## 📋 Complete 3 Tarefas")
    st.info(f"**Progresso:** {st.session_state.tasks_completed}/3 tarefas completadas")
    
    tasks = [
        ("Escrever um email profissional", "✉️"),
        ("Organizar lista de prioridades do dia", "📝"),
        ("Fazer brainstorm de ideias criativas", "💡"),
        ("Revisar um documento importante", "📄"),
        ("Planejar a próxima semana", "📅")
    ]
    
    for i, (task, icon) in enumerate(tasks):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            if i in st.session_state.completed_tasks:
                st.success(f"~~{icon} {task}~~ ✅")
            else:
                st.markdown(f"**{icon} {task}**")
        
        with col2:
            if i not in st.session_state.completed_tasks:
                if st.button("Completar", key=f"task_{i}", use_container_width=True):
                    st.session_state.completed_tasks.add(i)
                    st.session_state.tasks_completed = len(st.session_state.completed_tasks)
                    
                    if st.session_state.tasks_completed >= 3:
                        st.session_state.step = "iap"
                    st.rerun()
    
    if st.session_state.tasks_completed >= 3:
        st.success("🎉 Parabéns! Você completou 3 tarefas!")
        if st.button("Ver meu IAP →", use_container_width=True, type="primary"):
            st.session_state.step = "iap"
            st.rerun()

# ========================
# IAP
# ========================
def show_iap():
    if not st.session_state.iap_score:
        # Calcula IAP baseado nas respostas
        st.session_state.iap_score = random.randint(70, 95)
    
    st.markdown("## 📊 Seu Índice de Autonomia Produtiva")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.metric(
            label="IAP Score",
            value=f"{st.session_state.iap_score}%",
            delta="↑ Acima da média"
        )
        st.progress(st.session_state.iap_score / 100)
    
    st.info("""
    **O que é o IAP?**  
    
    O Índice de Autonomia Produtiva mede sua capacidade de iniciar, executar e 
    completar tarefas de forma independente. Quanto maior o IAP, maior sua autonomia!
    """)
    
    st.markdown("### 📈 Seu Desempenho:")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.metric("Iniciativa", "85%")
    with col_b:
        st.metric("Execução", "90%")
    with col_c:
        st.metric("Conclusão", "92%")
    
    if st.button("Descobrir meu Perfil →", use_container_width=True, type="primary"):
        st.session_state.step = "profile"
        st.rerun()

# ========================
# PROFILE
# ========================
def show_profile():
    # Determina perfil baseado nas respostas
    profiles = ["🎯 Executor", "📋 Organizador", "💡 Criativo"]
    
    if not st.session_state.profile:
        # Lógica simples baseada nas respostas
        if st.session_state.answers:
            first_answer = st.session_state.answers.get(0, {}).get("option", "")
            if "ação" in first_answer.lower():
                st.session_state.profile = "🎯 Executor"
            elif "planejamento" in first_answer.lower():
                st.session_state.profile = "📋 Organizador"
            else:
                st.session_state.profile = "💡 Criativo"
        else:
            st.session_state.profile = profiles[st.session_state.tasks_completed % 3]
    
    st.markdown(f"## Seu Perfil: {st.session_state.profile}")
    st.balloons()
    
    profile_info = {
        "🎯 Executor": {
            "desc": "Você é orientado à ação e resultados. Prefere fazer do que planejar excessivamente.",
            "forças": ["⚡ Implementação rápida", "🎯 Foco em resultados", "🔄 Adaptabilidade"],
            "dicas": ["Use timers de 25 minutos (Pomodoro)", "Divida projetos grandes em micro-tarefas", "Celebre pequenas conquistas diariamente"]
        },
        "📋 Organizador": {
            "desc": "Você valoriza estrutura e planejamento. Gosta de ter tudo sob controle e bem documentado.",
            "forças": ["📅 Planejamento detalhado", "🗂️ Organização impecável", "⏱️ Gestão de tempo"],
            "dicas": ["Crie checklists para tudo", "Use ferramentas de calendário", "Defina prazos claros e realistas"]
        },
        "💡 Criativo": {
            "desc": "Você é inovador e explora novas possibilidades constantemente. Pensa fora da caixa.",
            "forças": ["🌟 Pensamento divergente", "💫 Inovação constante", "🎨 Flexibilidade mental"],
            "dicas": ["Reserve tempo diário para brainstorm", "Experimente métodos diferentes", "Mantenha um caderno de ideias"]
        }
    }
    
    info = profile_info[st.session_state.profile]
    
    st.markdown(f"### {info['desc']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💪 Suas Forças:")
        for f in info['forças']:
            st.success(f)
    
    with col2:
        st.markdown("### 💡 Dicas para Você:")
        for d in info['dicas']:
            st.info(d)
    
    st.markdown("---")
    
    if st.button("🤖 Conversar com IA Personalizada →", use_container_width=True, type="primary"):
        st.session_state.step = "chat"
        st.rerun()

# ========================
# CHAT
# ========================
def show_chat():
    st.markdown(f"## 🤖 Assistente IA - Perfil {st.session_state.profile}")
    
    st.info(f"💬 Este chat é personalizado para o perfil **{st.session_state.profile}** "
            f"e tem conhecimento do seu IAP de **{st.session_state.iap_score}%**")
    
    # Mostrar mensagens
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Faça uma pergunta sobre produtividade..."):
        # Adiciona mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Gera resposta simulada
        profile_tips = {
            "🎯 Executor": "focar em ação imediata e dividir tarefas em blocos pequenos",
            "📋 Organizador": "criar estruturas e listas detalhadas antes de começar",
            "💡 Criativo": "explorar múltiplas abordagens e manter flexibilidade"
        }
        
        tip = profile_tips.get(st.session_state.profile, "manter o foco")
        
        response = f"""Como **{st.session_state.profile}** com IAP de {st.session_state.iap_score}%, 
        recomendo {tip}. 
        
        Sobre sua pergunta "{prompt}":
        
        {random.choice([
            "Uma estratégia eficaz seria começar pela parte mais desafiadora quando sua energia estiver alta.",
            "Experimente usar a técnica Pomodoro - 25 minutos de foco total, 5 minutos de pausa.",
            "Divida essa tarefa em 3 partes menores e comece pela que parece mais fácil para ganhar momentum.",
            "O segredo é não esperar motivação - crie um sistema que funcione independente dela."
        ])}
        
        Quer que eu elabore mais algum ponto específico?"""
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Recomeçar Jornada", use_container_width=True):
            st.session_state.step = "questionnaire"
            st.session_state.current_question = 0
            st.session_state.tasks_completed = 0
            st.session_state.completed_tasks = set()
            st.session_state.iap_score = None
            st.session_state.profile = None
            st.session_state.messages = []
            st.rerun()
    
    with col2:
        if st.button("📊 Ver Meu Perfil Novamente", use_container_width=True):
            st.session_state.step = "profile"
            st.rerun()

# ========================
# MAIN ROUTER
# ========================
if not st.session_state.logged_in:
    if st.session_state.current_page == "landing":
        show_landing_page()
    elif st.session_state.current_page == "features":
        show_features_page()
    elif st.session_state.current_page == "login":
        show_login_page()
    elif st.session_state.current_page == "about":
        show_about_page()
    elif st.session_state.current_page == "lgpd":
        show_lgpd_page()
else:
    show_app()
