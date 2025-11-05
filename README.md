# 📧 Correo Automatización HTML - Cajasan

## 📋 Descripción

Este repositorio contiene plantillas HTML optimizadas para el envío de correos electrónicos corporativos de **Cajasan - Caja de Ahorro y Crédito de Santander**. Las plantillas están diseñadas siguiendo las mejores prácticas para emails HTML, garantizando compatibilidad con los principales clientes de correo electrónico.

Específicamente, este proyecto automatiza el envío de correos a nuevas empresas de Santander, presentando los servicios y beneficios que Cajasan ofrece al sector empresarial.

## 🎯 Características

- ✅ **Compatible con múltiples clientes de correo**: Gmail, Outlook, Apple Mail, etc.
- ✅ **Diseño responsivo**: Se adapta a diferentes tamaños de pantalla
- ✅ **Estructura basada en tablas**: Máxima compatibilidad con clientes antiguos
- ✅ **Estilos inline**: CSS incorporado directamente en las etiquetas HTML
- ✅ **Identidad corporativa**: Colores y elementos visuales de Cajasan
- ✅ **Variables dinámicas**: Placeholders para personalización automática
- ✅ **Optimizado para bots**: Integración con sistemas de automatización

## 🎨 Identidad Visual

La plantilla sigue el manual de identidad visual de Cajasan:

- **Color principal**: `#1e5aa8` (Azul Cajasan)
- **Color secundario**: `#2a6bb8` (Azul claro)
- **Tipografía**: Arial, sans-serif (para máxima compatibilidad)
- **Elementos**: Logo oficial, slogan corporativo, íconos descriptivos

## 📁 Estructura del Proyecto

```
Correo-Automatizacion-HTML/
│
├── index.html                          # Plantilla principal para correos empresariales
├── README.md                           # Este archivo
└── CM-MPP-M002 MANUAL DE IDENTIDAD VISUAL CAJASAN v 2 (1).pdf
```

## 🔧 Variables Dinámicas

La plantilla utiliza las siguientes variables que pueden ser reemplazadas dinámicamente:

### Variables Principales
- `{{COMPANY_NAME}}` - Nombre de la empresa destinataria
- `{{CONTACT_EMAIL}}` - Email de contacto de Cajasan
- `{{CONTACT_PHONE}}` - Teléfono de contacto
- `{{CONTACT_ADDRESS}}` - Dirección física
- `{{CURRENT_YEAR}}` - Año actual
- `{{EMAIL_TIMESTAMP}}` - Fecha y hora de envío

### Variables Opcionales
- `{{ADDITIONAL_INFO}}` - Información adicional personalizada
- `{{SHOW_ADDITIONAL_INFO}}` - Mostrar/ocultar sección adicional

## 💼 Casos de Uso

### 1. Presentación de Servicios Empresariales
Correo para nuevas empresas presentando los servicios de Cajasan:
- 💰 Descuento por nómina
- 📊 Ahorro empresarial
- 🏦 Créditos corporativos
- 👥 Programas de bienestar para colaboradores

### 2. Comunicaciones Corporativas
- Anuncios de nuevos productos
- Invitaciones a eventos empresariales
- Boletines informativos
- Seguimiento a clientes corporativos

## 🚀 Cómo Usar

### Opción 1: Uso Manual

1. Abre `index.html` en un editor de texto
2. Reemplaza las variables `{{VARIABLE_NAME}}` con los valores reales
3. Copia el código HTML resultante
4. Pégalo en tu cliente de correo o plataforma de email marketing

### Opción 2: Automatización con Script

```javascript
// Ejemplo en Node.js
const fs = require('fs');

// Leer la plantilla
let template = fs.readFileSync('index.html', 'utf8');

// Reemplazar variables
const datos = {
  COMPANY_NAME: 'Empresa XYZ S.A.S.',
  CONTACT_EMAIL: 'empresas@cajasan.com',
  CONTACT_PHONE: '(607) 123 4567',
  CONTACT_ADDRESS: 'Calle 35 # 10-43, Bucaramanga',
  CURRENT_YEAR: new Date().getFullYear(),
  EMAIL_TIMESTAMP: new Date().toLocaleDateString('es-CO')
};

Object.keys(datos).forEach(key => {
  const regex = new RegExp(`{{${key}}}`, 'g');
  template = template.replace(regex, datos[key]);
});

// Guardar o enviar el email procesado
fs.writeFileSync('email_personalizado.html', template);
```

### Opción 3: Integración con Plataformas de Email

#### Mailchimp
1. Crea una nueva campaña
2. Selecciona "Code your own"
3. Pega el código HTML
4. Usa merge tags de Mailchimp: `*|COMPANY_NAME|*`

#### SendGrid
1. Crea una nueva plantilla dinámica
2. Pega el HTML
3. Define las variables en el panel de SendGrid

#### Outlook / Office 365
1. Abre el HTML en un navegador
2. Copia el contenido renderizado (Ctrl+A, Ctrl+C)
3. Pega en un nuevo correo de Outlook

