# Configura o Gunicorn para rodar na porta que o Azure App Service espera
bind = "0.0.0.0:8000"
workers = 2 # Número de workers Gunicorn. Ajuste conforme a necessidade.
timeout = 120 # Tempo limite para requisições