from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Set the URL of your Rasa server
RASA_SERVER_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route('/')
def index():
    return render_template('index combined.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form['message']
    # Send the message to the Rasa server
    response = requests.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message})
    bot_response = response.json()
    return jsonify(bot_response)

if __name__ == '__main__':
    app.run(debug=True)
