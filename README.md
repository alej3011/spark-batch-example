# Spark Batch Example
Bienvenidos, el repositorio almacena dos ejemplos en python, en los cuales se muestra el uso de Apache Spark y Kafka para el procesamiento conjunto de datos.

## Tecnologías usadas
Para hacer un poco más amena la experiencia y desarrollo de estos dos ejemplos se usaron:
- Jupyter (Equivalente a Google Collab).
- Python
- SDK de Kafka
- SDK de Apache Spark

## Ejemplos desarrollados
### 1. Procesamiento en Batch con Spark
Para este ejemplo, primero se seleccionó un dataset directamente de [Datos Colombia](https://www.datos.gov.co/Estad-sticas-Nacionales/Entradas-de-extranjeros-a-Colombia/96sh-4v8d/about_data), acerca de los datos migratorios desde 2012.

El objetivo era explorar el dataset, realizar una limpieza del dataset, hacer un análisis EDA y finalizar con un almacenamiento de dichos resultados en parker de Spark, el ejercicio se puede ver completo en el archivo [batch_procesing.ipynb](https://github.com/alej3011/spark-batch-example/blob/main/batch_procesing.ipynb), el cual es un formato que se carga en Jupyter y puede ser ejecutado por partes, un texto enriquesido.

#### ¿Cómo ejecutarlo?
> Pre-requisitos, tener instalado uv cómo manejador de paquetes e inicializar un entorno virtual: https://docs.astral.sh/uv/getting-started/installation/
1. Clone el presente proyecto
2. Abra una consola en la raíz del proyecto
3. Inicie el entorno virtual con: `.venv/bin/activate`
4. Instale las dependencias del proyecto con: `uv sync`
5. Abra otra terminal y ejecute en la primera el comando: `python src/google_finance_producer.py` y en la otra `python src/spark_streaming.py`

### 2. Procesamiento en tiempo real
En este ejemplo se buscaba mostrar una integración de Apache Kafka, y Spark Streaming, lo cual es básicamente conectar un flujo directo de datos con un
motor de procesamiento.

Aquí se hizo uso de datos financieros con la librería *yfinance* de python, para luego enviar los datos a un topic de kafka, esto se puede revisar en el archivo [google_finance_producer.py](https://github.com/alej3011/spark-batch-example/blob/main/src/google_finance_producer.py).

Para finalizar, se hizo un script donde Spark Streaming estaba activamente escuchando los topics de Kafka y procesando los datos para mostrarlos por consola, esto se hace en el archivo [spark_streaming.py](https://github.com/alej3011/spark-batch-example/blob/main/src/spark_streaming.py).

#### ¿Cómo ejecutarlo?
> Pre-requisitos, tener instalado uv cómo manejador de paquetes e inicializar un entorno virtual: https://docs.astral.sh/uv/getting-started/installation/
1. Clone el presente proyecto
2. Abra una consola en la raíz del proyecto
3. Inicie el entorno virtual con: `.venv/bin/activate`
4. Instale las dependencias del proyecto con: `uv sync`
5. Inicialize Jupyter con el comando: `jupyter lab`
6. Vaya al navegador
7. Abra el archivo *batch_procesing.ipyn*

Eso es todo :D.
