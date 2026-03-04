import streamlit as st
import requests

st.set_page_config(page_title="EcoNexo's System", layout="centered")

# ------------------------
# SESSION STATE INIT
# ------------------------

if "step" not in st.session_state:
    st.session_state.step = "login"
    st.session_state.current_question = 0
    st.session_state.scores = {"Executor": 0, "Organizador": 0, "Criativo": 0}
    st.session_state.user = None
    st.session_state.completed_tasks = []
    st.session_state.chat_history = []

# Simulated user DB (in-memory)
if "users_db" not in st.session_state:
    st.session_state.users_db = {}

# ------------------------
# QUESTIONS
# ------------------------

questions = [
    ("Quando recebo um desafio, prefiro começar a praticar imediatamente.", "Executor"),
    ("Sinto-me mais produtivo quando começo o dia com lista clara.", "Organizador"),
    ("Sinto-me motivado quando posso criar algo do zero.", "Criativo"),
    ("Foco mais em concluir tarefas do que no processo.", "Executor"),
    ("Manter arquivos organizados é essencial.", "Organizador"),
    ("Trabalho melhor em ambientes criativos.", "Criativo"),
    ("Prefiro testar soluções rápidas diante de obstáculos.", "Executor"),
    ("Prefiro seguir método testado passo a passo.", "Organizador"),
    ("Busco soluções inovadoras para problemas.", "Criativo"),
    ("Gosto de entregar resultados em prazo curto.", "Executor"),
    ("Valorizo precisão acima da velocidade.", "Organizador"),
    ("Preocupo-me com estética e originalidade.", "Criativo"),
    ("Minha maior satisfação é ver o produto final pronto.", "Executor"),
    ("Realização é ver fluxo organizado funcionando.", "Organizador"),
    ("Sucesso é expressar identidade no resultado final.", "Criativo"),
]

answer_options = [
    "Me afino totalmente",
    "Me afino parcialmente",
    "Não me afino parcialmente",
    "Não me afino totalmente"
]
answer_scores = [3, 2, 1, 0]

tasks_list = [
    "Criar currículo estratégico",
    "Organizar finanças pessoais",
    "Criar apresentação de vendas",
    "Estruturar planejamento semanal",
    "Criar plano de ação 30 dias"
]

# ------------------------
# HELPER: AI CHAT (OpenRouter free)
# ------------------------

def ask_ai(messages):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer sk-or-v1-free",  # placeholder; user should add key
                "Content-Type": "application/json",
            },
            json={
                "model": "mistralai/mistral-7b-instruct:free",
                "messages": messages,
            },
            timeout=15
        )
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ Erro ao conectar com IA: {e}"

# ========================
# STEP: LOGIN / CADASTRO
# ========================

if st.session_state.step == "login":
    st.title("EcoNexo's System")
    st.subheader("Bem-vindo! Entre ou crie sua conta.")

    tab_login, tab_register = st.tabs(["Entrar", "Criar Conta"])

    with tab_login:
        email = st.text_input("E-mail", key="login_email")
        password = st.text_input("Senha", type="password", key="login_pass")
        if st.button("Entrar"):
            db = st.session_state.users_db
            if email in db and db[email]["password"] == password:
                st.session_state.user = {"email": email, "name": db[email]["name"]}
                st.session_state.step = "questionnaire"
                st.rerun()
            else:
                st.error("E-mail ou senha incorretos.")

    with tab_register:
        name = st.text_input("Nome completo", key="reg_name")
        email_r = st.text_input("E-mail", key="reg_email")
        password_r = st.text_input("Senha", type="password", key="reg_pass")
        if st.button("Criar conta"):
            if email_r and password_r and name:
                st.session_state.users_db[email_r] = {"name": name, "password": password_r}
                st.session_state.user = {"email": email_r, "name": name}
                st.session_state.step = "questionnaire"
                st.rerun()
            else:
                st.error("Preencha todos os campos.")

# ========================
# STEP: QUESTIONNAIRE
# ========================

elif st.session_state.step == "questionnaire":
    st.title("EcoNexo's System")
    st.subheader(f"Olá, {st.session_state.user['name']}! Descubra seu estilo funcional.")

    q_idx = st.session_state.current_question
    question, profile = questions[q_idx]

    progress = q_idx / len(questions)
    st.progress(progress, text=f"Pergunta {q_idx + 1} de {len(questions)}")
    st.write(question)

    answer = st.radio("Escolha uma opção:", answer_options, key=f"q_{q_idx}")

    if st.button("Próxima"):
        score_value = answer_scores[answer_options.index(answer)]
        st.session_state.scores[profile] += score_value
        st.session_state.current_question += 1

        if st.session_state.current_question >= len(questions):
            st.session_state.step = "tasks"
        st.rerun()

# ========================
# STEP: TASKS (3 obrigatórias)
# ========================

elif st.session_state.step == "tasks":
    completed = st.session_state.completed_tasks
    remaining = [t for t in tasks_list if t not in completed]

    st.title("Vitrine de Tarefas")
    st.info(f"Conclua **3 tarefas** para liberar seu IAP. ({len(completed)}/3 concluídas)")

    if len(completed) >= 3:
        st.session_state.step = "iap"
        st.rerun()

    if remaining:
        selected_task = st.selectbox("Escolha sua próxima tarefa:", remaining)
        if st.button("Iniciar Execução"):
            st.session_state.task = selected_task
            st.session_state.step = "execution"
            st.rerun()

    if completed:
        st.markdown("**Tarefas concluídas:**")
        for t in completed:
            st.write(f"✅ {t}")

