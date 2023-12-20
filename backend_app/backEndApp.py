import psycopg2
from flask import Flask, request, jsonify, after_this_request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO
from psycopg2 import sql
from io import BytesIO
from PIL import Image
import base64
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
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
            SELECT id,nome, litragem, imagem
            FROM produtos;
        '''
        cursor.execute(select_query)
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            image_data = row[3]
            image_base64 = None
            if image_data:
                image_base64 = base64.b64encode(image_data).decode('utf-8')

            data.append({
                'indice': row[0],
                'nome': row[1],
                'litragem': row[2],
                'image': image_base64
            })

        return data
    except Exception as e:
        print(f"Error: Unable to retrieve data\n{e}")
        return []

def get_tara_and_densidade(cod_barra):
    try:
        connection = connect()
        cursor = connection.cursor()

        select_query = '''
            SELECT tara_garrafa, densidadeliquido
            FROM produtos
            WHERE cod_barra = %s;
        '''

        cursor.execute(select_query, (cod_barra,))
        result = cursor.fetchone()

        connection.close()

        return result  # Returns a tuple (tara_garrafa, densidadeliquido)

    except Exception as e:
        print(f"Error getting tara and densidade: {str(e)}")
        return None

def update_produto(cod_barra, peso):
    try:
        connection = connect()
        cursor = connection.cursor()

        # Get tara_garrafa and densidadeliquido for the given cod_barra
        tara_garrafa, densidadeliquido = get_tara_and_densidade(cod_barra)
        
        if tara_garrafa is not None and densidadeliquido is not None:
            # Remove tara_garrafa from peso and multiply by densidadeliquido
            peso_ajustado = (peso - tara_garrafa) * densidadeliquido
            # Update the litragem in the database
            update_query = '''
                UPDATE produtos
                SET litragem =  %s
                WHERE cod_barra = %s;
            '''

            cursor.execute(update_query, (peso_ajustado, cod_barra))
            connection.commit()
            updated_data = get_table_produtos(connection)

            connection.close()
            return updated_data

        else:
            print(f"Unable to get tara_garrafa or densidadeliquido for cod_barra: {cod_barra}")
            return None

    except Exception as e:
        print(f"Erro ao atualizar produto: {str(e)}")
        return None


@app.route('/get_produtos')
def get_produtos():
    try:
        response = []
        connection = connect()
        if not connection:
            return jsonify({'error': 'Unable to connect to the database'}), 500

        data = get_table_produtos(connection)

        connection.close()

        response.extend(data)
        socketio.emit('response', {'data': data})

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/update_database', methods=['POST'])
def update_database():
    try:
        data = request.get_data(as_text=True)
        print("DADO RECEBIDO: ",data)
        cleaned_data = ''.join([char if ord(char) > 31 or ord(char) == 9 else ' ' for char in data])
        json_data = json.loads(cleaned_data)
        cod_barra = json_data.get("cod_barra", "")
        peso = json_data.get("peso")
        if cod_barra != '':
            updated_data = update_produto(int(cod_barra), float(peso))
            if updated_data is not None:
                socketio.emit('database_updated', {'data': 'Database updated', 'cod_barra': cod_barra, 'peso': peso})
                return jsonify({'status': 'success', 'data': updated_data})
            else:
                return jsonify({'status': 'error', 'message': 'Falha ao atualizar banco'}), 501
        else:
            return jsonify({'status': 'error', 'message': 'Código de Barra vazio'}), 503
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
