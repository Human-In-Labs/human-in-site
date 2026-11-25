"""Flask entry point for the Human In and PlanPaz website."""

from datetime import datetime
import os
from pathlib import Path

from flask import Flask, jsonify, redirect, render_template, url_for
from werkzeug.middleware.proxy_fix import ProxyFix
from whitenoise import WhiteNoise

import data

BASE_DIR = Path(__file__).resolve().parent


def create_app() -> Flask:
    """Create and configure the Flask WSGI application."""
    flask_app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates",
    )

    flask_app.wsgi_app = ProxyFix(flask_app.wsgi_app, x_for=1, x_proto=1, x_host=1)
    flask_app.wsgi_app = WhiteNoise(
        flask_app.wsgi_app,
        root=str(BASE_DIR / "static"),
        prefix="static/",
        max_age=3600,
    )

    @flask_app.context_processor
    def inject_globals() -> dict:
        return {"current_year": datetime.now().year}

    @flask_app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault(
            "Referrer-Policy", "strict-origin-when-cross-origin"
        )
        return response

    @flask_app.get("/")
    def planpaz():
        return render_template(
            "planpaz.html",
            meta=data.PLANPAZ_META,
            nav_links=data.PLANPAZ_NAV,
            hero_pills=data.PLANPAZ_HERO_PILLS,
            pains=data.PLANPAZ_PAINS,
            steps=data.PLANPAZ_STEPS,
            features=data.PLANPAZ_FEATURES,
            screens=data.PLANPAZ_SCREENS,
            evolution_items=data.PLANPAZ_EVOLUTION,
            community_posts=data.PLANPAZ_COMMUNITY,
            impacts=data.PLANPAZ_IMPACTS,
            differentials=data.PLANPAZ_DIFFERENTIALS,
        )

    @flask_app.get("/humanin")
    def index():
        return render_template(
            "index.html",
            meta=data.COMPANY_META,
            nav_links=data.COMPANY_NAV,
            stats=data.COMPANY_STATS,
            conception_cards=data.CONCEPTION_CARDS,
            values=data.VALUES,
            team_members=data.TEAM_MEMBERS,
        )

    @flask_app.get("/planpaz")
    def planpaz_redirect():
        return redirect(url_for("planpaz"))

    @flask_app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @flask_app.errorhandler(404)
    def page_not_found(_error):
        return (
            render_template(
                "404.html",
                meta={
                    "title": "Página não encontrada — Human In",
                    "description": "A página solicitada não foi encontrada.",
                    "og_title": "Página não encontrada — Human In",
                    "og_description": "A página solicitada não foi encontrada.",
                },
            ),
            404,
        )

    return flask_app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
