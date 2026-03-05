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

# CSS Global com Google Fonts
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown, .stText, p, div, span, h1, h2, h3, h4, label {
        font-family: 'Inter', sans-serif !important;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s;
        border: none;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }

    /* Tabs font */
    .stTabs [data-baseweb="tab"] {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600;
    }

    /* Input font */
    .stTextInput input, .stTextArea textarea {
        font-family: 'Inter', sans-serif !important;
    }

    /* Metric */
    [data-testid="metric-container"] {
        font-family: 'Inter', sans-serif !important;
    }

    /* Radio */
    .stRadio label {
        font-family: 'Inter', sans-serif !important;
    }

    /* Chat */
    .stChatMessage {
        font-family: 'Inter', sans-serif !important;
    }

    .hero-title {
        font-family: 'Inter', sans-serif !important;
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 1.5rem;
    }

    .hero-subtitle {
        font-family: 'Inter', sans-serif !important;
        font-size: 1.2rem;
        color: #64748B;
        margin-bottom: 2rem;
        line-height: 1.6;
    }

    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-top: 1rem;
        border-left: 4px solid #2D5BFF;
    }

    .card h3 {
        font-family: 'Inter', sans-serif !important;
        color: #2D5BFF;
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
        font-weight: 700;
    }

    .card p {
        color: #64748B;
        margin: 0;
        font-size: 0.95rem;
    }

    .task-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }

    .task-card-selected {
        background: #eff6ff;
        border: 2px solid #2D5BFF;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }

    .task-card-done {
        background: #f0fdf4;
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
        opacity: 0.7;
    }

    .progress-bar-container {
        background: #e2e8f0;
        border-radius: 99px;
        height: 10px;
        margin: 0.5rem 0 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ========================
# SESSION STATE
# ========================
defaults = {
    "logged_in": False,
    "user_name": "",
    "current_page": "landing",
    "step": "questionnaire",
    "current_question": 0,
    "answers": {},
    "tasks_completed": 0,
    "completed_tasks": set(),
    "selected_task": None,
    "iap_score": None,
    "profile": None,
    "messages": [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ========================
# PERGUNTAS DO QUESTIONÁRIO
# ========================
QUESTIONS = [
    {
        "q": "Como você costuma iniciar um projeto?",
        "opts": [
            ("Executor", "Pulo direto para a ação, sem muita análise prévia"),
            ("Organizador", "Faço um planejamento detalhado antes de começar"),
            ("Criativo", "Exploro ideias e possibilidades primeiro"),
        ]
    },
    {
        "q": "O que mais te motiva no trabalho?",
        "opts": [
            ("Executor", "Ver resultados rápidos e tangíveis"),
            ("Organizador", "Ter processos claros e tudo bem organizado"),
            ("Criativo", "Criar algo novo e inovador"),
        ]
    },
    {
        "q": "Como você lida com prazos apertados?",
        "opts": [
            ("Executor", "Trabalho melhor sob pressão, entro no modo foco"),
            ("Organizador", "Planejo com antecedência para evitar correria"),
            ("Criativo", "Adapto o escopo do trabalho conforme a situação"),
        ]
    },
    {
        "q": "Qual é o seu maior ponto forte?",
        "opts": [
            ("Executor", "Colocar ideias em prática rapidamente"),
            ("Organizador", "Manter tudo estruturado e dentro do prazo"),
            ("Criativo", "Encontrar soluções originais para problemas"),
        ]
    },
    {
        "q": "Como você prefere receber tarefas?",
        "opts": [
            ("Executor", "Direto ao ponto: o que fazer e até quando"),
            ("Organizador", "Com contexto, critérios e checklist claros"),
            ("Criativo", "Com liberdade para interpretar e criar a abordagem"),
        ]
    },
    {
        "q": "Quando um projeto não vai bem, o que você faz?",
        "opts": [
            ("Executor", "Tomo uma decisão rápida e mudo o curso da ação"),
            ("Organizador", "Reviso o planejamento e identifico onde errei"),
            ("Criativo", "Busco uma abordagem completamente diferente"),
        ]
    },
    {
        "q": "Como você organiza seu dia de trabalho?",
        "opts": [
            ("Executor", "Faço as tarefas conforme chegam, priorizando urgência"),
            ("Organizador", "Tenho uma lista priorizada e sigo ela rigorosamente"),
            ("Criativo", "Trabalho no que me inspira mais em cada momento"),
        ]
    },
]

AFFINITY = [
    "Me identifico totalmente",
    "Me identifico parcialmente",
    "Não me identifico muito",
    "Não me identifico",
]

AFFINITY_WEIGHTS = {
    "Me identifico totalmente": 2,
    "Me identifico parcialmente": 1,
    "Não me identifico muito": 0,
    "Não me identifico": -1,
}

# ========================
# TAREFAS
# ========================
ALL_TASKS = [
    {"id": 0, "icon": "✉️", "name": "Escrever um email profissional",      "desc": "Rascunhe um email claro e objetivo para um colega ou cliente.", "profile": "Executor"},
    {"id": 1, "icon": "📝", "name": "Organizar lista de prioridades do dia","desc": "Liste e priorize as 5 tarefas mais importantes para hoje.",     "profile": "Organizador"},
    {"id": 2, "icon": "💡", "name": "Brainstorm de ideias criativas",       "desc": "Gere 10 ideias para solucionar um problema do seu trabalho.",   "profile": "Criativo"},
    {"id": 3, "icon": "📄", "name": "Revisar um documento importante",      "desc": "Releia e melhore um documento em que está trabalhando.",         "profile": "Organizador"},
    {"id": 4, "icon": "📅", "name": "Planejar a próxima semana",            "desc": "Monte um plano realista para os próximos 7 dias.",               "profile": "Organizador"},
    {"id": 5, "icon": "⚡", "name": "Resolver uma tarefa pendente há dias", "desc": "Escolha algo que está procrastinando e finalize agora.",         "profile": "Executor"},
    {"id": 6, "icon": "🎨", "name": "Criar um esboço visual ou mapa mental","desc": "Desenhe ou descreva visualmente um projeto ou ideia.",           "profile": "Criativo"},
    {"id": 7, "icon": "📊", "name": "Analisar métricas ou resultados",      "desc": "Revise números, dados ou indicadores do seu trabalho.",          "profile": "Executor"},
]

# ========================
# HELPERS
# ========================
def compute_profile():
    scores = {"Executor": 0, "Organizador": 0, "Criativo": 0}
    for q_idx, q_answers in st.session_state.answers.items():
        for profile_key, affinity in q_answers.items():
            weight = AFFINITY_WEIGHTS.get(affinity, 0)
            scores[profile_key] = scores.get(profile_key, 0) + weight
    best = max(scores, key=lambda k: scores[k])
    icons = {"Executor": "🎯", "Organizador": "📋", "Criativo": "💡"}
    return f"{icons[best]} {best}"

# ========================
# LANDING PAGE
# ========================
def show_landing_page():
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("""
        <div style="padding: 2rem 0;">
            <h1 class="hero-title">
                Produtividade
                <span style="background: linear-gradient(135deg, #2D5BFF, #00D9B4);
                             -webkit-background-clip: text;
                             -webkit-text-fill-color: transparent;">
                    Guiada
                </span>
                e Inteligente
            </h1>
            <p class="hero-subtitle">
                Descubra seu perfil de trabalho, receba tarefas personalizadas e alcance
                autonomia produtiva real com IA.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🚀 Começar Agora", key="btn_start", use_container_width=True, type="primary"):
                st.session_state.current_page = "login"
                st.rerun()
        with col_btn2:
            if st.button("📖 Saiba Mais", key="btn_learn", use_container_width=True):
                st.session_state.current_page = "features"
                st.rerun()

    with col2:
        st.markdown("""
        <div class="card"><h3>🎯 Executor</h3><p>Focado em ação rápida e resultados imediatos</p></div>
        <div class="card"><h3>📋 Organizador</h3><p>Estrutura processos e planeja com precisão</p></div>
        <div class="card"><h3>💡 Criativo</h3><p>Inova constantemente e explora novas ideias</p></div>
        """, unsafe_allow_html=True)

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
        <div style="text-align:center; padding:0.75rem; color:#64748B; font-size:0.9rem;">
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

    features = [
        ("📊", "Análise de Perfil", "Questionário com 7 perguntas identifica se você é Executor, Organizador ou Criativo com base nas suas respostas."),
        ("🎯", "Tarefas Personalizadas", "Escolha as tarefas que deseja executar — adaptadas ao seu perfil — com execução guiada passo a passo."),
        ("📈", "IAP — Índice de Autonomia", "Acompanhe sua evolução com métricas reais de iniciativa, execução e conclusão."),
        ("🤖", "Assistente IA", "Chat integrado e personalizado para dúvidas e ajustes conforme seu perfil."),
        ("💾", "Histórico Completo", "Visualize sua evolução e padrões ao longo do tempo."),
        ("🔒", "Segurança Total", "Proteção de dados rigorosa em conformidade com a LGPD."),
    ]

    for icon, title, desc in features:
        col1, col2 = st.columns([1, 6])
        with col1:
            st.markdown(f"<div style='font-size:3rem; text-align:center; padding-top:0.3rem;'>{icon}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{title}**")
            st.write(desc)
        st.markdown("<hr style='margin:0.5rem 0; border:none; border-top:1px solid #e2e8f0;'>", unsafe_allow_html=True)

    col_back, col_start = st.columns(2)
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
                        st.session_state.user_name = email.split('@')[0].replace('.', ' ').title()
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
                        if len(password_signup) < 8:
                            st.error("❌ A senha deve ter pelo menos 8 caracteres")
                        else:
                            st.session_state.logged_in = True
                            st.session_state.user_name = name.split()[0].title()
                            st.session_state.current_page = "app"
                            st.success("✅ Conta criada com sucesso!")
                            st.rerun()
                    else:
                        st.error("❌ Preencha todos os campos e aceite a política de privacidade")

        st.markdown("<br>", unsafe_allow_html=True)
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
        st.info("🎯 **Foco no Resultado** — Medimos sucesso pelas tarefas concluídas")
        st.success("🤝 **Personalização** — Cada pessoa é única; nosso sistema se adapta")
        st.warning("🔐 **Transparência Total** — Seus dados são seus; conformidade com LGPD")

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
        Coletamos apenas as informações essenciais para o funcionamento da plataforma:
        - **Dados de cadastro:** nome, e-mail e senha (criptografada)
        - **Dados de perfil:** respostas ao questionário de produtividade
        - **Dados de uso:** histórico de tarefas completadas e pontuação IAP
        - **Dados técnicos:** endereço IP e tipo de navegador (segurança)
        """)

    with st.expander("🎯 2. Como Usamos Seus Dados"):
        st.markdown("""
        - Fornecer acesso personalizado à plataforma
        - Identificar seu perfil (Executor, Organizador, Criativo)
        - Sugerir tarefas e orientações via IA
        - Calcular seu Índice de Autonomia Produtiva (IAP)
        - Melhorar continuamente a experiência do usuário
        """)

    with st.expander("✅ 3. Seus Direitos"):
        st.markdown("""
        Você tem total controle e pode a qualquer momento:
        - ✓ **Acessar** todos os dados armazenados
        - ✓ **Corrigir** informações desatualizadas
        - ✓ **Deletar** permanentemente sua conta
        - ✓ **Exportar** seus dados em formato legível
        - ✓ **Revogar** o consentimento dado
        """)

    with st.expander("🔐 4. Segurança"):
        st.markdown("""
        - Criptografia SSL/TLS em todas as conexões
        - Senhas com hash criptográfico (bcrypt)
        - Servidores com backup diário e acesso restrito
        - Monitoramento contínuo contra acessos não autorizados
        """)

    st.info("📧 **Contato DPO:** privacidade@econexo.com | Resposta em até 5 dias úteis")

    if st.button("← Voltar", use_container_width=True):
        st.session_state.current_page = "landing"
        st.rerun()

# ========================
# MAIN APP SHELL
# ========================
def show_app():
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

    st.title("🎯 EcoNexo's System")
    st.markdown("### Sua jornada de produtividade guiada")
    st.markdown("---")

    step_map = {
        "questionnaire": show_questionnaire,
        "tasks": show_tasks,
        "iap": show_iap,
        "profile": show_profile,
        "chat": show_chat,
    }
    step_map.get(st.session_state.step, show_questionnaire)()

# ========================
# QUESTIONÁRIO (7 perguntas)
# ========================
def show_questionnaire():
    total = len(QUESTIONS)
    current = st.session_state.current_question

    st.markdown(f"## 📋 Questionário de Perfil")
    st.progress((current + 1) / total)
    st.markdown(f"**Pergunta {current + 1} de {total}**")
    st.markdown("---")

    q = QUESTIONS[current]
    st.markdown(f"### {q['q']}")
    st.markdown("*Para cada opção abaixo, indique o quanto você se identifica:*")
    st.markdown("<br>", unsafe_allow_html=True)

    # Resgata respostas salvas para esta pergunta, se houver
    saved = st.session_state.answers.get(current, {})
    current_answers = {}

    for profile_key, opt_text in q["opts"]:
        st.markdown(f"**{opt_text}**")
        default_idx = AFFINITY.index(saved.get(profile_key, "Me identifico parcialmente"))
        answer = st.radio(
            "Nível de identificação:",
            AFFINITY,
            index=default_idx,
            key=f"q{current}_{profile_key}",
            horizontal=True,
            label_visibility="collapsed",
        )
        current_answers[profile_key] = answer
        st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if current > 0:
            if st.button("← Anterior", use_container_width=True):
                st.session_state.answers[current] = current_answers
                st.session_state.current_question -= 1
                st.rerun()
    with col3:
        label = "Próxima →" if current < total - 1 else "✅ Finalizar"
        if st.button(label, use_container_width=True, type="primary"):
            st.session_state.answers[current] = current_answers
            if current < total - 1:
                st.session_state.current_question += 1
                st.rerun()
            else:
                st.session_state.profile = compute_profile()
                st.session_state.step = "tasks"
                st.rerun()

# ========================
# TAREFAS — COM SELEÇÃO
# ========================
def show_tasks():
    st.markdown("## 📋 Vitrine de Tarefas")
    st.markdown(f"Selecione as tarefas que deseja realizar e clique em **Iniciar** para completá-las. Você precisa completar **3 tarefas** para avançar.")
    
    progress_val = min(st.session_state.tasks_completed / 3, 1.0)
    st.progress(progress_val)
    st.markdown(f"**{st.session_state.tasks_completed}/3** tarefas completadas")
    st.markdown("---")

    # Destacar tarefas do perfil do usuário
    user_profile_label = ""
    if st.session_state.profile:
        for k in ["Executor", "Organizador", "Criativo"]:
            if k in st.session_state.profile:
                user_profile_label = k
                break

    if user_profile_label:
        st.info(f"✨ Tarefas marcadas com **⭐** são recomendadas para o perfil **{st.session_state.profile}**")

    for task in ALL_TASKS:
        tid = task["id"]
        is_done = tid in st.session_state.completed_tasks
        is_selected = st.session_state.selected_task == tid

        # Badge de recomendação
        rec_badge = " ⭐ Recomendada" if task["profile"] == user_profile_label else ""

        if is_done:
            st.markdown(f"""
            <div class="task-card-done">
                <strong>{task['icon']} {task['name']}</strong>{rec_badge}<br>
                <small style="color:#16a34a;">✅ Concluída</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            card_class = "task-card-selected" if is_selected else "task-card"
            st.markdown(f"""
            <div class="{card_class}">
                <strong>{task['icon']} {task['name']}</strong>{rec_badge}<br>
                <small style="color:#64748B;">{task['desc']}</small>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns([3, 1])
            with col1:
                btn_label = "✅ Selecionada — Iniciar" if is_selected else "Selecionar"
                btn_type = "primary" if is_selected else "secondary"
                if st.button(btn_label, key=f"sel_{tid}", use_container_width=True, type=btn_type):
                    if is_selected:
                        # Completar a tarefa
                        st.session_state.completed_tasks.add(tid)
                        st.session_state.tasks_completed = len(st.session_state.completed_tasks)
                        st.session_state.selected_task = None
                        if st.session_state.tasks_completed >= 3:
                            st.success("🎉 3 tarefas concluídas! Calculando seu IAP...")
                            st.session_state.step = "iap"
                        st.rerun()
                    else:
                        st.session_state.selected_task = tid
                        st.rerun()
            with col2:
                if is_selected:
                    if st.button("Cancelar", key=f"cancel_{tid}", use_container_width=True):
                        st.session_state.selected_task = None
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
        st.session_state.iap_score = random.randint(72, 96)

    score = st.session_state.iap_score

    st.markdown("## 📊 Seu Índice de Autonomia Produtiva (IAP)")
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.metric(label="IAP Score", value=f"{score}%", delta="↑ Acima da média")
        st.progress(score / 100)

    st.info("""
**O que é o IAP?**

O Índice de Autonomia Produtiva mede sua capacidade de iniciar, executar e
completar tarefas de forma independente. Quanto maior o IAP, maior sua autonomia!
    """)

    st.markdown("### 📈 Detalhamento do Desempenho")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Iniciativa", f"{random.randint(75, 95)}%")
    with col_b:
        st.metric("Execução", f"{random.randint(80, 96)}%")
    with col_c:
        st.metric("Conclusão", f"{random.randint(82, 98)}%")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Descobrir meu Perfil →", use_container_width=True, type="primary"):
        st.session_state.step = "profile"
        st.rerun()

# ========================
# PERFIL
# ========================
def show_profile():
    if not st.session_state.profile:
        st.session_state.profile = compute_profile()

    profile = st.session_state.profile
    st.markdown(f"## Seu Perfil: {profile}")
    st.balloons()

    profile_info = {
        "Executor": {
            "desc": "Você é orientado à ação e resultados. Prefere fazer do que planejar excessivamente. Sua força está na capacidade de colocar ideias em prática com agilidade.",
            "forças": ["⚡ Implementação rápida", "🎯 Foco total em resultados", "🔄 Alta adaptabilidade à mudança"],
            "dicas": [
                "Use blocos de foco de 25 min (Técnica Pomodoro)",
                "Divida projetos grandes em micro-tarefas imediatas",
                "Celebre pequenas conquistas para manter o momentum",
            ]
        },
        "Organizador": {
            "desc": "Você valoriza estrutura, clareza e planejamento. Gosta de ter processos definidos e tudo sob controle, entregando com consistência e confiabilidade.",
            "forças": ["📅 Planejamento detalhado", "🗂️ Organização impecável", "⏱️ Gestão de tempo precisa"],
            "dicas": [
                "Crie checklists para cada projeto ou meta",
                "Use ferramentas de calendário e bloco de tempo",
                "Defina prazos realistas com margens de segurança",
            ]
        },
        "Criativo": {
            "desc": "Você é inovador e está sempre explorando novas possibilidades. Pensa fora da caixa, encontra soluções originais e se destaca quando tem liberdade para criar.",
            "forças": ["🌟 Pensamento divergente", "💫 Inovação constante", "🎨 Flexibilidade mental elevada"],
            "dicas": [
                "Reserve tempo diário para brainstorm livre",
                "Mantenha um caderno de ideias sempre acessível",
                "Experimente métodos diferentes para evitar bloqueio criativo",
            ]
        },
    }

    key = next((k for k in profile_info if k in profile), "Executor")
    info = profile_info[key]

    st.markdown(f"_{info['desc']}_")
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💪 Suas Forças")
        for f in info["forças"]:
            st.success(f)
    with col2:
        st.markdown("### 💡 Dicas Personalizadas")
        for d in info["dicas"]:
            st.info(d)

    st.markdown("---")
    if st.button("🤖 Conversar com IA Personalizada →", use_container_width=True, type="primary"):
        st.session_state.step = "chat"
        st.rerun()

# ========================
# CHAT
# ========================
def show_chat():
    st.markdown(f"## 🤖 Assistente IA")
    st.info(f"💬 Chat personalizado para o perfil **{st.session_state.profile}** | IAP: **{st.session_state.iap_score}%**")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Faça uma pergunta sobre produtividade..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        profile_tips = {
            "Executor": [
                "focar em ação imediata — divida a tarefa em 3 passos pequenos e comece agora",
                "criar um senso de urgência artificial: defina um timer de 20 minutos e execute sem interrupções",
                "começar pela parte mais fácil para ganhar momentum e depois avançar para o que é mais difícil",
            ],
            "Organizador": [
                "criar um checklist claro antes de começar, identificando dependências e prazos",
                "bloquear tempo específico no calendário para essa atividade e protegê-lo de interrupções",
                "mapear os riscos e ter um plano B antes de iniciar a execução",
            ],
            "Criativo": [
                "explorar múltiplas abordagens antes de se comprometer com uma — faça um rápido brainstorm de 5 minutos",
                "buscar referências externas ou analogias de outras áreas para encontrar uma solução original",
                "trabalhar em rajadas curtas e intensas de criatividade, descansando entre elas",
            ],
        }

        key = next((k for k in profile_tips if k in st.session_state.profile), "Executor")
        tip = random.choice(profile_tips[key])

        response = f"""Como **{st.session_state.profile}** com IAP de **{st.session_state.iap_score}%**, recomendo {tip}.

Sobre sua pergunta — *"{prompt}"*:

{random.choice([
    "Uma abordagem eficaz é começar pela parte mais desafiadora quando sua energia estiver no pico, geralmente pela manhã.",
    "Experimente a técnica Pomodoro: 25 minutos de foco total, 5 minutos de pausa. Repita 4 vezes e faça uma pausa longa.",
    "Divida essa questão em 3 partes menores e resolva uma de cada vez. Completar cada parte já gera motivação para a próxima.",
    "O segredo está em criar um sistema que funcione independentemente da motivação do momento. Consistência supera inspiração.",
    "Identifique qual é a menor ação possível que avança esse objetivo e faça ela agora. Pequenos passos criam grandes resultados.",
])}

Quer que eu aprofunde algum ponto específico ou sugira exercícios práticos?"""

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Recomeçar Jornada", use_container_width=True):
            for k in ["step", "current_question", "answers", "tasks_completed",
                      "completed_tasks", "selected_task", "iap_score", "profile", "messages"]:
                st.session_state[k] = defaults[k]
            st.rerun()
    with col2:
        if st.button("📊 Ver Meu Perfil Novamente", use_container_width=True):
            st.session_state.step = "profile"
            st.rerun()

# ========================
# MAIN ROUTER
# ========================
if not st.session_state.logged_in:
    page_map = {
        "landing": show_landing_page,
        "features": show_features_page,
        "login": show_login_page,
        "about": show_about_page,
        "lgpd": show_lgpd_page,
    }
    page_map.get(st.session_state.current_page, show_landing_page)()
else:
    show_app()
