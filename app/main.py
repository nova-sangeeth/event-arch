import uvicorn
from constants import main
from constants.api import API_PREFIX
from fastapi import FastAPI
from routers.api_router import main_router

# Initialize the FastAPI application.

app = FastAPI(
    docs_url=main.DOCS_URL,
    debug=main.DEBUG,
    title=main.TITLE,
    description=main.DESCRIPTION,
    version=main.VERSION,
)

# register routers.

app.include_router(router=main_router, prefix=API_PREFIX)

# Run the debug server with auto reload on change ot the files
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)
