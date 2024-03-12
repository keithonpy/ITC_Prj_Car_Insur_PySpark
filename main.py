from os.path import abspath
from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_replace, col
from FullLoad import FullLoad



if __name__ == "__main__":
    # PostgresSQL connection properties
    postgres_url = "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
    postgres_properties = {
        "user": "consultants",
        "password": "WelcomeItc@2022",
        "driver": "org.postgresql.Driver",
    }
    postgres_table_name = "car_insurance_claims"
    
    hive_data = {
        "hive_database_name": "project1db",
        "hive_table_name": "carInsuranceClaims"
    }
    FullLoad(postgres_url, postgres_properties, postgres_table_name, hive_data)