## 📱 Pruebas de Compatibilidad

Se recomienda probar la plantilla en:

- ✅ Gmail (Web, iOS, Android)
- ✅ Outlook (Web, Desktop, iOS, Android)
- ✅ Apple Mail (macOS, iOS)
- ✅ Yahoo Mail
- ✅ Thunderbird

### Herramientas de Prueba Recomendadas

- [Litmus](https://www.litmus.com/) - Testing de emails en múltiples clientes
- [Email on Acid](https://www.emailonacid.com/) - Análisis y pruebas
- [HTML Email Check](https://www.htmlemailcheck.com/check/) - Validación gratuita

## 🔒 Mejores Prácticas

1. **Evita JavaScript**: Los clientes de correo lo bloquean
2. **Usa tablas para layout**: Mayor compatibilidad que CSS Grid/Flexbox
3. **Estilos inline**: Evita `<style>` tags externos
4. **Imágenes hosteadas**: Usa URLs absolutas (CDN recomendado)
5. **Texto alternativo**: Siempre incluye `alt` en imágenes
6. **Tamaño máximo**: Mantén el HTML bajo 102KB
7. **Texto plano**: Incluye versión de texto plano como fallback

## 🖼️ Gestión de Imágenes

Las imágenes deben estar alojadas en servidores externos:

```html
<!-- Ejemplo actual -->
<img src="https://res.cloudinary.com/df84r8tny/image/upload/v1751918973/LOGO_CAJASAN_LOGO_VRT-BLANCO_u7krqi.png" 
     alt="Cajasan" 
     width="120" />
```

### Recomendaciones
- Usa servicios CDN: Cloudinary, ImgIX, AWS S3
- Optimiza las imágenes (compresión, tamaño adecuado)
- Usa formatos compatibles: JPG, PNG, GIF
- Evita: SVG, WebP (compatibilidad limitada)

## 📊 Métricas y Seguimiento

Para trackear la efectividad de los emails:

```html
<!-- Pixel de seguimiento (opcional) -->
<img src="https://tu-servidor.com/track?email={{EMAIL_ID}}" 
     width="1" height="1" style="display:none;" />

<!-- Links con parámetros UTM -->
<a href="https://www.cajasan.com?utm_source=email&utm_medium=corporativo&utm_campaign=nuevas_empresas">
  Visita nuestro sitio web
</a>
```

## 🛠️ Personalización Avanzada

### Agregar Nueva Sección

```html
<!-- Nueva sección después de servicios -->
<tr>
  <td style="padding-bottom: 25px">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%"
           style="background-color: #ffffff; border-radius: 8px; border: 1px solid #e9ecef;">
      <tr>
        <td style="padding: 25px;">
          <h3 style="margin: 0 0 15px 0; font-size: 18px; font-weight: bold; color: #1e5aa8;">
            🎯 Tu Título Aquí
          </h3>
          <p style="margin: 0; font-size: 15px; color: #333333; line-height: 1.6;">
            Tu contenido aquí
          </p>
        </td>
      </tr>
    </table>
  </td>
</tr>
```

### Cambiar Colores

Para actualizar los colores corporativos, busca y reemplaza:
- `#1e5aa8` → Color principal
- `#2a6bb8` → Color secundario
- `#e6f2ff` → Color texto claro
- `#f8f9fa` → Color fondo

## 📞 Contacto y Soporte

**Cajasan - Caja de Ahorro y Crédito de Santander**

- 📞 Línea Nacional: 018000 960 960
- 📧 Email: servicioalcliente@cajasan.com
- 🌐 Web: [www.cajasan.com](https://www.cajasan.com)
- 📍 Dirección: Bucaramanga, Santander, Colombia

## 📄 Licencia

Este proyecto es propiedad de **Cajasan**. Uso interno exclusivo para comunicaciones oficiales de la organización.

## 🤝 Contribuciones

Para sugerencias o mejoras:

1. Contacta al área de Comunicaciones o Marketing
2. Envía propuestas al equipo de Desarrollo Digital
3. Sigue las guías de identidad visual corporativa

## 📚 Recursos Adicionales

- [Manual de Identidad Visual Cajasan](./CM-MPP-M002%20MANUAL%20DE%20IDENTIDAD%20VISUAL%20CAJASAN%20v%202%20(1).pdf)
- [Guía de Email HTML - Campaign Monitor](https://www.campaignmonitor.com/css/)
- [Can I Email](https://www.caniemail.com/) - Compatibilidad CSS en emails

---

## 📅 Historial de Versiones

### v1.1.0 (2025-01-07)
- ✨ Actualización completa para correos a nuevas empresas
- ✨ Sección de servicios empresariales detallada
- ✨ Call-to-action con email personalizable
- ✨ Footer corporativo con información de contacto
- ✨ Identidad visual Cajasan completamente aplicada
- 📝 README completo y documentación extendida

### v1.0.0 (Inicial)
- ✨ Plantilla base para automatización de correos

---

**Hecho con ❤️ por el equipo de Cajasan**

*"Cada día más cerca para llegar más lejos"*
