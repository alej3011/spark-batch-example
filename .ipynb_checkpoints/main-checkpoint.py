from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, sum

# Create nuestra instancia de Spark con nombre appName
spark = SparkSession.builder \
    .appName("ProcesamientoY_EDA_Reseñas") \
    .master("local[*]") \
    .getOrCreate()

try:
  # Carga de archivos de texto en formato csv
  df_migrations = spark.read.csv("public/Entradas_de_extranjeros_a_Colombia_20251022.csv", header=True, inferSchema=True)
  df_migrations.show(5)

  # Limpieza y ajuste de datos
  ## 1. Renombrar columnas primero
  df_migrations = df_migrations \
    .withColumnsRenamed({
      "Año": "year",
      "Mes": "month",
      "Total": "total",
      "Codigo M49": "nationality",
      "Femenino": "gender_female",
      "Masculino": "gender_male",
      "Indefinido": "gender_unknown"
    })

  ## 2. Aplicar filtros
  df_migrations = df_migrations \
    .withColumn("total", regexp_replace(col("total"), ",", "")) \
    .withColumn("total", col("total").cast("int")) \
    .withColumns({
      "gender_female": regexp_replace(col("gender_female"), ",", ""),
      "gender_male": regexp_replace(col("gender_male"), ",", ""),
      "gender_unknown": regexp_replace(col("gender_unknown"), ",", ""),
    }) \
    .withColumn("month",
      when(col("month") == "Enero", "01")
      .when(col("month") == "Febrero", "02")
      .when(col("month") == "Marzo", "03")
      .when(col("month") == "Abril", "04")
      .when(col("month") == "Mayo", "05")
      .when(col("month") == "Junio", "06")
      .when(col("month") == "Julio", "07")
      .when(col("month") == "Agosto", "08")
      .when(col("month") == "Septiembre", "09")
      .when(col("month") == "Octubre", "10")
      .when(col("month") == "Noviembre", "11")
      .when(col("month") == "Diciembre", "12")
      .otherwise(None)
    ) \
    .filter(col("total") > 0) \
    .filter(col("month").isNotNull())

  ## 3. Aplicar casting de tipos de datos
  df_migrations = df_migrations \
    .withColumns({
      "year": col("year").cast("int"),
      "month": col("month").cast("int"),
      "total": col("total").cast("int"),
      "nationality": col("nationality").cast("string"),
      "gender_female": col("gender_female").cast("int"),
      "gender_male": col("gender_male").cast("int"),
      "gender_unknown": col("gender_unknown").cast("int")
    }) \
    .withColumn("gender_unknown", when(col("gender_unknown").isNull(), 0).otherwise(col("gender_unknown")))

  ## 4. Eliminar columnas innecesarias
  df_migrations = df_migrations \
    .drop("Nacionalidad", "Ubicación PCM")

  df_migrations.show(5)

  print("Descripción de las columnas de género")
  df_migrations.describe("gender_female", "gender_male", "gender_unknown").show()

  print("Resumen de las migraciones")
  df_migrations.describe("total").show()

  # Vamos a mostrar el total de migraciones por año
  df_migrations.groupBy("year").agg(sum("total").alias("total")).sort("year").show()

  

except Exception as e:
  print(f"Error al cargar el archivo: {e}")
