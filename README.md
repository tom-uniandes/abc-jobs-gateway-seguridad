# abc-jobs-gateway

Gateway del experimento para el proyecto ABC

## Configuracion de Docker
1. Crear la network para los dos microservicios del experimento (correr solo una vez)

    ```bash
    docker network create abc-network-seguridad
    ```
2. Construir la imagen de docker 
    ```bash
     docker build -t gateway-seguridad .
    ```
3. Crear y iniciar el container (correr solo una vez)
    ```bash
    docker run --network=abc-network-seguridad --name gateway-seguridad -p 5005:5005 gateway-seguridad
    ```
4. Iniciar el container de nuevo:
    ```bash
    docker start gateway-seguridad
    ```