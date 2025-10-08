# Sistema de Diagnóstico Inteligente – Tech Challenge (Fase 1) e (Fase 2)

Este projeto foi desenvolvido como parte do Tech Challenge – Fase 1 e Fase 2, com o objetivo de criar uma solução inicial de IA para suporte ao diagnóstico médico, utilizando Machine Learning e Modelos Otimizados via Algoritmos Genéticos (PyGAD).  
Na Fase 2, o projeto foi expandido com:
- Integração com LLM (GPT-4o-mini) para geração de explicações clínicas automáticas;
- API Flask servindo o modelo otimizado;
- Implantação em nuvem via Azure Container Apps.

---

## Objetivo

Desenvolver um sistema capaz de analisar automaticamente exames médicos (dados estruturados) e indicar se o diagnóstico é maligno ou benigno, oferecendo:
- Métricas clínicas interpretáveis (sensibilidade, especificidade, PPV, NPV, AUC);
- Explicações automáticas em linguagem natural voltadas a profissionais da saúde;
- Implantação escalável e reproduzível via Docker + Azure Container Apps (IaC).

---

## Dataset

- Fonte: `load_breast_cancer()` do Scikit-learn (Breast Cancer Wisconsin – Diagnostic).  
- Total: 569 amostras com 30 variáveis (features) numéricas.  
- Classes:
  - 0 → Benigno  
  - 1 → Maligno  
- Dataset amplamente validado e utilizado em benchmarks científicos.

---

## Estrutura do Projeto
diagnostico_cancer_ml/
│
├── diagnostico_cancer_ml/
│ ├── core.py # Fase 1 – Modelagem Clássica
│ └── core_v2.py # Fase 2 – Otimização + LLM
│ 
│
├── infra/
│ ├── containerapp.yaml # Configuração IaC (Azure)
│ └── log_analytics.json # Observabilidade
│
├── requirements.txt # Dependências do projeto
├── Dockerfile # Imagem base do container
├── docker-compose.yml # Execução local
├── README.md
├── setup.py
└── app.py # API Flask (implantada na Azure)

