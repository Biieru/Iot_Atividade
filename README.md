# ThingSpeak Data Extractor

Script simples para extrair dados de temperatura e umidade do ThingSpeak.

## O que faz

- Conecta na API do ThingSpeak
- Extrai dados de temperatura e umidade
- Exibe os dados de forma organizada

## Como usar

1. **Instale a dependência:**
```bash
pip install requests
```

2. **Configure o arquivo:**
   - Abra `ThingSpeakTest.PY`
   - Substitua `SEU_CHANNEL_ID_AQUI` pelo ID do seu canal
   - Substitua `SUA_READ_API_KEY_AQUI` pela sua chave de leitura

3. **Execute:**
```bash
python ThingSpeakTest.PY
```

## Exemplo de saída

```
Extraindo dados do ThingSpeak...

=== DADOS EXTRAÍDOS ===
Canal: Meu Canal
Total de registros: 5
----------------------------------------
Registro 1:
  Data/Hora: 2023-12-15T14:30:25Z
  Temperatura: 23.5 °C
  Umidade: 65.2 %
------------------------------
Registro 2:
  Data/Hora: 2023-12-15T14:29:55Z
  Temperatura: 23.8 °C
  Umidade: 64.8 %
------------------------------
```

## Configuração do ThingSpeak

1. Crie uma conta em [thingspeak.com](https://thingspeak.com)
2. Crie um canal com:
   - Campo 1: Umidade
   - Campo 2: Temperatura
3. Copie o Channel ID e Read API Key
4. Cole no código Python
