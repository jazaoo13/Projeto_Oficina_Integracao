import psycopg2
from flask import Flask, request, jsonify, after_this_request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
from psycopg2 import sql

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
socketio.init_app(app, cors_allowed_origins="*")
clients = []

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

def get_table_produtos(connection):
    try:
        cursor = connection.cursor()
        select_query = '''
            SELECT id, litragem
            FROM produtos;
        '''
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            data.append({'indice': row[0], 'litragem': row[1]})

        return data
    except Exception as e:
        print(f"Error: Unable to retrieve data\n{e}")
        return []

def update_produto(cod_barra, peso):
    try:
        connection = connect()
        cursor = connection.cursor()

        # Assuming your database has a table named 'produtos' with 'cod_barra' as a unique identifier
        update_query = '''
            UPDATE produtos
            SET peso = %s
            WHERE cod_barra = %s;
        '''

        cursor.execute(update_query, (peso, cod_barra))
        connection.commit()

        updated_data = get_table_produtos(connection)

        connection.close()
        return updated_data

    except Exception as e:
        print(f"Error updating produto: {str(e)}")
        return None


@app.route('/get_produtos')
def get_produtos():
    try:
        print("1. Entrou em get_produtos")

        response_event = socketio.start_background_task(target=background_task)

        response = []

        print("2. Conectando ao banco de dados")
        connection = connect()
        if not connection:
            print("Erro: Não foi possível conectar ao banco de dados")
            return jsonify({'error': 'Unable to connect to the database'}), 500

        print("3. Obtendo dados da tabela produtos")
        data = get_table_produtos(connection)

        print("Dados obtidos:", data)

        print("4. Fechando conexão com o banco de dados")
        connection.close()

        print("5. Emitindo evento 'response'")
        response.extend(data)
        socketio.emit('response', {'data': data})

        print("6. Retornando resposta ao cliente")
        return jsonify(data)
    except Exception as e:
        print(f"Erro em get_produtos: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

def background_task():
    socketio.sleep(1)
    socketio.emit('background_task_response', {'data': 'Task completed'})

@app.route('/update_database', methods=['POST'])
def update_database():
    try:
        data = request.json
        cod_barra = data.get('cod_barra')
        peso = data.get('peso')

        updated_data = update_produto(cod_barra, peso)

        if updated_data is not None:
            # Broadcast the updated data to all clients
            for client in clients:
                client['response'].append({'data': 'Updated data'})
                client['event'].set()

            socketio.emit('database_updated', {'data': 'Database updated', 'cod_barra': cod_barra, 'peso': peso})
            return jsonify({'status': 'success', 'data': updated_data})
        else:
            return jsonify({'status': 'error', 'message': 'Failed to update the database'}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

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
