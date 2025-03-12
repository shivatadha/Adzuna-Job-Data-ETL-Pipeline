import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import explode, col, to_timestamp

# Initialize Glue job and context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Set fixed values manually
job_name = "adzuna_etl_transformation_job"
s3_source_path = "s3://adzuna-project-etl/raw_data/to_process/"
s3_output_path = "s3://adzuna-project-etl/transformed_data/"

# Initialize the job
job.init(job_name, {})

# Read data from S3
source_dyf = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="json",
    connection_options={"paths": [s3_source_path], "recurse": True},
    transformation_ctx="source_dyf"
)

# Convert to DataFrame and transform
jobs_df = source_dyf.toDF()
transformed_df = jobs_df.select(
    col("id").alias("job_id"),
    col("title").alias("job_title"),
    col("location.display_name").alias("job_location"),
    col("company.display_name").alias("job_company"),
    col("category.label").alias("job_category"),
    col("description").alias("job_description"),
    col("redirect_url").alias("job_url"),
    to_timestamp(col("created"), "yyyy-MM-dd'T'HH:mm:ss'Z'").alias("job_created"),
    col("salary_min"),
    col("salary_max")
).dropDuplicates(["job_id"])

# Write data to S3
transformed_df.write.mode("overwrite").parquet(s3_output_path)

job.commit()
