from flask import Flask, render_template


def create_app() -> Flask:
    """Application factory for the portfolio map site."""
    app = Flask(__name__, static_folder="static", template_folder="templates")

    from .register_dash import register_dash_apps

    register_dash_apps(app)

    @app.route("/")
    def landing():
        return render_template("landing.html")

    return app
