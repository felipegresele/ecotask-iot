import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configura a API Key do Gemini
# É recomendado carregar a chave de uma variável de ambiente em produção
# Mas para simplicidade, usaremos a chave diretamente aqui, como solicitado.
genai.configure(api_key="AIzaSyDR5DlOeySR6FIoz37hi6H4AFg3IjsMzzw")

@app.route('/api/generate-plan', methods=['POST'])
def generate_plan():
    try:
        data = request.get_json()
        user_context = data.get('userContext')
        sustainability_goal = data.get('sustainabilityGoal')

        if not user_context or not sustainability_goal:
            return jsonify({"error": "userContext and sustainabilityGoal are required"}), 400

        # Constrói o prompt para o Gemini
        prompt = f"""Atuando como um consultor de sustentabilidade experiente, crie um plano de ação detalhado e prático para {user_context} com o objetivo de {sustainability_goal}.
Inclua pelo menos 5 passos acionáveis, dicas sobre como superar desafios comuns, recursos úteis (ex: tipos de lixo, pontos de coleta comuns no Brasil) e uma breve seção sobre o impacto positivo dessas ações.
Use linguagem encorajadora e fácil de entender.
Formate a resposta como um texto contínuo, sem formatação Markdown de blocos de código."""

        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)

        # Acessa o texto da resposta
        generated_plan = response.text

        return jsonify({"plan": generated_plan})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Para rodar em ambiente de desenvolvimento
    app.run(host='0.0.0.0', port=5000)
