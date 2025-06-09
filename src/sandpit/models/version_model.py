import pydantic

class AboutModel(pydantic.BaseModel):
    description: str
    version: str