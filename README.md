# Dashboard IoT - ThingSpeak

Um dashboard web simples para visualizar dados de sensores IoT do ThingSpeak com gráficos em tempo real.

## O que é este projeto?

Este projeto cria um **dashboard web** que:
- Mostra gráficos de temperatura e umidade
- Atualiza automaticamente a cada 30 segundos
- Funciona no seu navegador
- Permite configurar diferentes canais do ThingSpeak

## Como usar (Passo a Passo)

### 1. **Instalar Python** (se não tiver)
- Baixe Python em: https://python.org
- Durante a instalação, marque "Add Python to PATH"

### 2. **Instalar dependências**
Abra o terminal/prompt na pasta do projeto e digite:
```bash
pip install requests
```

### 3. **Executar o servidor**
No terminal, digite:
```bash
python server.py
```
Você verá:
```
Servidor rodando em http://localhost:8000
Acesse: http://localhost:8000/dashboard.html
```

### 4. **Abrir o dashboard**
- Abra seu navegador (Chrome, Firefox, Edge)
- Digite: `http://localhost:8000/dashboard.html`
- Pronto! Os gráficos devem aparecer

## Configuração

### **Como obter suas credenciais do ThingSpeak:**

1. **Acesse:** https://thingspeak.com
2. **Faça login** na sua conta (ou crie uma gratuita)
3. **Crie um canal** ou use um existente
4. **Anote:**
   - **Channel ID** (ID do canal)
   - **Read API Key** (chave de leitura)

### **Configurar no dashboard:**
1. No dashboard, digite seu **Channel ID** no campo "Canal"
2. Digite sua **Read API Key** no campo "API Key"
3. Clique em "CONFIRMAR"
4. Clique em "Atualizar"

### **Exemplo de configuração:**
- **Canal:** 1234567 (seu ID)
- **API Key:** ABCDEFGHIJKLMNOP (sua chave)

## Arquivos do Projeto

| Arquivo | O que faz |
|---------|-----------|
| `dashboard.html` | Interface web com gráficos |
| `server.py` | Servidor local (resolve problemas de CORS) |
| `ThingSpeakTest.PY` | Script Python para testar a API |
| `requirements.txt` | Lista de dependências Python |

## Solução de Problemas

### **"Erro CORS" ou gráficos não aparecem:**
- Certifique-se que o servidor está rodando (`python server.py`)
- Acesse via `http://localhost:8000/dashboard.html` (não abra o arquivo diretamente)

### **"Nenhum valor numérico encontrado":**
- Verifique se o canal tem dados nos campos `field1` e `field2`
- Confirme se a API Key está correta

### **Servidor não inicia:**
- Verifique se Python está instalado: `python --version`
- Instale as dependências: `pip install requests`

## Como funciona?

1. **Servidor Python** (`server.py`) roda na sua máquina
2. **Dashboard HTML** faz requisições para o servidor
3. **Servidor** busca dados do ThingSpeak (evita bloqueio CORS)
4. **Gráficos** são atualizados com os dados recebidos

## Recursos do Dashboard

- **Gráfico de Temperatura** (field2)
- **Gráfico de Umidade** (field1)
- **Atualização automática** (30 segundos)
- **Configuração flexível** (canal/API)
- **Interface responsiva** (funciona no celular)
- **Debug integrado** (F12 > Console)

## Precisa de ajuda?

1. **Abra o Console do navegador** (F12 > Console)
2. **Veja se há mensagens de erro**
3. **Verifique se o servidor está rodando**
4. **Confirme se os dados estão chegando**

---

**Desenvolvido para:** TADS034 - IoT Atividade  
**Tecnologias:** Python, HTML, JavaScript, Chart.js, ThingSpeak API