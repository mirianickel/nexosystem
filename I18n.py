"""
EcoNexo Internationalization Module
Complete bilingual support (PT-BR / EN-US)
"""

# Translation strings
STRINGS = {
    # Navigation
    "nav_home": {"pt": "🏠 Home", "en": "🏠 Home"},
    "nav_features": {"pt": "📖 Funcionalidades", "en": "📖 Features"},
    "nav_about": {"pt": "👥 Sobre", "en": "👥 About"},
    "nav_contact": {"pt": "📬 Contato", "en": "📬 Contact"},
    "nav_lgpd": {"pt": "🔒 LGPD", "en": "🔒 Privacy"},
    "nav_login": {"pt": "Entrar", "en": "Login"},
    "nav_logout": {"pt": "Sair", "en": "Logout"},
    
    # Hero section
    "hero_title_1": {"pt": "Produtividade", "en": "Productivity"},
    "hero_title_2": {"pt": "Guiada", "en": "Guided"},
    "hero_title_3": {"pt": "e Inteligente", "en": "and Intelligent"},
    "hero_sub": {
        "pt": "Descubra seu perfil de trabalho, receba tarefas personalizadas e alcance autonomia produtiva real com IA.",
        "en": "Discover your work profile, get personalized tasks and achieve real productive autonomy with AI."
    },
    
    # Buttons
    "btn_start": {"pt": "🚀 Começar Agora", "en": "🚀 Get Started"},
    "btn_learn": {"pt": "📖 Saiba Mais", "en": "📖 Learn More"},
    "btn_login": {"pt": "Entrar", "en": "Login"},
    "btn_signup": {"pt": "Criar Conta", "en": "Sign Up"},
    "btn_save_settings": {"pt": "💾 Salvar", "en": "💾 Save"},
    "btn_send": {"pt": "📨 Enviar", "en": "📨 Send"},
    "btn_next": {"pt": "Próxima →", "en": "Next →"},
    "btn_prev": {"pt": "← Anterior", "en": "← Previous"},
    "btn_finish": {"pt": "✅ Finalizar", "en": "✅ Finish"},
    "btn_start_task": {"pt": "Iniciar", "en": "Start"},
    "btn_select": {"pt": "Selecionar", "en": "Select"},
    "btn_cancel": {"pt": "Cancelar", "en": "Cancel"},
    "btn_see_iap": {"pt": "Ver meu IAP →", "en": "See my IAP →"},
    "btn_see_profile": {"pt": "Descobrir meu Perfil →", "en": "Discover my Profile →"},
    "btn_chat": {"pt": "🤖 Conversar com IA →", "en": "🤖 Chat with AI →"},
    "btn_clear_chat": {"pt": "🗑️ Limpar Chat", "en": "🗑️ Clear Chat"},
    "btn_restart": {"pt": "🔄 Recomeçar", "en": "🔄 Restart"},
    "btn_see_profile_again": {"pt": "📊 Ver Perfil", "en": "📊 See Profile"},
    
    # Login/Signup
    "login_title": {"pt": "🔐 Acesse sua conta", "en": "🔐 Access your account"},
    "tab_login": {"pt": "✉️ Entrar", "en": "✉️ Login"},
    "tab_signup": {"pt": "📝 Criar Conta", "en": "📝 Sign Up"},
    "field_email": {"pt": "📧 Email", "en": "📧 Email"},
    "field_password": {"pt": "🔒 Senha", "en": "🔒 Password"},
    "field_name": {"pt": "👤 Nome Completo", "en": "👤 Full Name"},
    "lgpd_agree": {
        "pt": "Concordo com a Política de Privacidade (LGPD)",
        "en": "I agree to the Privacy Policy"
    },
    
    # Errors
    "err_fill": {"pt": "❌ Preencha todos os campos", "en": "❌ Fill in all fields"},
    "err_lgpd": {"pt": "❌ Aceite a política de privacidade", "en": "❌ Accept the privacy policy"},
    "err_pw_len": {"pt": "❌ Senha deve ter mínimo 8 caracteres", "en": "❌ Password must be at least 8 characters"},
    "err_credentials": {"pt": "❌ Email ou senha incorretos", "en": "❌ Invalid email or password"},
    "err_email_exists": {"pt": "❌ Email já cadastrado", "en": "❌ Email already registered"},
    
    # Success messages
    "login_success": {"pt": "✅ Login realizado!", "en": "✅ Login successful!"},
    "signup_success": {"pt": "✅ Conta criada!", "en": "✅ Account created!"},
    "contact_sent": {
        "pt": "✅ Mensagem enviada! Responderemos em breve.",
        "en": "✅ Message sent! We will reply soon."
    },
    "settings_saved": {"pt": "✅ Preferências salvas!", "en": "✅ Settings saved!"},
    
    # About page
    "about_title": {"pt": "Quem Somos", "en": "About Us"},
    "about_mission": {"pt": "Nossa Missão", "en": "Our Mission"},
    "about_values": {"pt": "Nossos Valores", "en": "Our Values"},
    
    # Contact page
    "contact_title": {"pt": "Fale Conosco", "en": "Contact Us"},
    "contact_name": {"pt": "Nome", "en": "Name"},
    "contact_email": {"pt": "Email", "en": "Email"},
    "contact_subject": {"pt": "Assunto", "en": "Subject"},
    "contact_message": {"pt": "Mensagem", "en": "Message"},
    
    # Questionnaire
    "q_title": {"pt": "Questionário de Perfil", "en": "Profile Questionnaire"},
    "q_question": {"pt": "Pergunta", "en": "Question"},
    "q_of": {"pt": "de", "en": "of"},
    "q_identify": {
        "pt": "Para cada opção, indique o quanto você se identifica:",
        "en": "For each option, indicate how much you identify:"
    },
    "aff_1": {"pt": "Me identifico totalmente", "en": "Fully identify"},
    "aff_2": {"pt": "Me identifico parcialmente", "en": "Partially identify"},
    "aff_3": {"pt": "Não me identifico muito", "en": "Barely identify"},
    "aff_4": {"pt": "Não me identifico", "en": "Do not identify"},
    
    # Tasks
    "tasks_title": {"pt": "Vitrine de Tarefas", "en": "Task Showcase"},
    "tasks_done": {"pt": "tarefas completadas", "en": "tasks completed"},
    "tasks_all_done": {
        "pt": "🎉 Parabéns! 3 tarefas concluídas!",
        "en": "🎉 Congrats! 3 tasks completed!"
    },
    "task_recommended": {"pt": "⭐ Recomendada", "en": "⭐ Recommended"},
    "task_done_label": {"pt": "✅ Concluída", "en": "✅ Done"},
    
    # IAP
    "iap_title": {
        "pt": "Índice de Autonomia Produtiva",
        "en": "Productive Autonomy Index"
    },
    "iap_above": {"pt": "Acima da média ↑", "en": "Above average ↑"},
    "iap_detail": {"pt": "Detalhamento", "en": "Details"},
    "iap_initiative": {"pt": "Iniciativa", "en": "Initiative"},
    "iap_execution": {"pt": "Execução", "en": "Execution"},
    "iap_conclusion": {"pt": "Conclusão", "en": "Conclusion"},
    "iap_what": {"pt": "O que é o IAP?", "en": "What is the IAP?"},
    "iap_desc": {
        "pt": "O Índice de Autonomia Produtiva mede sua capacidade de iniciar, executar e completar tarefas de forma independente. Quanto maior o IAP, maior sua autonomia!",
        "en": "The Productive Autonomy Index measures your ability to start, execute and complete tasks independently. The higher the IAP, the greater your autonomy!"
    },
    
    # Profile
    "profile_title": {"pt": "Seu Perfil", "en": "Your Profile"},
    "profile_strengths": {"pt": "💪 Suas Forças", "en": "💪 Your Strengths"},
    "profile_tips": {"pt": "💡 Dicas Personalizadas", "en": "💡 Personalized Tips"},
    
    # Chat
    "chat_title": {"pt": "Assistente IA", "en": "AI Assistant"},
    "chat_context": {"pt": "Perfil:", "en": "Profile:"},
    "chat_placeholder": {
        "pt": "Faça uma pergunta sobre produtividade...",
        "en": "Ask a productivity question..."
    },
    
    # Settings
    "settings_title": {"pt": "Preferências", "en": "Settings"},
    "settings_theme": {"pt": "Tema", "en": "Theme"},
    "settings_theme_light": {"pt": "☀️ Claro", "en": "☀️ Light"},
    "settings_theme_dark": {"pt": "🌙 Escuro", "en": "🌙 Dark"},
    "settings_font": {"pt": "Tamanho da Fonte", "en": "Font Size"},
    "settings_font_sm": {"pt": "Pequeno", "en": "Small"},
    "settings_font_md": {"pt": "Médio", "en": "Medium"},
    "settings_font_lg": {"pt": "Grande", "en": "Large"},
    "settings_lang": {"pt": "Idioma", "en": "Language"},
    
    # Profile types
    "executor_name": {"pt": "Executor", "en": "Executor"},
    "executor_desc": {
        "pt": "Focado em ação rápida e resultados imediatos",
        "en": "Focused on quick action and immediate results"
    },
    "organizer_name": {"pt": "Organizador", "en": "Organizer"},
    "organizer_desc": {
        "pt": "Estrutura processos e planeja com precisão",
        "en": "Structures processes and plans with precision"
    },
    "creative_name": {"pt": "Criativo", "en": "Creative"},
    "creative_desc": {
        "pt": "Inova constantemente e explora novas ideias",
        "en": "Constantly innovates and explores new ideas"
    },
    
    # Footer
    "footer_rights": {
        "pt": "© 2026 EcoNexo's System — Todos os direitos reservados",
        "en": "© 2026 EcoNexo's System — All rights reserved"
    },
}


