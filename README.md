# Sistema de Diagnóstico Inteligente – Tech Challenge (Fase 1)
Este projeto foi desenvolvido como parte do **Tech Challenge – Fase 1**, com o objetivo de criar uma solução inicial de **IA para suporte ao diagnóstico médico**, utilizando **Machine Learning** para análise de exames e classificação de doenças.

---

## Objetivo
Desenvolver um sistema capaz de analisar automaticamente exames médicos (dados estruturados) e indicar se o diagnóstico é **maligno** ou **benigno**, oferecendo métricas claras e interpretabilidade para apoiar profissionais de saúde.

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
│   └── core.py         # Código principal (funções e classes do pacote)
│
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

---

## Fluxo do Projeto

**Exploração de Dados**  
- Carregamento do dataset.  
- Estatísticas descritivas, heatmap de correlação e análises gráficas.

**Pré-processamento**  
- Padronização dos dados com `StandardScaler`.  
- Seleção das 10 features mais relevantes (análise de correlação + feature importance).

**Modelagem**  
- Treinamento de 3 algoritmos:
  - **Regressão Logística** (baseline)
  - **Random Forest**
  - **SVM (kernel RBF)**

**Avaliação**  
- Métricas: Accuracy, Precision, Recall, F1-score.  
- **Curva ROC e AUC**.  
- **Cross-validation (10 folds)** para validar consistência dos resultados.

---

## Resultados

**Com todas as features:**
- **Regressão Logística:** 98.0% ± 1.5%  
- **Random Forest:** 96.0% ± 2.8%  
- **SVM:** 97.7% ± 1.8%

**Com apenas 10 features mais relevantes:**
- **Regressão Logística:** 95.5% ± 2.5%  
- **Random Forest:** 95.0% ± 3.0%  
- **SVM:** 94.7% ± 2.7%

## Resumo interpretativo dos resultados
O modelo de Regressão Logística apresentou a melhor performance geral (98%), enquanto Random Forest e SVM também obtiveram resultados robustos. A seleção de features reduziu a dimensionalidade sem comprometer significativamente a performance, mostrando que é possível simplificar o modelo mantendo alta acurácia.

---

## Como Executar

### Clone o repositório:
```bash
git clone https://github.com/vinicius025/diagnostico_cancer_ml.git
cd diagnostico_cancer_ml
```

### Crie e ative o ambiente virtual:
```bash
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate    # Windows
```

### Instale as dependências:
```bash
pip install -r requirements.txt
```

### Rode o notebook:
```bash
jupyter notebook notebooks/core.ipynb
```

### Execute os testes:
```bash
pytest tests/
```

---

## Aviso
Este projeto tem **fins acadêmicos**.  
Não deve ser utilizado como ferramenta clínica sem validação médica formal.

## Licenças

Este projeto utiliza o dataset **Breast Cancer Wisconsin (Diagnostic)**, disponível via `load_breast_cancer()` do Scikit-learn e também no [Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data).
O dataset está licenciado sob a **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

**Fonte oficial:** [Kaggle - Breast Cancer Wisconsin (Diagnostic)](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/data) 

## Link do video de explicação

**Vídeo de demonstração:** [Clique aqui para assistir](LINK_DO_VIDEO)