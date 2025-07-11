# Deploy a MCP Server on Cloud Run

This project is a simple demonstration of how to create a MCP server using the `fastmcp` library and deploy it as a containerized service on Google Cloud Run.

The server exposes two basic tools:
- `add`: Adds two numbers.
- `subtract`: Subtracts two numbers.

## Project Structure

- `server.py`: The main application server using `fastmcp`.
- `test_server.py`: A client to test the server, both locally and when deployed.
- `Dockerfile`: Used to containerize the application for Cloud Run.
- `requirements.txt`: Python dependencies.

## Prerequisites

- Python 3.8+
- Google Cloud SDK (`gcloud`) installed and configured.
- A Google Cloud project with billing enabled.
- The Cloud Run API enabled in your GCP project.

## Running Locally

1.  **Clone the repository.**

```
git clone https://github.com/georgemao/mcp-on-cloudrun.git
```

2.  **Set up a virtual environment (recommended):**
UV is a Python package manager similar to Pip. Install it using the method that’s most appropriate for your development environment.

3.  **Install dependencies:**
```
uv sync
```

## Deploying to Cloud Run

1.  **Authenticate with gcloud:**
    ```bash
    gcloud auth login
    gcloud config set project YOUR_PROJECT_ID
    ```
    Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

2.  **Deploy the service:**
    Run the following command from the root of the project directory:
    
    ```bash
    gcloud run deploy mcp-server --source . --region us-central1 --allow-unauthenticated
    ```
    
    - `mcp-server`: You can change this to your preferred service name.
    - `--source .`: This tells gcloud to build a container from the source code in the current directory using the `Dockerfile`.
    - `--region`: Choose a region that is close to you.
    - `--allow-unauthenticated`: This makes the service publicly accessible. Remove this flag if you want to control access using IAM.

    When the deployment is complete, gcloud will output the **Service URL**.

## Testing the Deployed Service

You can use the `test_server.py` client to test your deployed service.

Proxy localhost calls to Cloud Run and provide the correct authentication. This will prompt you to enter your IAM account password. The account you’re using must have permissions to invoke Run services. If necessary, add this permission to your IAM role: `roles/run.invoker`

```
gcloud run services proxy mcp-server --region=us-central1
```

1.  **Run a test script**
    ```bash
    python test_server.py
    ```
    The client will now connect to your Cloud Run service and test the tools.

2.  **Test with a GUI: MCP Inspector:**
    If you prefer to use a GUI based tool to test your MCP Server, MCP Inspector is built for this purpose. 

    ```
    npx @modelcontextprotocol/inspector
    ```

    Copy the Session Token, enter it into the Inspector Configuration, and click `Connect`Connect