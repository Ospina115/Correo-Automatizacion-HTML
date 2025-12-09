import os
import oracledb
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():
    """
    Establece y retorna una conexión a la base de datos Oracle.
    
    Returns:
        oracledb.Connection: Objeto de conexión a Oracle
        
    Raises:
        Exception: Si no se puede establecer la conexión
    """
    try:
        # Obtener credenciales desde variables de entorno
        user = os.getenv("ORACLE_USER")
        password = os.getenv("ORACLE_PASSWORD")
        host = os.getenv("ORACLE_HOST")
        port = os.getenv("ORACLE_PORT", "1521")  # Puerto por defecto
        sid = os.getenv("ORACLE_SID")
        
        # Validar que existan las credenciales
        if not all([user, password, host, sid]):
            raise ValueError("Faltan credenciales de Oracle en el archivo .env")
        
        # Construir DSN (Data Source Name)
        dsn = oracledb.makedsn(host, port, sid=sid)
        
        # Establecer conexión
        connection = oracledb.connect(
            user=user,
            password=password,
            dsn=dsn
        )
        
        print("✓ Conexión exitosa a Oracle Database")
        return connection
        
    except oracledb.Error as e:
        error, = e.args
        print(f"✗ Error de Oracle: {error.message}")
        raise
    except Exception as e:
        print(f"✗ Error al conectar a la base de datos: {str(e)}")
        raise


def obtener_empresas_semana_anterior():
    """
    Obtiene las empresas matriculadas en la semana anterior.
    
    Returns:
        list: Lista de diccionarios con la información de cada empresa.
            Cada diccionario contiene: nombre_empresa, num_matricula, correo

    Raises:
        Exception: Si hay error en la consulta
    """
    connection = None
    cursor = None
    
    try:
        # Establecer conexión
        connection = obtener_conexion()
        cursor = connection.cursor()
        
        # Ejecutar consulta
        query = """
            SELECT MATRICULA, RAZON_SOCIAL, NIT, CORREO, FECHA_MATRICULA, MAIL_ENVIA, MAIL_CONFIRMA 
            FROM sismemp.V_BI_COMPITE360
            WHERE TO_CHAR(FECHA_MATRICULA,'IYYYIW') = TO_CHAR(SYSDATE,'IYYYIW') - 1
        """
        
        print("\nEjecutando consulta...")
        cursor.execute(query)
        
        # Obtener nombres de columnas
        column_names = [desc[0] for desc in cursor.description]
        
        # Obtener resultados
        rows = cursor.fetchall()
        
        print(f"✓ Se encontraron {len(rows)} empresa(s) matriculada(s) la semana anterior\n")
        
        # Convertir resultados a lista de diccionarios
        empresas = []
        for row in rows:
            empresa = dict(zip(column_names, row))
            empresas.append(empresa)
        
        return empresas
        
    except oracledb.Error as e:
        error, = e.args
        print(f"✗ Error en la consulta Oracle: {error.message}")
        raise
    except Exception as e:
        print(f"✗ Error al obtener empresas: {str(e)}")
        raise
    finally:
        # Cerrar cursor y conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("✓ Conexión cerrada\n")


def obtener_empresas_todas():
    """
    Obtiene todas las empresas de la vista V_BI_COMPITE360.
    Útil para pruebas o consultas generales.
    
    Returns:
        list: Lista de diccionarios con la información de cada empresa
    """
    connection = None
    cursor = None
    
    try:
        connection = obtener_conexion()
        cursor = connection.cursor()
        
        query = "SELECT * FROM sismemp.V_BI_COMPITE360"
        
        print("\nEjecutando consulta de todas las empresas...")
        cursor.execute(query)
        
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        
        print(f"✓ Se encontraron {len(rows)} empresa(s) en total\n")
        
        empresas = []
        for row in rows:
            empresa = dict(zip(column_names, row))
            empresas.append(empresa)
        
        return empresas
        
    except oracledb.Error as e:
        error, = e.args
        print(f"✗ Error en la consulta Oracle: {error.message}")
        raise
    except Exception as e:
        print(f"✗ Error al obtener empresas: {str(e)}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("✓ Conexión cerrada\n")
