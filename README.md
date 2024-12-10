# up_ml_flow_deploy

Repositorio dedicado al proyecto escolar de cloud computing para desplegar modelos registrados en un servicio de MLFlow.

Este repositorio automatiza el despliegue de modelos utilizando Cloud Run y GitHub Actions, generando una interfaz y un endpoint configurados con **FastAPI**. Incluye buenas prácticas como el uso de **Pydantic** para la validación de datos. El servicio recupera los artefactos necesarios del bucket donde fueron almacenados por el servicio de MLFlow.

---

## Configuración de Variables

Para desplegar el servicio, edita las siguientes variables dentro del archivo de configuración:

```yaml
env:
  REGION: La región que estás usando (ejemplo: us-central1).
  PROJECT_ID: Tu ID de proyecto en GCP.
  REPOSITORY: Tu repositorio creado en Artifact Registry.
  SERVICE_ACCOUNT: El correo completo de la cuenta de servicio.
  SERVICE_NAME: Un nombre adecuado para tu servicio en Cloud Run.
  IMAGE_NAME: Un nombre adecuado para la imagen que usará Cloud Run.
  DEPLOY: Cambiar a true si deseas desplegar el servicio automáticamente.
  MODEL_URI: El ID del modelo registrado en MLFlow.
```

---

## Características

- **Despliegue Automático**: El servicio se despliega automáticamente en Cloud Run mediante GitHub Actions.
- **Interfaz de API**: Utiliza FastAPI para exponer un endpoint funcional y fácilmente integrable.
- **Validación Robusta**: Implementa Pydantic para garantizar la validación de datos en la API.
- **Recuperación de Artefactos**: El servicio obtiene los artefactos del bucket configurado en GCP donde MLFlow los almacenó.
- **Eficiencia y Seguridad**: Aprovecha buenas prácticas para optimizar y proteger el despliegue del servicio.

---

## Buenas Prácticas

1. **Pruebas Locales**:
   - Antes de realizar el despliegue, se recomienda montar el contenedor localmente y ejecutar pruebas para garantizar su correcto funcionamiento.
   - Usa herramientas como `Docker` para construir y probar la imagen:

     ```bash
     docker build -t [IMAGE_NAME] .
     docker run -p 8080:8080 [IMAGE_NAME]
     ```

2. **Versionado del Modelo**:
   - Asegúrate de que el modelo registrado en MLFlow tiene un URI correcto y está en su versión final.

3. **Monitoreo**:
   - Configura herramientas de monitoreo en Cloud Run para supervisar el desempeño del servicio desplegado.

---

## Despliegue Paso a Paso

1. **Configura los Secrets en GitHub**:
   - Ve a la configuración del repositorio y agrega los siguientes secrets bajo la pestaña **Secrets & Variables -> Actions**:
     - `GOOGLE_APPLICATION_CREDENTIALS`: Copia el contenido del archivo `sa-private-key.json` que contiene las credenciales de tu cuenta de servicio.

2. **Reemplaza las Variables de Entorno**:
   - Edita el archivo de configuración de GitHub Actions (`.yml`) y reemplaza las variables bajo `env` con las específicas de tu proyecto.

3. **Construcción y Despliegue**:
   - Realiza un `push` al repositorio. El flujo de trabajo de GitHub Actions construirá el contenedor, lo subirá a Artifact Registry y lo desplegará en Cloud Run.

4. **Verifica el Despliegue**:
   - Ve a la consola de Cloud Run en GCP y asegúrate de que el servicio esté activo.
   - Prueba el endpoint expuesto para verificar la funcionalidad.

---

## Notas Adicionales

- **Optimización del Contenedor**:
  - Mantén el `Dockerfile` lo más simple y eficiente posible para reducir el tiempo de construcción y el tamaño de la imagen.
- **Seguridad**:
  - Evita subir credenciales sensibles al repositorio. Usa GitHub Secrets para gestionar las claves de acceso.
- **Escalabilidad**:
  - Configura Cloud Run para manejar cargas variables, asegurándote de que los límites de CPU y memoria estén correctamente establecidos.

---

Con estos pasos, podrás desplegar y gestionar modelos en un entorno de producción usando MLFlow, GitHub Actions, y Google Cloud Platform.

