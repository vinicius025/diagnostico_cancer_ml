import pytest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Função auxiliar para treinar e extrair importância das features
def treinar_rf_feature_importances():
    # Carrega os dados
    dados = load_breast_cancer()
    df = pd.DataFrame(dados.data, columns=dados.feature_names)
    df['diagnostico'] = dados.target

    X = df.drop(columns=['diagnostico'])
    y = df['diagnostico']

    # Divisão
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Padronização
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Treinar Random Forest
    model_rf = RandomForestClassifier(n_estimators=200, random_state=42)
    model_rf.fit(X_train_scaled, y_train)

    # Importância das features
    importancias = pd.Series(model_rf.feature_importances_, index=X.columns)
    return importancias.sort_values(ascending=False)

# Teste: verifica se uma das top features esperadas está no topo
def test_feature_importance_contains_expected():
    top_features = treinar_rf_feature_importances()

    # Verifica se 'worst concave points' está entre as top 10
    top_10 = top_features.head(10).index.tolist()
    assert 'worst concave points' in top_10, "'worst concave points' não está entre as top 10 features."
