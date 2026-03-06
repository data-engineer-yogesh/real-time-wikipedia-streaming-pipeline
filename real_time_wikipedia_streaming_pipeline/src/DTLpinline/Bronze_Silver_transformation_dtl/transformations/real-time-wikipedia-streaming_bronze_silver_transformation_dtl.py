from pyspark.sql.functions import current_timestamp, col
import dlt
from pyspark.sql.types import *

volume_path = "/Volumes/real_time_wikipedia_streaming_pipeline/bronze/wikipedia_raw_data"
primary_key = "id"

wikipedia_schema = StructType(
    [
        StructField("$schema", StringType(), True),
        StructField(
            "meta",
            StructType(
                [
                    StructField("uri", StringType(), True),
                    StructField("request_id", StringType(), True),
                    StructField("id", StringType(), True),
                    StructField("dt", StringType(), True),
                    StructField("domain", StringType(), True),
                    StructField("stream", StringType(), True),
                    StructField("topic", StringType(), True),
                    StructField("partition", IntegerType(), True),
                    StructField("offset", LongType(), True),
                ]
            ),
            True,
        ),
        StructField("id", LongType(), True),
        StructField("type", StringType(), True),
        StructField("namespace", IntegerType(), True),
        StructField("title", StringType(), True),
        StructField("title_url", StringType(), True),
        StructField("comment", StringType(), True),
        StructField("timestamp", LongType(), True),
        StructField("user", StringType(), True),
        StructField("bot", BooleanType(), True),
        StructField("minor", BooleanType(), True),
        StructField("patrolled", BooleanType(), True),
        StructField("notify_url", StringType(), True),
        StructField(
            "length",
            StructType(
                [
                    StructField("old", IntegerType(), True),
                    StructField("new", IntegerType(), True),
                ]
            ),
            True,
        ),
        StructField(
            "revision",
            StructType(
                [
                    StructField("old", LongType(), True),
                    StructField("new", LongType(), True),
                ]
            ),
            True,
        ),
        StructField("server_url", StringType(), True),
        StructField("server_name", StringType(), True),
        StructField("server_script_path", StringType(), True),
        StructField("wiki", StringType(), True),
        StructField("parsedcomment", StringType(), True),
    ]
)

@dlt.table(name="real_time_wikipedia_streaming_data_vw")
def real_time_wikipedia_streaming_data():
    df = (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load(volume_path)
        .withColumn("_load_timestamp", current_timestamp())
    )
    df = df.withColumnRenamed("$schema", "schemaName").withColumnRenamed("title_url", "titleUrl").withColumnRenamed("_rescued_data", "rescued_data")
    df = df.filter(col("schemaName").isNotNull() & col("length").isNotNull())
    return df

dlt.create_streaming_table(name="real_time_wikipedia_streaming_data")

dlt.apply_changes(
    target="real_time_wikipedia_streaming_data",
    source="real_time_wikipedia_streaming_data_vw",
    keys=[primary_key],
    sequence_by="_load_timestamp")

