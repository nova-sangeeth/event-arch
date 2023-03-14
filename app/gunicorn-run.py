import argparse
import subprocess

# Define command-line arguments using argparse
parser = argparse.ArgumentParser(
    description="Run a FastAPI app with Gunicorn and Uvicorn"
)
parser.add_argument(
    "--module",
    default="main",
    help="The name of the Python module containing the FastAPI app",
)
parser.add_argument(
    "--workers",
    type=int,
    default=4,
    help="The number of worker processes to use",
)
parser.add_argument(
    "--port",
    type=int,
    default=8000,
    help="The port to listen on",
)
parser.add_argument(
    "--host",
    default="0.0.0.0",
    help="The interface to bind to",
)
parser.add_argument(
    "--log-level",
    default="info",
    help="The log level for the server",
)
args = parser.parse_args()

# Construct the gunicorn command as a list of strings
cmd = [
    "gunicorn",
    f"{args.module}:app",
    "-w",
    str(args.workers),
    "-k",
    "uvicorn.workers.UvicornWorker",
    "-b",
    f"{args.host}:{args.port}",
    "--log-level",
    args.log_level,
]

# Use subprocess.Popen to start the server as a subprocess and capture its output
with subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    bufsize=1,
    universal_newlines=True,
) as process:
    # Iterate over the lines of the output and print them to the console
    for line in process.stdout:
        print(line, end="")
