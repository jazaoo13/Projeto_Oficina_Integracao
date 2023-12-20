from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app, resources={r"/socket.io/*": {"origins": "http://192.168.3.8:8080/"}})
socketio = SocketIO(app, transports=['websocket', 'polling'])
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

@app.route('/test')
def test_route():
    return jsonify({'message': 'Test route works!'})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True)
