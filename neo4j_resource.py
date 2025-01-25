from dagster import resource
from neo4j import GraphDatabase

@resource(config_schema={"uri": str, "user": str, "password": str})
def neo4j_resource(context):
    uri = context.resource_config["uri"]
    user = context.resource_config["user"]
    password = context.resource_config["password"]
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver
