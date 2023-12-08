from flask import Flask, render_template, request
from rasa.core.agent import Agent

app = Flask(__name__)

# Load Rasa model
agent = Agent.load("D:\MobiChat\my_chatbot\models")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
async def get_response():
    user_message = request.form["user_message"]
    response = await agent.handle_text(user_message)
    return {"response": response[0]["text"]}

if __name__ == "__main__":
    app.run(debug=True)
