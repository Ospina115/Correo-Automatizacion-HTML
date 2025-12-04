# 🚀 GUÍA RÁPIDA DE USO - Envío Masivo de Correos

## ✅ Sistema Actualizado

El script ahora incluye:
- ✅ Lectura automática del CSV
- ✅ Personalización con nombre de empresa
- ✅ Conversión automática de caracteres especiales (á, é, í, ó, ú, ñ) a entidades HTML
- ✅ Envío correo por correo con reporte en tiempo real
- ✅ Estadísticas completas al finalizar

## 📝 PASO 1: Prueba Individual

Antes de enviar a todas las empresas, haz una prueba:

```bash
python test_single_email.py
```

Edita `test_single_email.py` para cambiar el correo de prueba y verificar que todo funciona correctamente.

## 🚀 PASO 2: Envío Masivo

Una vez confirmado que funciona, ejecuta el envío masivo:

```bash
python send_email.py
```

Esto procesará todas las empresas del archivo `Noviembre.csv` y enviará un correo personalizado a cada una.

## 📊 Qué Hace el Script

1. **Lee el CSV** `Noviembre.csv` con las empresas
2. **Por cada empresa**:
   - Extrae la RAZON_SOCIAL y CORREO
   - Convierte caracteres especiales del nombre a entidades HTML (á → &aacute;)
   - Reemplaza `{{COMPANY_NAME}}` en el HTML con el nombre de la empresa
   - Convierte el HTML a Base64
   - Obtiene un token de autenticación
   - Envía el correo
3. **Muestra progreso** en tiempo real: `[5/120] Procesando: EMPRESA X`
4. **Al finalizar** muestra estadísticas:
   - Total procesados
   - Exitosos
   - Fallidos (con detalles de errores)

## ⚙️ Configuración del Delay

Por defecto hay un delay de **2 segundos** entre cada envío. Si quieres cambiarlo, edita en `send_email.py`:

```python
resultado = procesar_csv_y_enviar_correos(
    csv_path="Noviembre.csv",
    html_path="index copy.html",
    asunto="Bienvenido a Cajasan - Portal de Beneficios Empresariales",
    delay_segundos=3  # Cambiar aquí (en segundos)
)
```

## 📋 Formato del CSV

El script espera estas columnas:
- `RAZON_SOCIAL` - Nombre de la empresa
- `CORREO` - Email del destinatario
- `FECHA_MATRICULA` - (opcional, no se usa)
- `MATRICULA` - (opcional, no se usa)

## 🔧 Funciones Disponibles

### Envío Individual
```python
from send_email import enviar_correo

enviar_correo(
    destinatarios="email@ejemplo.com",
    asunto="Asunto del correo",
    html_path="index copy.html",
    nombre_empresa="NOMBRE DE LA EMPRESA"
)
```

### Conversión de Caracteres
```python
from send_email import convertir_caracteres_especiales_a_html

texto_convertido = convertir_caracteres_especiales_a_html("Café & Compañía")
# Resultado: "Caf&eacute; &amp; Compa&ntilde;&iacute;a"
```

## 📈 Ejemplo de Salida

```
================================================================================
INICIANDO PROCESO DE ENVÍO MASIVO DE CORREOS
================================================================================

Total de empresas a procesar: 120

[1/120] Procesando: LUZ NEY CRUZ CHIMA
    Correo: pastosverdeazules@gmail.com
    ✓ Correo enviado exitosamente

[2/120] Procesando: BRAYAN HELI PRADILLA JIMENEZ
    Correo: brayanpradilla131@gmail.com
    ✓ Correo enviado exitosamente

...

================================================================================
RESUMEN DEL PROCESO
================================================================================
Total procesados: 120
Exitosos: 118 (98.3%)
Fallidos: 2 (1.7%)
================================================================================
```

## ⚠️ Notas Importantes

1. **Caracteres especiales**: El sistema convierte automáticamente á, é, í, ó, ú, ñ, etc.
2. **Template HTML**: Usa `index copy.html` (versión con entidades HTML)
3. **Token**: Se renueva automáticamente en cada envío
4. **Errores**: Si un envío falla, continúa con el siguiente

## 🐛 Solución de Problemas

**Error: "No se encontró el archivo CSV"**
- Verifica que `Noviembre.csv` esté en la misma carpeta

**Error: "Token inválido"**
- Verifica las credenciales en el archivo `.env`

**Caracteres mal codificados en el correo**
- El sistema ya los convierte automáticamente
- Si persiste, verifica que uses `index copy.html` (no `index.html`)

## 📞 Archivos del Proyecto

- `send_email.py` - Script principal (envío masivo)
- `test_single_email.py` - Script de prueba individual
- `PyToken.py` - Obtención de token
- `index copy.html` - Template HTML con entidades
- `Noviembre.csv` - Lista de empresas
- `.env` - Credenciales de API

---

**¡Listo para enviar! 🎉**
