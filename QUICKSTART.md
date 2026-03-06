# 🚀 Início Rápido - EcoNexo v2.0

## ⚡ 3 Minutos para Começar

### Passo 1: Instalar Dependências (1 min)

```bash
pip install -r requirements.txt
```

Ou use o setup completo:
```bash
python setup.py
```

### Passo 2: Configurar API Key (1 min)

Crie arquivo `.env` (ou copie do `.env.example`):

```bash
cp .env.example .env
```

Edite `.env` e adicione sua API key:
```
ANTHROPIC_API_KEY=sk-ant-api03-SEU_KEY_AQUI
```

**Obter key grátis:** https://console.anthropic.com/

### Passo 3: Executar (1 min)

```bash
streamlit run main.py
```

Abra: http://localhost:8501

---

## ✅ Checklist

- [ ] Python 3.8+ instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` criado com `ANTHROPIC_API_KEY`
- [ ] App rodando (`streamlit run main.py`)

---

## 🎯 Primeiro Uso

1. **Criar Conta**
   - Clique em "Criar Conta"
   - Preencha nome, email, senha
   - Aceite política de privacidade

2. **Responder Questionário**
   - 7 perguntas sobre seu estilo de trabalho
   - Identifica seu perfil (Executor/Organizador/Criativo)

3. **Completar Tarefas**
   - Escolha 3 tarefas da vitrine
   - Tarefas ⭐ são recomendadas para você

4. **Ver seu IAP**
   - Índice de Autonomia Produtiva
   - Score detalhado por dimensões

5. **Chat com IA**
   - Assistente personalizado para seu perfil
   - Ferramentas de produtividade integradas

---

## 🔧 Problemas Comuns

### Erro: "No module named 'streamlit'"
```bash
pip install streamlit
```

### Erro: "No module named 'anthropic'"
```bash
pip install anthropic
```

### Erro: "ANTHROPIC_API_KEY not found"
- Certifique-se que `.env` existe
- Verifique se a key está correta
- Reinicie a aplicação

### Database não inicializa
```bash
python -c "import database; database.init_database()"
```

---

## 📚 Próximos Passos

- Explore as **ferramentas do AI Agent** no chat
- Veja **analytics** de produtividade
- Teste em **outro idioma** (PT/EN)
- Experimente **tema escuro**

---

## 🆘 Precisa de Ajuda?

1. Execute os testes: `python test_suite.py`
2. Veja logs no terminal
3. Consulte o README.md completo
4. Abra uma issue no GitHub

---

**Divirta-se! 🎉**