def t(key: str, lang: str = "pt") -> str:
    """Get translated string"""
    return STRINGS.get(key, {}).get(lang, STRINGS.get(key, {}).get("pt", key))


# Questionnaire data
QUESTIONS = {
    "pt": [
        {
            "q": "Como você costuma iniciar um projeto?",
            "opts": [
                ("Executor", "Pulo direto para a ação, sem muita análise prévia"),
                ("Organizador", "Faço um planejamento detalhado antes de começar"),
                ("Criativo", "Exploro ideias e possibilidades primeiro")
            ]
        },
        {
            "q": "O que mais te motiva no trabalho?",
            "opts": [
                ("Executor", "Ver resultados rápidos e tangíveis"),
                ("Organizador", "Ter processos claros e tudo bem organizado"),
                ("Criativo", "Criar algo novo e inovador")
            ]
        },
        {
            "q": "Como você lida com prazos apertados?",
            "opts": [
                ("Executor", "Trabalho melhor sob pressão, entro no modo foco"),
                ("Organizador", "Planejo com antecedência para evitar correria"),
                ("Criativo", "Adapto o escopo do trabalho conforme a situação")
            ]
        },
        {
            "q": "Qual é o seu maior ponto forte?",
            "opts": [
                ("Executor", "Colocar ideias em prática rapidamente"),
                ("Organizador", "Manter tudo estruturado e dentro do prazo"),
                ("Criativo", "Encontrar soluções originais para problemas")
            ]
        },
        {
            "q": "Como você prefere receber tarefas?",
            "opts": [
                ("Executor", "Direto ao ponto: o que fazer e até quando"),
                ("Organizador", "Com contexto, critérios e checklist claros"),
                ("Criativo", "Com liberdade para interpretar e criar a abordagem")
            ]
        },
        {
            "q": "Quando um projeto não vai bem, o que você faz?",
            "opts": [
                ("Executor", "Tomo uma decisão rápida e mudo o curso da ação"),
                ("Organizador", "Reviso o planejamento e identifico onde errei"),
                ("Criativo", "Busco uma abordagem completamente diferente")
            ]
        },
        {
            "q": "Como você organiza seu dia de trabalho?",
            "opts": [
                ("Executor", "Faço as tarefas conforme chegam, priorizando urgência"),
                ("Organizador", "Tenho uma lista priorizada e sigo ela rigorosamente"),
                ("Criativo", "Trabalho no que me inspira mais em cada momento")
            ]
        },
    ],
    "en": [
        {
            "q": "How do you usually start a project?",
            "opts": [
                ("Executor", "I jump straight into action without much prior analysis"),
                ("Organizer", "I make a detailed plan before starting"),
                ("Creative", "I explore ideas and possibilities first")
            ]
        },
        {
            "q": "What motivates you most at work?",
            "opts": [
                ("Executor", "Seeing quick, tangible results"),
                ("Organizer", "Having clear processes and everything organized"),
                ("Creative", "Creating something new and innovative")
            ]
        },
        {
            "q": "How do you handle tight deadlines?",
            "opts": [
                ("Executor", "I work better under pressure, I enter focus mode"),
                ("Organizer", "I plan ahead to avoid last-minute rush"),
                ("Creative", "I adapt the scope of work as needed")
            ]
        },
        {
            "q": "What is your greatest strength?",
            "opts": [
                ("Executor", "Putting ideas into practice quickly"),
                ("Organizer", "Keeping everything structured and on time"),
                ("Creative", "Finding original solutions to problems")
            ]
        },
        {
            "q": "How do you prefer to receive tasks?",
            "opts": [
                ("Executor", "Straight to the point: what to do and by when"),
                ("Organizer", "With context, clear criteria and checklists"),
                ("Creative", "With freedom to interpret and create the approach")
            ]
        },
        {
            "q": "When a project is not going well, what do you do?",
            "opts": [
                ("Executor", "I make a quick decision and change course"),
                ("Organizer", "I review the plan and identify where I went wrong"),
                ("Creative", "I look for a completely different approach")
            ]
        },
        {
            "q": "How do you organize your workday?",
            "opts": [
                ("Executor", "I do tasks as they come, prioritizing urgency"),
                ("Organizer", "I have a prioritized list and follow it strictly"),
                ("Creative", "I work on what inspires me most at each moment")
            ]
        },
    ]
}


