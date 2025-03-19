# Stock Price Tracker

Este é um projeto simples que utiliza Selenium, Celery e Flask para realizar buscas automáticas do preço de ações no Google e salvá-las em um banco de dados SQLite.

## Tecnologias Utilizadas
- **Python**
- **Selenium** 
- **Celery** 
- **Flask**

## Funcionalidades
- Busca automática do preço de ações especificadas através do navegador Chrome.
- Salvamento dos preços encontrados no banco de dados SQLite.
- Exposição de uma API para requisições de consulta via Flask.
- Execução periódica de buscas através do Celery.
