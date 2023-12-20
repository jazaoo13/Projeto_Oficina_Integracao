import psycopg2
from psycopg2 import sql
from psycopg2.extensions import adapt

db_host = "localhost"
db_port = "5432"
db_name = "Site_Bebidas"
db_user = "postgres"
db_password = "postgres"

# Connect to the database
connection = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Read image data from a file
with open("C:/Users/Jazaoo/Desktop/Site_Bebidas/static/imagens/bebidas/bebida_vodka.jpeg", "rb") as image_file:
    image_data = image_file.read()

# Prepare the SQL query
insert_query = sql.SQL("UPDATE produtos SET imagem = %s WHERE id = 4;")

# Execute the query
with connection.cursor() as cursor:
    cursor.execute(insert_query, (psycopg2.Binary(image_data),))
    # new_id = cursor.fetchone()[0]  # No need for this line in an UPDATE query

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