# Task definitions
TASKS = {
    "pt": [
        {
            "id": 0,
            "icon": "✉️",
            "name": "Escrever um email profissional",
            "desc": "Rascunhe um email claro e objetivo para um colega ou cliente.",
            "profile": "Executor"
        },
        {
            "id": 1,
            "icon": "📝",
            "name": "Organizar lista de prioridades do dia",
            "desc": "Liste e priorize as 5 tarefas mais importantes para hoje.",
            "profile": "Organizador"
        },
        {
            "id": 2,
            "icon": "💡",
            "name": "Brainstorm de ideias criativas",
            "desc": "Gere 10 ideias para solucionar um problema do seu trabalho.",
            "profile": "Criativo"
        },
        {
            "id": 3,
            "icon": "📄",
            "name": "Revisar um documento importante",
            "desc": "Releia e melhore um documento em que está trabalhando.",
            "profile": "Organizador"
        },
        {
            "id": 4,
            "icon": "📅",
            "name": "Planejar a próxima semana",
            "desc": "Monte um plano realista para os próximos 7 dias.",
            "profile": "Organizador"
        },
        {
            "id": 5,
            "icon": "⚡",
            "name": "Resolver uma tarefa pendente há dias",
            "desc": "Escolha algo que está procrastinando e finalize agora.",
            "profile": "Executor"
        },
        {
            "id": 6,
            "icon": "🎨",
            "name": "Criar um esboço visual ou mapa mental",
            "desc": "Desenhe ou descreva visualmente um projeto ou ideia.",
            "profile": "Criativo"
        },
        {
            "id": 7,
            "icon": "📊",
            "name": "Analisar métricas ou resultados",
            "desc": "Revise números, dados ou indicadores do seu trabalho.",
            "profile": "Executor"
        },
    ],
    "en": [
        {
            "id": 0,
            "icon": "✉️",
            "name": "Write a professional email",
            "desc": "Draft a clear, objective email to a colleague or client.",
            "profile": "Executor"
        },
        {
            "id": 1,
            "icon": "📝",
            "name": "Organize today's priority list",
            "desc": "List and prioritize the 5 most important tasks for today.",
            "profile": "Organizer"
        },
        {
            "id": 2,
            "icon": "💡",
            "name": "Creative brainstorming session",
            "desc": "Generate 10 ideas to solve a problem at work.",
            "profile": "Creative"
        },
        {
            "id": 3,
            "icon": "📄",
            "name": "Review an important document",
            "desc": "Re-read and improve a document you are working on.",
            "profile": "Organizer"
        },
        {
            "id": 4,
            "icon": "📅",
            "name": "Plan next week",
            "desc": "Build a realistic plan for the next 7 days.",
            "profile": "Organizer"
        },
        {
            "id": 5,
            "icon": "⚡",
            "name": "Resolve a long-pending task",
            "desc": "Pick something you have been procrastinating and finish it now.",
            "profile": "Executor"
        },
        {
            "id": 6,
            "icon": "🎨",
            "name": "Create a visual sketch or mind map",
            "desc": "Draw or visually describe a project or idea.",
            "profile": "Creative"
        },
        {
            "id": 7,
            "icon": "📊",
            "name": "Analyze metrics or results",
            "desc": "Review numbers, data or indicators from your work.",
            "profile": "Executor"
        },
    ]
}


