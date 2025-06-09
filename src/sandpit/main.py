
from pathlib import Path
from sandpit.version import get_version
from sandpit.infrastructure.logging import logger
import sandpit.infrastructure.app_setup as app_setup
import fastapi
from sandpit.infrastructure import middleware

current_file = Path(__file__)
current_file_dir = current_file.parent
current_file_dir_absolute = current_file_dir.absolute()
project_root = current_file_dir.parent
project_root_absolute = project_root.resolve()
static_root_absolute = current_file_dir_absolute / "static"


app = fastapi.FastAPI(
    title="Sandpit Play API", middleware=middleware, lifespan=app_setup.app_lifespan
)

def setup_routes(app: fastapi.FastAPI):
    from sandpit.api.version_api import router as version_router

    # Include the version API routes
    app.include_router(version_router, prefix="/api/v1", tags=["version"])

    # Just log the current working directory - useful is some of the static files are not found.
    logger.info(f"Current working directory: {os.getcwd()}")

def main():
    print("Hello from Sandpit Play API!")


if __name__ == "__main__":
    main()
