import os
import requests
import urllib3 # Para evitar advertencias de SSL
from API.ObtenerToken import obtener_token
from HTML.Base64Converter import convertir_html_a_base64
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()


def enviar_correo(destinatarios, asunto, html_path, nombre_empresa, num_matricula):
    """
    Envía un correo usando la API de notificaciones.
    
    Args:
        destinatarios (str o list): Email(s) del destinatario. Puede ser un string con emails 
                                    separados por comas o una lista de emails
        asunto (str): Asunto del correo
        html_path (str): Ruta al archivo HTML que será el cuerpo del correo
        nombre_empresa (str): Nombre de la empresa para personalizar el correo
        num_matricula (str): Número de matrícula para el link de confirmación
        producto_cobro (str): Código del producto de cobro (default: "GC-C360")
        
    Returns:
        dict: Respuesta de la API
    """
    try:
        # Obtener el token de autenticación
        token = obtener_token()
        
        # Convertir HTML a base64 con reemplazo de nombre y link
        body_base64 = convertir_html_a_base64(html_path, nombre_empresa, num_matricula)
        
        # Si destinatarios es una lista, convertir a string separado por comas
        if isinstance(destinatarios, list):
            destinatarios = ", ".join(destinatarios)
        
        # Si hay un email de copia en las variables de entorno, agregarlo
        email_copia = os.getenv("FSEND_EMAIL_COPIA")
        if email_copia:
            destinatarios = f"{destinatarios};{email_copia}"
        
        # Preparar la solicitud
        url = os.getenv("API_FSEND_CORREO")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        
        payload = {
            "producto_cobro": os.getenv("FSEND_PRODUCTO_COBRO"),
            "email": destinatarios,
            "asunto": asunto,
            "body_base64": body_base64
        }
        
        # Enviar la solicitud
        response = requests.post(
            url, 
            json=payload, 
            headers=headers,
            verify=False
        )
        
        # Obtener el JSON de respuesta
        response_data = response.json()
        
        # Validar respuesta exitosa (status 200 y código 200)
        if response.status_code == 200 and response_data.get("codigo") == 200:
            mensaje = response_data.get("respuesta", {}).get("mensaje", "Sin mensaje")
            return {
                "exito": True,
                "status_code": response.status_code,
                "mensaje": mensaje,
                "respuesta_completa": response_data
            }
        
        # Validar respuesta con error 500 (Internal Server Error)
        elif response.status_code == 500:
            error_msg = response_data.get("error", "Internal Server Error")
            timestamp = response_data.get("timestamp", "N/A")
            path = response_data.get("path", "N/A")
            
            print(f"✗ Error 500 - Posible problema de autenticación o error del servidor")
            print(f"  • Timestamp: {timestamp}")
            print(f"  • Path: {path}")
            print(f"  • Error: {error_msg}")
            
            return {
                "exito": False,
                "status_code": response.status_code,
                "error": error_msg,
                "tipo_error": "autenticacion_o_servidor",
                "timestamp": timestamp,
                "respuesta_completa": response_data
            }
        
        # Otros códigos de error
        else:
            print(f"✗ Respuesta inesperada del servidor (Status: {response.status_code})")
            print(f"  Respuesta: {response_data}")
            
            return {
                "exito": False,
                "status_code": response.status_code,
                "error": "Respuesta inesperada del servidor",
                "respuesta_completa": response_data
            }
        
    except requests.exceptions.ConnectionError as e:
        error_msg = f"Error de conexión con el servidor: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "conexion"
        }
    
    except requests.exceptions.Timeout as e:
        error_msg = f"Timeout en la solicitud: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "timeout"
        }
    
    except requests.exceptions.RequestException as e:
        error_msg = f"Error en la solicitud HTTP: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "http"
        }
    
    except Exception as e:
        error_msg = f"Error inesperado al enviar correo: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "exito": False,
            "error": error_msg,
            "tipo_error": "desconocido"
        }

