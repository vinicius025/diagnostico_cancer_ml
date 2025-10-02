# Sistema de Diagnóstico Inteligente – Tech Challenge (Fase 1) e (Fase 2)
Este projeto foi desenvolvido como parte do **Tech Challenge – Fase 1** e **Tech Challenge – Fase 2**, com o objetivo de criar uma solução inicial de **IA para suporte ao diagnóstico médico**, utilizando **Machine Learning** para análise de exames e classificação de doenças. Outro ponto que vou abordar é sobre a otimização de hiperparâmetros com Algoritmos Genéticos (PyGAD) e explicação em linguagem natural com LLM.

---

## Objetivo
Desenvolver um sistema capaz de analisar automaticamente exames médicos (dados estruturados) e indicar se o diagnóstico é **maligno** ou **benigno**, oferecendo métricas claras e interpretabilidade para apoiar profissionais de saúde e também a otimização de hiperparâmetros com Algoritmos Genéticos (PyGAD) e explicação em linguagem natural com LLM.

---

## Dataset
- Utilizamos o dataset **`load_breast_cancer()`** do Scikit-learn que é a versão pré-processada do Breast Cancer Wisconsin (Diagnostic), o mesmo disponível no Kaggle e no UCI Machine Learning Repository, já limpo e pronto para uso em modelos de Machine Learning.  
- **569 amostras** com 30 variáveis (features) que descrevem características dos tumores.  
- Classes:
  - `0` Benigno
  - `1` Maligno  

Dataset limpo, amplamente utilizado em pesquisas de ML, ideal para prototipagem.

---

## Estrutura do Projeto

```
Diagnostico_cancer_ml/
│
├── diagnostico_cancer_ml/     # Pacote principal do projeto
│   ├── __init__.py
│   └── core.py         # Código Tech Challenge - Fase 1 (funções e classes do pacote)
│   └── core_v2.py      # Código Tech Challenge - Fase 2 (Otimização e uso de LLM)
│
├── Dockefile
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do projeto
└── setup.py            # Configuração para empacotamento do pacote
```

---

## Tecnologias Utilizadas
- **Python 3.11+**
- **Jupyter Notebook**
- **Pandas** – Manipulação de dados
- **Matplotlib** & **Seaborn** – Visualizações
- **Scikit-learn** – Modelagem de Machine Learning
- **Pytest** – Testes automatizados
- **jupyter**
- **openai** - (GPT)
- **transformers**
- **numpy**
- **pygad** - (Algoritmos Genéticos)
---

## Fluxo do Projeto -- Fase 1

**Exploração de Dados**  
- Carregamento do dataset.  
- Estatísticas descritivas, heatmap de correlação e análises gráficas.

**Pré-processamento**  
- Padronização dos dados com `StandardScaler`.  
- Redução de dimensionalidade com PCA (por exemplo, para manter 95% da variância)
- Seleção das 10 features mais relevantes (análise de correlação + feature importance).

**Modelagem**  
- Treinamento de 3 algoritmos:
  - **Regressão Logística** (baseline)
  - **Random Forest**
  - **SVM (kernel Linear)**

**Avaliação**  
- Métricas: Accuracy, Precision, Recall, F1-score.  
- **Curva ROC e AUC**.  
- **Cross-validation (10 folds)** para validar consistência dos resultados.

---
## Fluxo do Projeto -- Fase 2

**Baseline**  
- RandomForest sem ajuste de hiperparâmetros.

**Otimização com Algoritmo Genético (PyGAD)**  
- Função fitness: F1 médio em validação cruzada (5 folds).
- Espaço de busca: número de árvores, profundidade máxima e min_samples_split.
- 3 experimentos diferentes de GA (alterando população, gerações e taxa de mutação).

**Comparação de Resultados**
- Tabela consolidando baseline e experimentos.
- Gráficos de barras e linha mostrando a evolução do F1-score.

**Comparação de Resultados**
- Explicação automática dos resultados em linguagem natural.
- Voltada para médicos: destaca impacto prático em diagnósticos, decisões clínicas e segurança do paciente.

---
## Resultados - Fase 1

**Com todas as features:**
- **Regressão Logística:** 98.0% ± 1.5%  
- **Random Forest:** 96.0% ± 2.8%  
- **SVM:** 97.0% ± 1.5%

