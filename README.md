# 🎯 EcoNexo's System v2.0

**Plataforma de produtividade com AI Agents, persistência SQL, suporte bilíngue e design inovador**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Características Principais

### 🤖 AI Agent com Arquitetura ReAct
- 4 ferramentas de produtividade integradas
- Sistema de memória (short-term, long-term, episodic, semantic)
- Logging completo de execução
- Suporte multi-provider (Anthropic Claude, Groq)

### 📊 Sistema de Perfis Personalizado
- Questionário de 7 perguntas
- 3 perfis: Executor, Organizador, Criativo
- IAP Score (Índice de Autonomia Produtiva)
- Recomendações personalizadas

### 💾 Database Robusto
- SQLite com connection pooling thread-safe
- 7 tabelas otimizadas
- Sistema de observabilidade
- Analytics integrado

### 🌐 Internacionalização Completa
- Suporte PT-BR / EN-US
- Interface totalmente traduzida
- Conteúdo localizado

---

## 🚀 Instalação Rápida

### Pré-requisitos
- Python 3.8+
- pip

### Passo 1: Clone/Download

```bash
# Se estiver no GitHub:
git clone https://github.com/seu-usuario/econexo-system.git
cd econexo-system

# Ou apenas extraia o ZIP
```

### Passo 2: Execute o Setup

```bash
python setup.py
```

O script irá:
- ✅ Verificar versão do Python
- ✅ Instalar dependências
- ✅ Criar arquivo .env
- ✅ Inicializar database
- ✅ Executar testes (opcional)

### Passo 3: Configure API Keys

Edite o arquivo `.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-api03-...
GROQ_API=gsk_...  # Opcional
```

**Como obter:**
- Anthropic: https://console.anthropic.com/
- Groq: https://console.groq.com/

### Passo 4: Execute a Aplicação

```bash
streamlit run main.py
```

Acesse: `http://localhost:8501`

---

## 📁 Estrutura do Projeto

```
econexo-system/
├── main.py              # Aplicação Streamlit principal
├── database.py          # Camada de persistência SQL
├── agent.py             # AI Agent com ferramentas
├── i18n.py              # Internacionalização
├── test_suite.py        # Suite de testes
├── setup.py             # Script de configuração
├── requirements.txt     # Dependências Python
├── .env.example         # Template de configuração
├── .streamlit/
│   └── config.toml      # Configuração do Streamlit
└── data/
    └── econexo.db       # Database SQLite (gerado)
```

---

## 🧪 Executar Testes

```bash
python test_suite.py
```

---

## 📦 Deploy

### Streamlit Cloud

1. Push para GitHub
2. Conecte no https://share.streamlit.io
3. Configure secrets (API keys)
4. Deploy!

### Docker

```bash
docker build -t econexo .
docker run -p 8501:8501 -e ANTHROPIC_API_KEY=... econexo
```

---

## 🛠️ Tecnologias

- **Frontend**: Streamlit
- **AI**: Anthropic Claude, Groq
- **Database**: SQLite
- **Testes**: unittest
- **Idiomas**: Python 3.8+

---

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/NovaFeature`
3. Commit: `git commit -m 'Adiciona NovaFeature'`
4. Push: `git push origin feature/NovaFeature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT - veja [LICENSE](LICENSE)

---

## 📞 Suporte

- **Email**: suporte@econexo.com
- **Issues**: Abra uma issue no GitHub

---

**Feito com ❤️ pela equipe EcoNexo**
