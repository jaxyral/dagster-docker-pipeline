# dagster-docker-pipeline

A repository for setting up the Dagster pipeline with Docker Compose and Tilt.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/jayral/dagster-docker-pipeline.git
   ```

2. Navigate to the repository directory:
   ```
   cd dagster-docker-pipeline
   ```

3. Install the required Python packages using Poetry:
   ```
   poetry install
   ```

4. Build and run the Docker Compose services:
   ```
   docker-compose up --build
   ```

5. Access the Dagster UI:
   Open your web browser and navigate to `http://localhost:3000` to access the Dagster UI.

## Running the Pipeline

1. Open the Dagster UI in your web browser.
2. Navigate to the pipeline and run it.
3. Monitor the pipeline execution and view the logs.

## Additional Information

- The `neo4j_resource.py` file contains the Neo4j resource configuration for Dagster.
- The `dagster_pipeline` directory contains the pipeline and asset definitions.
- The `Tiltfile` is used for local development with Tilt.
- The `pyproject.toml` file contains the Python project configuration.

## Contributing

Contributions are welcome! Please submit a pull request with your changes.
