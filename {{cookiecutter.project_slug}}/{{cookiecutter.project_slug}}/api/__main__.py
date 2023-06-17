import uvicorn
from ..config import Config

_config = Config()

uvicorn.run(
    "{{ cookiecutter.project_slug }}.api:serve",
    host=_config.host,
    port=_config.port,
    reload=True,
    factory=True,
)
