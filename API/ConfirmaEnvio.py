import os
import requests
import urllib3
from dotenv import load_dotenv
from API.ObtenerToken import obtener_token

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()


def confirmar_envio_email(num_matricula, estado):
    """
    Confirma el envío de correo actualizando la base de datos.
    
    Args:
        num_matricula (str): Número de matrícula de la empresa
        estado (str): Estado del envío - "s" (enviado) o "n" (no enviado)
        
    Returns:
        dict: Resultado de la confirmación con éxito/error
    """
    try:
        # Validar estado
        if estado not in ["S", "N"]:
            raise ValueError("Estado debe ser 'S' (enviado) o 'N' (no enviado)")
        
        # Construir URL
        base_url = os.getenv("API_CONFIRMA_ENVIO_URL")
        if not base_url:
            raise ValueError("No se encontró API_CONFIRMA_ENVIO_URL en el archivo .env")
        
        url = f"{base_url}/{num_matricula}/{estado}"
        
        # Obtener token de autenticación
        token = obtener_token()
        
        headers = {
            "Authorization": f"Bearer {token}"
        }
        
        # Realizar petición GET
        response = requests.get(
            url,
            headers=headers,
            verify=False
        )
        
        # Obtener respuesta
        response_data = response.json() if response.text else {}
        
        # Validar respuesta exitosa
        if response.status_code == 200:
            return {
                "exito": True,
                "status_code": response.status_code,
                "mensaje": "Confirmación registrada exitosamente",
                "respuesta_completa": response_data
            }
        else:
            error_msg = response_data.get("error", f"Error {response.status_code}")
            print(f"✗ Error al confirmar envío: {error_msg}")
            
            return {
                "exito": False,
                "status_code": response.status_code,
                "error": error_msg,
                "respuesta_completa": response_data
            }
    
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Error de conexión: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "conexion"
        }
    
    except requests.exceptions.Timeout as e:
        error_msg = f"Timeout: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "timeout"
        }
    
    except Exception as e:
        error_msg = f"Error al confirmar envío: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "desconocido"
        }