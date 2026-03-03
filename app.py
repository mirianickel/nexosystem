import streamlit as st

st.set_page_config(page_title="EcoNexo's System", layout="centered")

# ------------------------
# SESSION STATE INIT
# ------------------------

if "step" not in st.session_state:
    st.session_state.step = "questionnaire"
    st.session_state.current_question = 0
    st.session_state.scores = {
        "Executor": 0,
        "Organizador": 0,
        "Criativo": 0
    }

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

options = {
    "3": 3,
    "2": 2,
    "1": 1,
    "0": 0
}

# ------------------------
# QUESTIONNAIRE
# ------------------------

if st.session_state.step == "questionnaire":
    st.title("EcoNexo's System")
    st.subheader("Descubra seu estilo funcional de trabalho")

    question, profile = questions[st.session_state.current_question]

    st.write(f"Pergunta {st.session_state.current_question + 1} de 15")
    st.write(question)

    answer = st.radio(
        "Escolha uma opção:",
        ["3 - Me afinou perfeitamente",
         "2 - Me afino",
         "1 - Me afino pouco",
         "0 - Não me afino"]
    )

    if st.button("Próxima"):
        score_value = int(answer[0])
        st.session_state.scores[profile] += score_value
        st.session_state.current_question += 1

        if st.session_state.current_question >= len(questions):
            st.session_state.step = "result"

        st.rerun()

# ------------------------
# RESULT
# ------------------------

if st.session_state.step == "result":
    st.title("Seu Resultado")

    scores = st.session_state.scores
    profile = max(scores, key=scores.get)

    st.write(f"Seu estilo funcional predominante é: **{profile}**")

    descriptions = {
        "Executor": "Você produz melhor quando entra em ação rapidamente e foca em resultados práticos.",
        "Organizador": "Você produz melhor quando trabalha com estrutura, método e planejamento claro.",
        "Criativo": "Você produz melhor quando pode inovar e colocar originalidade no que faz."
    }

    st.write(descriptions[profile])
    st.info("Este resultado representa seu estilo funcional de execução, não sua personalidade completa.")

    if st.button("Ir para Vitrine de Tarefas"):
        st.session_state.profile = profile
        st.session_state.step = "tasks"
        st.rerun()

# ------------------------
# TASKS
# ------------------------

if st.session_state.step == "tasks":
    st.title("Vitrine de Tarefas")

    tasks = [
        "Criar currículo estratégico",
        "Organizar finanças pessoais",
        "Criar apresentação de vendas",
        "Estruturar planejamento semanal",
        "Criar plano de ação 30 dias"
    ]

    selected_task = st.selectbox("Escolha sua tarefa:", tasks)

    if st.button("Iniciar Execução"):
        st.session_state.task = selected_task
        st.session_state.step = "execution"
        st.rerun()

# ------------------------
# EXECUTION
# ------------------------

if st.session_state.step == "execution":
    st.title("Execução Guiada")

    st.write(f"Tarefa escolhida: **{st.session_state.task}**")

    objective = st.text_input("1️⃣ Qual o objetivo específico dessa tarefa?")
    info = st.text_area("2️⃣ Quais informações você já tem?")
    draft = st.text_area("3️⃣ Escreva um primeiro rascunho:")

    if st.button("Finalizar Versão"):
        st.success("Parabéns! Você transformou intenção em entrega.")
        st.session_state.step = "iap"
        st.rerun()

# ------------------------
# IAP
# ------------------------

if st.session_state.step == "iap":
    st.title("Índice de Autonomia Produtiva (IAP)")

    clarity_before = st.slider("Antes do método, qual era sua clareza para executar? (0-10)", 0, 10)
    confidence_after = st.slider("Agora, qual sua confiança para repetir sozinho? (0-10)", 0, 10)
    transformed = st.radio("Você sente que transformou intenção em entrega real?", ["Sim", "Não"])

    if st.button("Finalizar"):
        st.success("Processo concluído com sucesso!")
        st.write("O IAP mede aumento de autonomia produtiva — não perfeição, mas capacidade prática.")