# Profile information
PROFILE_INFO = {
    "pt": {
        "Executor": {
            "icon": "🎯",
            "desc": "Você é orientado à ação e resultados. Prefere fazer do que planejar excessivamente. Sua força está na capacidade de colocar ideias em prática com agilidade.",
            "strengths": [
                "⚡ Implementação rápida",
                "🎯 Foco total em resultados",
                "🔄 Alta adaptabilidade à mudança"
            ],
            "tips": [
                "Use blocos de foco de 25 min (Técnica Pomodoro)",
                "Divida projetos grandes em micro-tarefas imediatas",
                "Celebre pequenas conquistas para manter o momentum"
            ],
        },
        "Organizador": {
            "icon": "📋",
            "desc": "Você valoriza estrutura, clareza e planejamento. Gosta de ter processos definidos e tudo sob controle, entregando com consistência e confiabilidade.",
            "strengths": [
                "📅 Planejamento detalhado",
                "🗂️ Organização impecável",
                "⏱️ Gestão de tempo precisa"
            ],
            "tips": [
                "Crie checklists para cada projeto ou meta",
                "Use ferramentas de calendário e bloco de tempo",
                "Defina prazos realistas com margens de segurança"
            ],
        },
        "Criativo": {
            "icon": "💡",
            "desc": "Você é inovador e está sempre explorando novas possibilidades. Pensa fora da caixa, encontra soluções originais e se destaca quando tem liberdade para criar.",
            "strengths": [
                "🌟 Pensamento divergente",
                "💫 Inovação constante",
                "🎨 Flexibilidade mental elevada"
            ],
            "tips": [
                "Reserve tempo diário para brainstorm livre",
                "Mantenha um caderno de ideias sempre acessível",
                "Experimente métodos diferentes para evitar bloqueio criativo"
            ],
        },
    },
    "en": {
        "Executor": {
            "icon": "🎯",
            "desc": "You are action and results oriented. You prefer doing over excessive planning. Your strength lies in your ability to put ideas into practice with agility.",
            "strengths": [
                "⚡ Fast implementation",
                "🎯 Total focus on results",
                "🔄 High adaptability to change"
            ],
            "tips": [
                "Use 25-minute focus blocks (Pomodoro Technique)",
                "Break large projects into immediate micro-tasks",
                "Celebrate small wins to maintain momentum"
            ],
        },
        "Organizer": {
            "icon": "📋",
            "desc": "You value structure, clarity and planning. You like having defined processes and everything under control, delivering with consistency and reliability.",
            "strengths": [
                "📅 Detailed planning",
                "🗂️ Impeccable organization",
                "⏱️ Precise time management"
            ],
            "tips": [
                "Create checklists for every project or goal",
                "Use calendar tools and time blocking",
                "Set realistic deadlines with safety margins"
            ],
        },
        "Creative": {
            "icon": "💡",
            "desc": "You are innovative and always exploring new possibilities. You think outside the box, find original solutions and excel when you have freedom to create.",
            "strengths": [
                "🌟 Divergent thinking",
                "💫 Constant innovation",
                "🎨 High mental flexibility"
            ],
            "tips": [
                "Reserve daily time for free brainstorming",
                "Keep an idea notebook always accessible",
                "Try different methods to avoid creative blocks"
            ],
        },
    },
}
