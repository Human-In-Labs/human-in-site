"""Automated tests for the Human In & PlanPaz Flask site."""

from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import app  # noqa: E402
import wsgi  # noqa: E402


class SiteTestCase(unittest.TestCase):
    """Verify routes, content parity, security headers, and static assets."""

    def setUp(self):
        self.client = app.test_client()

    def test_wsgi_exposes_app(self):
        self.assertIs(wsgi.app, app)

    def test_index_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)

        self.assertIn("Human In — Tecnologia para a mudança individual", html)
        self.assertIn("Tecnologia que serve", html)
        self.assertIn("Andrew Gabriel", html)
        self.assertIn('href="/planpaz"', html)
        self.assertIn("data-contact-form", html)
        self.assertIn("js/main.js", html)
        self.assertNotIn("lovable-badge", html)
        self.assertNotIn("__l5e", html)

    def test_planpaz_route(self):
        response = self.client.get("/planpaz")
        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)

        self.assertIn("PlanPaz — Cultive mudanças, de semente em semente", html)
        self.assertIn("Cultive. Cuide.", html)
        self.assertIn("Madre Teresa de Calcutá", html)
        self.assertIn('href="/"', html)

        for img_name in (
            "planpaz-welcome.png",
            "planpaz-inicio.png",
            "planpaz-biblioteca.png",
            "planpaz-jardim.png",
            "planpaz-comunidade.png",
        ):
            self.assertIn(img_name, html)

        self.assertNotIn("lovable-badge", html)
        self.assertNotIn("__l5e", html)

    def test_health_route(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})

    def test_404_page(self):
        response = self.client.get("/rota-inexistente")
        self.assertEqual(response.status_code, 404)
        html = response.get_data(as_text=True)
        self.assertIn("Página não encontrada", html)
        self.assertIn('href="/"', html)
        self.assertIn('href="/planpaz"', html)

    def test_security_headers(self):
        response = self.client.get("/")
        self.assertEqual(response.headers.get("X-Content-Type-Options"), "nosniff")
        self.assertEqual(
            response.headers.get("Referrer-Policy"),
            "strict-origin-when-cross-origin",
        )

    def test_all_static_assets_served(self):
        static_dir = PROJECT_ROOT / "static"
        expected_files = [
            "css/styles.css",
            "css/custom.css",
            "js/main.js",
            "images/favicon.png",
            "images/hi-logo.png",
            "images/planpaz-logo.png",
            "images/planpaz-welcome.png",
            "images/planpaz-inicio.png",
            "images/planpaz-biblioteca.png",
            "images/planpaz-jardim.png",
            "images/planpaz-comunidade.png",
            "images/og-image.png",
        ]
        for rel_path in expected_files:
            file_path = static_dir / rel_path
            self.assertTrue(file_path.exists(), f"Missing static file: {rel_path}")
            response = self.client.get(f"/static/{rel_path}")
            self.assertEqual(
                response.status_code, 200, f"Static file {rel_path} returned {response.status_code}"
            )
            self.assertGreater(len(response.data), 0, f"Empty static file: {rel_path}")
            response.close()


if __name__ == "__main__":
    unittest.main()
