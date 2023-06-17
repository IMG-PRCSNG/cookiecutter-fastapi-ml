import logging
from .server import create_app, Config


def serve():
    from fastapi.staticfiles import StaticFiles

    _config = Config()
    logging.basicConfig(
        level=logging.DEBUG if _config.verbose else logging.INFO,
        format="%(asctime)s (%(processName)s - %(threadName)s): %(name)s - %(levelname)s - %(message)s",
    )
    app = create_app(_config)
    app.mount('/public', StaticFiles(directory="public"), name="public")

    return app
