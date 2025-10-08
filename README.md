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


---

## Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| Linguagem | Python 3.11 |
| Bibliotecas ML | Scikit-learn, PyGAD, NumPy, Pandas |
| Visualização | Matplotlib, Seaborn |
| Integração LLM | OpenAI API (GPT-4o-mini) |
| Implantação | Docker, Azure Container Apps |
| Outras | Flask, pytest, jupyter, transformers |

---

## Fluxo do Projeto — Fase 1

1. Exploração de Dados  
   - Carregamento do dataset e análise exploratória (EDA).  
   - Correlação, visualização e estatísticas descritivas.

2. Pré-processamento  
   - Normalização com StandardScaler.  
   - Redução de dimensionalidade com PCA (95% da variância).  
   - Seleção das 10 variáveis mais relevantes.

3. Modelagem  
   - Regressão Logística, Random Forest, SVM (Linear).

4. Avaliação  
   - Accuracy, Precision, Recall, F1-score, AUC.  
   - Validação cruzada (10-fold).  

---

## Fluxo do Projeto — Fase 2

1. Baseline  
   - RandomForest padrão com F1 médio = 0.9694.

2. Otimização com Algoritmo Genético (PyGAD)  
   - Função fitness: F1 médio (CV=5).  
   - Espaço de busca: n_estimators, max_depth, min_samples_split.  
   - Três experimentos variando população, gerações e mutação.

3. Integração com LLM  
   - Geração de explicações automáticas via GPT-4o-mini, com seções:
     - Resumo técnico (explica hiperparâmetros e performance)
     - Interpretação clínica (impacto na decisão médica e segurança do paciente)

4. Deploy Flask + Azure  
   - API servindo o modelo otimizado (/predict, /health).  
   - Container publicado no Docker Hub e Azure Container Apps.

---

## Resultados — Fase 1

| Modelo | Acurácia (± DP) |
|---------|-----------------|
| Regressão Logística | 98.0% ± 1.5% |
| Random Forest | 96.0% ± 2.8% |
| SVM | 97.0% ± 1.5% |

**Com PCA**

| Modelo | Acurácia |
|---------|-----------|
| Logística (PCA) | 0.980 |
| Random Forest (PCA) | 0.932 |
| SVC (PCA) | 0.972 |

---

## Resultados — Fase 2 (Otimização Genética)

| Configuração | F1 médio (CV=5) |
|---------------|-----------------|
| Baseline (RandomForest default) | 0.9694 |
| GA – Exp1 (pop=16, gen=12, mut=0.15) | 0.9723 |
| GA – Exp2 (pop=20, gen=20, mut=0.20) | 0.9723 |
| GA – Exp3 (pop=10, gen=10, mut=0.10) | 0.9723 |

---

## Explicação Clínica (via GPT-4o-mini)

O modelo otimizado apresentou melhora de F1-score de 0.9694 → 0.9723, indicando maior equilíbrio entre sensibilidade e precisão.  
Clinicamente, isso significa menos diagnósticos incorretos, melhor detecção de casos malignos e redução de falsos positivos — aumentando a segurança e a confiança na decisão médica.

---

## Implementação em Nuvem (IaC – Azure Container Apps)

A implantação foi automatizada com Infraestrutura como Código (IaC):

| Arquivo | Função |
|----------|--------|
| infra/containerapp.yaml | Define ambiente, CPU, memória, portas e segredos (OPENAI_API_KEY). |
| infra/docker-compose.yml | Executa e valida o container localmente antes do deploy. |
| infra/log_analytics.json | Envia logs e métricas de uso ao Log Analytics. |

**Deploy automatizado:**
```bash
az containerapp update \
  --name diagnostico-ml-app \
  --resource-group ml-diagnostico \
  --image aragao025/diagnostico_cancer_ml:latest \
  --revision-suffix vfinal \
  --set-env-vars FLASK_RUN_PORT=5000 OPENAI_API_KEY=<sua_chave>
```

---

**Endpoint público:**

https://diagnostico-ml-app.gentlefield-cbfa53dc.eastus.azurecontainerapps.io

Como Executar (Local)

1. Clonar o repositório
```bash
git clone https://github.com/vinicius025/diagnostico_cancer_ml.git
cd diagnostico_cancer_ml
```

2. Instalar dependências
```bash
pip install -r requirements.txt
```

3. Rodar a API Flask localmente
```bash
python diagnostico_cancer_ml/app.py
```
Acesse em: http://127.0.0.1:5000/health

4. Executar via Docker
```bash
docker build -t diagnostico_cancer_ml .
docker run -p 5000:5000 diagnostico_cancer_ml
```

---

**Variáveis de Ambiente**
```bash
export OPENAI_API_KEY="sua_chave_aqui"
export MODEL_PATH="/app/models/randomforest_optimized.pkl"
```

**Aviso**

Este projeto tem fins acadêmicos.
Não deve ser utilizado como ferramenta clínica sem validação médica formal.

---

**Licenças**

O dataset Breast Cancer Wisconsin (Diagnostic) está disponível via load_breast_cancer() (Scikit-learn) e no Kaggle.
Licença: Creative Commons Attribution 4.0 International (CC BY 4.0).

---

**Link do Vídeo de Demonstração**

Vídeo de demonstração part 1: https://youtu.be/5UroJKtpQP8
Vídeo de demonstração part 2: 