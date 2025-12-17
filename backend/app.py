from flask import Flask, request, jsonify
from flask_cors import CORS

from knowledge_base import knowledge_base
from diagram_engine import get_diagram
from keyword_mapper import normalize_topic

app = Flask(__name__)
CORS(app)

@app.route("/explain", methods=["POST"])
def explain():
    data = request.get_json()

    raw_text = data.get("text", "")
    level = data.get("level", "beginner").lower()

    topic = normalize_topic(raw_text)

    if topic in knowledge_base and level in knowledge_base[topic]:
        response = knowledge_base[topic][level].copy()
        response["diagram"] = get_diagram(topic, level)
    else:
        response = {
            "definition": "No explanation available.",
            "analogy": "",
            "engineering_example": "",
            "diagram": ""
        }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
