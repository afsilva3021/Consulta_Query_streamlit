import streamlit as st
import pyodbc

server = 'host_server'
database = 'database'
username = 'user'
password = 'password'
driver = '{ODBC Driver 18 for SQL Server}'

connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=no;TrustServerCertificate=yes'

conn = pyodbc.connect(connectionString) 

st.header('Consulta PEDIDOS CROSSDOCKING')

with st.sidebar:
    data = st.text_input(label='Data', format='YYY/MM/D')
    hora = st.text_input(label='Inicio', value='08:00:00')
    consulta = st.button(label="Consultar")



sql_query = (f"""Query""")

cursor = conn.cursor()

if(consulta):
    st.dataframe(cursor.execute(sql_query))
    
    
    

