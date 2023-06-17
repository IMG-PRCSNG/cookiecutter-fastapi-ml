import logging
import typer
from .config import Config


cli = typer.Typer()
config = Config()
logging.basicConfig(
    level=logging.DEBUG if config.verbose else logging.INFO,
    format="%(asctime)s (%(processName)s - %(threadName)s): %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()


@cli.callback()
def base():
    """
    {{ cookiecutter.project_name }} CLI
    """
    pass


@cli.command()
def serve():
    import uvicorn
    from .api import create_app

    app = create_app(config)
    uvicorn.run(
        app,
        host=config.host,
        port=config.port,
    )


if __name__ == "__main__":
    cli()
