from importlib import import_module
from typing import Callable

DashAppFactory = Callable[[object], None]


def register_dash_apps(app) -> None:
    """Attempt to mount each Dash app; skip modules that fail to import."""
    mappings = {
        "markov": "/markov/",
        "arima": "/arima/",
        "claims": "/claims/",
        "chesscnn": "/chess-cnn/",
    }

    for module_name, base_path in mappings.items():
        try:
            module = import_module(f".dashapps.{module_name}", package=__package__)
        except ImportError as exc:
            app.logger.warning("Skipping %s Dash app: %s", module_name, exc)
            continue

        factory = getattr(module, "init_app", None)
        if callable(factory):
            factory(app, url_base_pathname=base_path)
