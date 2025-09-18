#!/usr/bin/env python3
"""
Servidor simples para servir o dashboard.html e fazer proxy para a API do ThingSpeak
Evita problemas de CORS ao acessar a API diretamente do navegador
"""

import http.server
import socketserver
import urllib.request
import urllib.parse
import json
import sys
from urllib.error import HTTPError, URLError

PORT = 8000

class ThingSpeakProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Se a requisição for para /api/thingspeak, fazer proxy
        if self.path.startswith('/api/thingspeak'):
            self.handle_thingspeak_proxy()
        else:
            # Servir arquivos estáticos normalmente
            super().do_GET()
    
    def handle_thingspeak_proxy(self):
        try:
            # Extrair parâmetros da URL
            parsed_url = urllib.parse.urlparse(self.path)
            query_params = urllib.parse.parse_qs(parsed_url.query)
            
            # Construir URL da API do ThingSpeak (remover /api/thingspeak do path)
            api_path = parsed_url.path.replace('/api/thingspeak', '')
            thingspeak_url = f"https://api.thingspeak.com{api_path}?{urllib.parse.urlencode(query_params, doseq=True)}"
            
            print(f"Fazendo proxy para: {thingspeak_url}")
            
            # Fazer requisição para a API do ThingSpeak
            with urllib.request.urlopen(thingspeak_url, timeout=10) as response:
                data = response.read()
                
                # Enviar resposta com headers CORS
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.end_headers()
                self.wfile.write(data)
                
        except HTTPError as e:
            self.send_error(e.code, f"Erro HTTP: {e.reason}")
        except URLError as e:
            self.send_error(500, f"Erro de URL: {e.reason}")
        except Exception as e:
            self.send_error(500, f"Erro interno: {str(e)}")

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), ThingSpeakProxyHandler) as httpd:
            print(f"Servidor rodando em http://localhost:{PORT}")
            print("Acesse: http://localhost:8000/dashboard.html")
            print("Pressione Ctrl+C para parar")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado.")
        sys.exit(0)