# ========================
# STEP: EXECUTION
# ========================

elif st.session_state.step == "execution":
    st.title("Execução Guiada")
    st.write(f"Tarefa: **{st.session_state.task}**")

    objective = st.text_input("1️⃣ Qual o objetivo específico dessa tarefa?")
    info = st.text_area("2️⃣ Quais informações você já tem?")
    draft = st.text_area("3️⃣ Escreva um primeiro rascunho:")

    if st.button("Finalizar Versão"):
        st.session_state.completed_tasks.append(st.session_state.task)
        st.success("Parabéns! Você transformou intenção em entrega.")
        st.session_state.step = "tasks"
        st.rerun()

# ========================
# STEP: IAP
# ========================

elif st.session_state.step == "iap":
    st.title("Índice de Autonomia Produtiva (IAP)")

    clarity_before = st.slider("Antes do método, qual era sua clareza para executar? (0–10)", 0, 10, key="clarity")
    confidence_after = st.slider("Agora, qual sua confiança para repetir sozinho? (0–10)", 0, 10, key="confidence")
    transformed = st.radio("Você sente que transformou intenção em entrega real?", ["Sim", "Não"])

    if st.button("Ver meu IAP"):
        bonus = 10 if transformed == "Sim" else 0
        iap = round(((clarity_before + confidence_after) / 20) * 90 + bonus, 1)
        st.session_state.iap = iap
        st.session_state.step = "profiles"
        st.rerun()

# ========================
# STEP: PROFILES
# ========================

elif st.session_state.step == "profiles":
    scores = st.session_state.scores
    dominant = max(scores, key=scores.get)
    iap = st.session_state.get("iap", 0)

    # IAP display
    st.title("Seu Resultado Completo")
    col1, col2 = st.columns(2)
    with col1:
        color = "green" if iap >= 70 else "orange" if iap >= 40 else "red"
        st.metric("🎯 IAP — Autonomia Produtiva", f"{iap}/100")
        st.markdown(f"<div style='color:{color};font-weight:bold'>{'Alta autonomia ✅' if iap >= 70 else 'Autonomia em desenvolvimento 🔄' if iap >= 40 else 'Autonomia inicial 🌱'}</div>", unsafe_allow_html=True)
    with col2:
        total = sum(scores.values()) or 1
        for p, s in scores.items():
            pct = round((s / total) * 100)
            st.write(f"**{p}**: {pct}%")

    st.divider()

    # Profile cards
    st.subheader("Perfis de Produtividade")

    profiles = {
        "Executor": {
            "icon": "⚡",
            "desc": "Age rapidamente, foca em resultados práticos e entrega com velocidade.",
            "forças": ["Velocidade de execução", "Foco em resultados", "Adaptabilidade rápida"],
            "dicas": ["Use timers Pomodoro", "Defina metas diárias claras", "Celebre pequenas entregas"]
        },
        "Organizador": {
            "icon": "📋",
            "desc": "Produz melhor com estrutura, método e planejamento bem definido.",
            "forças": ["Precisão", "Consistência", "Planejamento eficaz"],
            "dicas": ["Use checklists detalhadas", "Bloqueie horários no calendário", "Documente processos"]
        },
        "Criativo": {
            "icon": "🎨",
            "desc": "Inova com facilidade, traz originalidade e pensa fora do padrão.",
            "forças": ["Inovação", "Visão única", "Solução criativa de problemas"],
            "dicas": ["Reserve tempo para brainstorm livre", "Use mapas mentais", "Trabalhe em blocos de foco profundo"]
        }
    }

    for name, data in profiles.items():
        is_dominant = name == dominant
        border = "3px solid #6366f1" if is_dominant else "1px solid #e5e7eb"
        with st.container():
            st.markdown(f"""
            <div style='border:{border};border-radius:12px;padding:16px;margin-bottom:12px;background:{"#eef2ff" if is_dominant else "#fafafa"}'>
            <h3>{data['icon']} {name} {"⭐ (seu perfil dominante)" if is_dominant else ""}</h3>
            <p>{data['desc']}</p>
            <b>Forças:</b> {" • ".join(data['forças'])}<br>
            <b>Dicas:</b> {" • ".join(data['dicas'])}
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # Chat IA
    st.subheader("💬 Chat com IA — Tire suas dúvidas")
    st.caption("IA gratuita integrada para te ajudar com produtividade.")

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Pergunte algo sobre seu perfil ou produtividade...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        system_msg = {
            "role": "system",
            "content": f"Você é um coach de produtividade do EcoNexo's System. O usuário tem perfil dominante '{dominant}' e IAP de {iap}/100. Responda em português, de forma prática e motivadora."
        }
        messages = [system_msg] + [{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history]
        with st.spinner("IA pensando..."):
            reply = ask_ai(messages)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

    if st.button("🔄 Refazer do início"):
        for key in list(st.session_state.keys()):
            if key != "users_db":
                del st.session_state[key]
        st.rerun()
