from flask import Flask, request, jsonify, after_this_request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
from psycopg2 import sql

db_host = "localhost"
db_port = "5432"
db_name = "Site_Bebidas"
db_user = "postgres"
db_password = "postgres"

def connect():
    try:
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )
        print("Connected to the database.")
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database\n{e}")
        return None

def get_produtos(connection):
    try:
        cursor = connection.cursor()
        select_query = '''
            SELECT cod_barra, litragem
            FROM produtos;
        '''
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            data.append({'cod_barra': row[0], 'litragem': row[1]})

        return data
    except Exception as e:
        print(f"Error: Unable to retrieve data\n{e}")
        return []

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
clients = []

@app.route('/get_produtos')
def get_produtos():
    response_event = request.environ['socketio'].get('response_event')
    response = []

    clients.append({'response': response, 'event': response_event})
    #Abre conexão Banco de dados
    connection = connect()
    #Pega lista de todos os produtos(cod_barra e litragem)
    data = get_produtos(connection)
    #Fecha conexão banco de dados
    connection.close()

    response.extend(data)
    response_event.wait(timeout=30)
    response_event.clear()

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

    socketio.emit('database_updated', {'data': 'Database updated', 'cod_barra': cod_barra, 'peso': peso})
    return jsonify({'status': 'success'})

@app.route('/test', methods=['GET'])
def teste():
    return "teste"

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, debug=True)
