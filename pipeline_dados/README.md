## 🏥 Fusão de Dados Clínicos — Sanare + Reviver
Este projeto faz parte do curso "Pipeline de Dados" da Alura. O objetivo é estruturar um ambiente seguro, reprodutível e eficiente para unificar os dados de duas clínicas médicas em processo de fusão: Clínica Sanare e Clínica Reviver.

O projeto é conduzido em ambiente Linux (Ubuntu via WSL) e utiliza Python e Jupyter Notebook como ferramentas principais de análise.

## 📁 Estrutura do Projeto
```
pipeline_dados/
├── data_raw/ # Dados brutos originais
│ ├── dados_empresaA.json
│ └── dados_empresaB.csv
├── notebooks/ # Análises e transformações (Jupyter)
├── scripts/ # Scripts Python reutilizáveis
├── .venv/ # Ambiente virtual Python
└── README.md # Este arquivo
```

## 1. Configuração do Ambiente (via WSL - Ubuntu)
Abra o terminal WSL e execute os passos abaixo:
Criação da estrutura inicial:
mkdir -p ~/pipeline_dados/{data_raw,notebooks,scripts}
cd ~/pipeline_dados
Download dos arquivos de dados:
cd data_raw
wget https://cdn3.gnarususercontent.com.br/3062-pipeline-dados/dados/dados_empresaA.json
wget https://cdn3.gnarususercontent.com.br/3062-pipeline-dados/dados/dados_empresaB.csv

## 2. Criar o Ambiente Virtual Python
cd ~/projetos/pipeline-clinicas
python3 -m venv .venv
source .venv/bin/activate

## 3. Instalar Jupyter Notebook (com versionamento)
pip install notebook==7.0.3
jupyter notebook

## 🤝 Contribuindo
Este projeto é educativo e visa o aprendizado de boas práticas em engenharia de dados, como:
- Organização de pastas
- Ambientes reprodutíveis
- Processamento de dados de diferentes fontes
- Documentação clara e compartilhável