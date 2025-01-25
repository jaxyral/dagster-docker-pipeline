from dagster import pipeline, solid

@solid
def hello_world(context):
    context.log.info("Hello, world!")

@pipeline
def my_pipeline():
    hello_world()
