import base64
import re
import os
from dotenv import load_dotenv

load_dotenv()


def convertir_caracteres_especiales_a_html(texto):
    """
    Convierte caracteres especiales en un texto a entidades HTML.
    
    Args:
        texto (str): Texto con posibles caracteres especiales
        
    Returns:
        str: Texto con entidades HTML
    """
    reemplazos = {
        'á': '&aacute;',
        'é': '&eacute;',
        'í': '&iacute;',
        'ó': '&oacute;',
        'ú': '&uacute;',
        'Á': '&Aacute;',
        'É': '&Eacute;',
        'Í': '&Iacute;',
        'Ó': '&Oacute;',
        'Ú': '&Uacute;',
        'ñ': '&ntilde;',
        'Ñ': '&Ntilde;',
        '¡': '&iexcl;',
        '¿': '&iquest;',
        'ü': '&uuml;',
        'Ü': '&Uuml;',
        '&': '&amp;',
    }
    
    texto_convertido = texto
    for caracter, entidad in reemplazos.items():
        texto_convertido = texto_convertido.replace(caracter, entidad)
    
    return texto_convertido


def convertir_html_a_base64(ruta_html, nombre_empresa, num_matricula):
    """
    Lee un archivo HTML y lo convierte a base64.
    Reemplaza {{COMPANY_NAME}} con el nombre de la empresa.
    Actualiza el link del botón de acción con el número de matrícula.
    
    Args:
        ruta_html (str): Ruta al archivo HTML
        nombre_empresa (str): Nombre de la empresa para reemplazar en el HTML
        num_matricula (str): Número de matrícula para el link de confirmación
        
    Returns:
        str: Contenido del HTML codificado en base64
    """
    try:
        with open(ruta_html, 'r', encoding='utf-8') as archivo:
            contenido_html = archivo.read()
        
        # Convertir caracteres especiales del nombre a entidades HTML
        nombre_empresa_convertido = convertir_caracteres_especiales_a_html(nombre_empresa)
        contenido_html = contenido_html.replace('{{COMPANY_NAME}}', nombre_empresa_convertido)
        
        # URL de confirmación desde variable de entorno
        api_confirma_base = os.getenv("API_CONFIRMA_WHATS")
        if not api_confirma_base:
            raise ValueError("No se encontró la variable API_CONFIRMA_WHATS en el archivo .env")
        
        url_confirmacion = f"{api_confirma_base}/{num_matricula}"
        
        # Reemplazar el href del botón de acción
        # Buscar específicamente el enlace dentro del botón CTA
        contenido_html = re.sub(
            r'(<a[^>]*href=")[^"]*("(?:[^>]*>.*?Cont&aacute;ctanos aqu&iacute;|[^>]*>.*?Contáctanos aquí))',
            rf'\1{url_confirmacion}\2',
            contenido_html,
            flags=re.DOTALL
        )
        
        # Convertir a bytes y luego a base64
        contenido_bytes = contenido_html.encode('utf-8')
        contenido_base64 = base64.b64encode(contenido_bytes).decode('utf-8')
        return contenido_base64
    except FileNotFoundError:
        raise Exception(f"No se encontró el archivo HTML: {ruta_html}")
    except Exception as e:
        raise Exception(f"Error al convertir HTML a base64: {str(e)}")
