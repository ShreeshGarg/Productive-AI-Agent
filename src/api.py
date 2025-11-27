"""Flask REST API"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.agent import ProductivityAgent
import os
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

agent = None

def init_agent():
    global agent
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"[API] Loading agent with key: {api_key[:20] if api_key else 'NONE'}")
    agent = ProductivityAgent(api_key)
    if agent.model:
        print("[API] ✅ Agent model initialized successfully")
    else:
        print("[API] ⚠️ Agent model NOT initialized")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "agent": "operational"})

@app.route("/api/query", methods=["POST"])
def query():
    try:
        data = request.get_json()
        user_input = data.get("query", "")
        if not user_input:
            return jsonify({"error": "Query required"}), 400
        response = agent.process_user_input(user_input)
        return jsonify({"status": "success", "query": user_input, "response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/status", methods=["GET"])
def get_status():
    return jsonify(agent.get_agent_status())

@app.route("/api/memory", methods=["GET"])
def get_memory():
    return jsonify({"memory": agent.memory.get_memory_summary()})

@app.route("/api/session", methods=["GET"])
def get_session():
    return jsonify(agent.export_session())

if __name__ == "__main__":
    init_agent()
    app.run(host="0.0.0.0", port=5000, debug=False)
