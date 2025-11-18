import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configura a API Key do Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/api/generate-plan', methods=['POST'])
def generate_plan():
    try:
        data = request.get_json()
        user_context = data.get('userContext')
        sustainability_goal = data.get('sustainabilityGoal')

        if not user_context or not sustainability_goal:
            return jsonify({"error": "userContext and sustainabilityGoal are required"}), 400

        # Constrói o prompt para o Gemini
        prompt = f"""Atuando como um arquiteto de soluções de sustentabilidade e guia pessoal, sua missão é criar um \"Plano de Missão Ambiental\" desafiador e inspirador para {user_context} com o objetivo principal de {sustainability_goal}.

        Este plano deve ser composto por:
        1.  **Missão Principal:** Um resumo conciso do objetivo.
        2.  **Passos Acionáveis (5 a 7 passos):** Uma lista numerada de ações concretas e quantificáveis, se possível, que o usuário pode realizar. Cada passo deve ser uma \"tarefa\" a ser concluída.
            *   Sugira como cada passo pode ser acompanhado ou \"concluído\".
            *   Pense em ações que poderiam, no futuro, ser conectadas a dados de IoT ou comportamentos (IoB).
        3.  **Dicas para Superar Desafios:** Conselhos práticos para as dificuldades comuns associadas a esses passos no contexto brasileiro.
        4.  **Recursos e Ferramentas Úteis:** Sugestões de aplicativos, sites, tecnologias ou iniciativas locais (com exemplos no Brasil) que podem auxiliar na missão.
        5.  **Impacto Esperado:** Uma breve descrição do impacto positivo que a conclusão desta missão terá.
        6.  **Frase Motivacional:** Uma frase para inspirar o usuário a começar.

        Use uma linguagem encorajadora, clara e orientada a resultados, sem formatação Markdown de blocos de código."""

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
