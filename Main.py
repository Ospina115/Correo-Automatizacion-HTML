from API.send_email import enviar_correo
from API.ConfirmaEnvio import confirmar_envio_email
from Database.OracleConnection import obtener_empresas_semana_anterior


def main():
    """
    Función principal para obtener empresas de la BD y enviar correos.
    """
    try:
        print("================================================================================")
        print("SISTEMA DE ENVÍO DE CORREOS - EMPRESAS NUEVAS")
        print("================================================================================\n")
        
        # Obtener empresas de la base de datos
        print("Conectando a la base de datos Oracle...")
        empresas = obtener_empresas_semana_anterior()
        
        if not empresas:
            print("⚠ No se encontraron empresas para procesar")
            return
        
        print(f"{'='*80}")
        print(f"PROCESANDO {len(empresas)} EMPRESA(S)")
        print(f"{'='*80}\n")
        
        # Contadores para estadísticas
        exitosos = 0
        fallidos = 0
        errores_autenticacion = 0
        
        # Procesar cada empresa
        for i, empresa in enumerate(empresas, 1):
            try:
                nombre_empresa = empresa.get('RAZON_SOCIAL')
                num_matricula = str(empresa.get('NIT'))
                correo = empresa.get('CORREO')
                nit = str(empresa.get('NIT'))
                
                # Validar que los datos necesarios existan
                if not correo:
                    print(f"[{i}/{len(empresas)}] ⚠ Empresa '{nombre_empresa}' sin correo. Omitiendo...")
                    fallidos += 1
                    continue
                
                print(f"[{i}/{len(empresas)}] Procesando:")
                print(f"  • Empresa: {nombre_empresa}")
                print(f"  • NIT: {nit}")
                print(f"  • Correo: {correo}")
                
                # Enviar correo
                resultado = enviar_correo(
                    destinatarios=correo,
                    asunto="Bienvenido a Cajasan - Portal de Beneficios Empresariales",
                    html_path="HTML/index.html",
                    nombre_empresa=nombre_empresa,
                    num_matricula=nit #se actualizó para usar el nit en vez del numero de la matricula
                )
                
                # Validar resultado
                if resultado.get("exito"):
                    print(f"  ✓ {resultado.get('mensaje', 'Correo enviado exitosamente')}")
                    
                    # Confirmar envío en la base de datos (estado "S" = enviado)
                    print("  ℹ Confirmando envío en BD...")
                    confirmacion = confirmar_envio_email(num_matricula, "S")
                    
                    if confirmacion.get("exito"):
                        print("  ✓ Confirmación registrada en BD\n")
                        exitosos += 1
                    else:
                        print(f"  ⚠ Advertencia: Correo enviado pero no se pudo confirmar en BD")
                        print(f"    Error: {confirmacion.get('error', 'Desconocido')}\n")
                        exitosos += 1  # Contamos como exitoso porque el correo sí se envió
                else:
                    fallidos += 1
                    
                    # Registrar fallo en la base de datos (estado "N" = no enviado)
                    print("  ℹ Registrando fallo en BD...")
                    confirmacion = confirmar_envio_email(num_matricula, "N")
                    
                    # Identificar si es error de autenticación
                    if resultado.get("status_code") == 500:
                        errores_autenticacion += 1
                        print("  ⚠ Posible error de autenticación. Considera renovar el token.\n")
                    else:
                        print(f"  ✗ Error: {resultado.get('error', 'Desconocido')}\n")
                
            except Exception as e:
                print(f"  ✗ Error inesperado al procesar empresa: {str(e)}\n")
                fallidos += 1
                continue
        
        # Resumen final
        print(f"{'='*80}")
        print("RESUMEN DE ENVÍO")
        print(f"{'='*80}")
        print(f"Total procesadas: {len(empresas)}")
        print(f"Exitosos: {exitosos}")
        print(f"Fallidos: {fallidos}")
        if errores_autenticacion > 0:
            print(f"  └─ Errores de autenticación/servidor (500): {errores_autenticacion}")
        print(f"{'='*80}\n")
        
    except Exception as e:
        print(f"\n✗ Error en el proceso principal: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
