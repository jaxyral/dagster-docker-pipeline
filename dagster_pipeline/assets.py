from dagster import asset

@asset
def my_asset():
    return "This is a sample asset."
