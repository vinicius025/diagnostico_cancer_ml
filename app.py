# app.py
import os
import joblib
import numpy as np
from flask import Flask, request, jsonify
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# ======================================
# Inicialização do Flask
# ======================================
app = Flask(__name__)

# ======================================
# Carregar modelo (ou criar um se não existir)
# ======================================
MODEL_PATH = os.getenv("MODEL_PATH", "models/randomforest_optimized.pkl")

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print(f"Modelo carregado de: {MODEL_PATH}")
else:
    print("Modelo não encontrado. Treinando um modelo padrão (fallback)...")
    X, y = load_breast_cancer(return_X_y=True)
    model = RandomForestClassifier(random_state=25)
    model.fit(X, y)
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Modelo padrão salvo em {MODEL_PATH}")

# ======================================
# Endpoint de saúde (teste de vida)
# ======================================
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "API de diagnóstico de câncer de mama ativa e operante.",
        "model_path": MODEL_PATH
    }), 200

# ======================================
# Endpoint de previsão
# ======================================
@app.route("/predict", methods=["POST"])
def predict():
    """
    Espera um JSON com formato:
    {
        "data": [
            [val1, val2, val3, ..., val30]
        ]
    }
    """
    try:
        body = request.get_json(force=True)
        data = body.get("data", None)

        if data is None:
            return jsonify({"error": "Campo 'data' ausente no JSON."}), 400

        # Converter para numpy array
        X_input = np.array(data)

        # Fazer previsão
        prediction = model.predict(X_input)
        proba = model.predict_proba(X_input)

        # Montar resposta
        resposta = {
            "prediction": prediction.tolist(),
            "probabilities": proba.tolist(),
            "interpretation": [
                "Maligno" if pred == 1 else "Benigno" for pred in prediction
            ]
        }

        return jsonify(resposta), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ======================================
# Inicialização da API
# ======================================
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
