import fastapi

from sandpit.infrastructure.logging import logger
from sandpit.version import get_version
from sandpit.models.version_model import AboutModel

router = fastapi.APIRouter()

@router.get("/about", response_model=AboutModel)
async def about():
    api_version = get_version()
    logger.info(f"API version: {api_version}")
    model = AboutModel(version=api_version, description="Sandpit Play API")
    return model