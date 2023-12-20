from flask import Flask, request, jsonify, after_this_request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app, support_credentials=True)
socketio = SocketIO(app)
clients = []

@app.route('/get_updates')
def get_updates():
    response_event = request.environ['socketio'].get('response_event')
    response = []

    # Add the client to the clients list
    clients.append({'response': response, 'event': response_event})

    # Wait for updates or a timeout
    response_event.wait(timeout=30)
    response_event.clear()  # Clear the event for the next request

    return jsonify(response)

@app.route('/update_database', methods=['POST'])
def update_database():
    data = request.json
    cod_barra = data.get('cod_barra')
    peso = data.get('peso')

    # Update your PostgreSQL database with cod_barra and peso

    # Broadcast the updated data to all clients
    for client in clients:
        client['response'].append({'data': 'Updated data'})
        client['event'].set()

    return jsonify({'status': 'success'})

@app.route('/test', methods=['GET'])
def yourMethod(params):
    response = Flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug= True)