**Com apenas 10 features mais relevantes:**
- **Regressão Logística:** 95.5% ± 2.5%  
- **Random Forest:** 94.7% ± 2.9%  
- **SVM:** 95.0% ± 2.5%

**Utilizando o metódo PCA**
- **Logística (PCA):** 0.980 ± 0.025
- **Random Forest (PCA):** 0.932 ± 0.042
- **SVC (PCA):** 0.972 ± 0.021

---
## Resultados - Fase 2

**Configuração	F1 médio (CV=5)**
- **Baseline (RandomForest default)**	0.9652
- **GA - Exp1 (pop=16, gen=12, mut=0.15)**	0.9709
- **GA - Exp2 (pop=20, gen=20, mut=0.20)**	0.9749
- **GA - Exp3 (pop=10, gen=10, mut=0.10)**	0.9736


## Resumo interpretativo dos resultados
A comparação dos modelos de classificação por meio da validação cruzada (10-fold) evidenciou que a Regressão Logística apresentou desempenho consistente e elevado em todas as estratégias avaliadas (todas as features, 10 mais correlacionadas e PCA), alcançando até 98% de acurácia média com baixo desvio padrão. Isso indica uma forte capacidade do modelo em generalizar bem para novos dados.

O Random Forest, embora também tenha apresentado bom desempenho geral, foi o modelo que mais variou entre as estratégias, especialmente quando submetido à redução de dimensionalidade via PCA, o que pode indicar sensibilidade à forma como as variáveis foram transformadas.

Já o SVC (Support Vector Classifier) manteve desempenho estável e competitivo nas três abordagens, com destaque para a versão com PCA, que alcançou 97,2% de acurácia média, superando ligeiramente o desempenho da versão com todas as variáveis.

De forma geral, os resultados demonstram que, embora a seleção de features e o uso do PCA possam oferecer vantagens específicas, modelos simples como a regressão logística continuam sendo altamente eficazes para o conjunto de dados avaliado, especialmente quando se busca estabilidade e previsibilidade nos resultados.

---

## Como Executar - Fase 1

### Clone o repositório:
```bash
git clone https://github.com/vinicius025/diagnostico_cancer_ml.git
cd diagnostico_cancer_ml
```

### Crie e ative o ambiente virtual:
```bash
python -m venv env
env\Scripts\activate # Windows
```

```bash
python -m venv env
env\Scripts\activate # Git Bash (Windows)
```

```bash
python3 -m venv env
source env/bin/activate # Mac
```

### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Rode o notebook:
Verifique se o Jupyter está instalado. Se não estiver:
```bash
pip install diagnostico_cancer_ml
```

Em seguida, rode:
```bash
jupyter diagnostico_cancer_ml diagnostico_cancer_ml/core.ipynb
```

### Execute os testes:
Forma recomendada (compatível com qualquer shell):
```bash
env/Scripts/python.exe -m pytest tests/
```

Alternativa (se pytest estiver no PATH):
```bash
pytest tests/
```

### Como rodar o projeto em Docker

```bash
docker build -t diagnostico-medico .
docker run -p 8888:8888 diagnostico-medico
```

---
## Como Executar - Fase 2

### Clone o repositório:
```bash
git clone https://github.com/vinicius025/diagnostico_cancer_ml.git
cd diagnostico_cancer_ml
```
### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Rode o notebook:
Verifique se o Jupyter está instalado. Se não estiver:
```bash
pip install diagnostico_cancer_ml
```

Em seguida, rode:
```bash
jupyter diagnostico_cancer_ml diagnostico_cancer_ml/core_v2.ipynb
```

### (Opcional) Defina sua chave OpenAI em variável de ambiente para habilitar a explicação com LLM:
```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

## Aviso
Este projeto tem **fins acadêmicos**.  
Não deve ser utilizado como ferramenta clínica sem validação médica formal.

## Licenças

Este projeto utiliza o dataset **Breast Cancer Wisconsin (Diagnostic)**, disponível via `load_breast_cancer()` do Scikit-learn e também no [Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data).
O dataset está licenciado sob a **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

**Fonte oficial:** [Kaggle - Breast Cancer Wisconsin (Diagnostic)](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) 

## Link do video de explicação
**Vídeo de demonstração:** [Clique aqui para assistir](https://youtu.be/5UroJKtpQP8)

