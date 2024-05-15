import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        # Testa se a página principal carrega corretamente
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Formulário da Escola', response.data)

    def test_form_submission(self):
        # Testa se o formulário é submetido corretamente
        response = self.app.post('/', data=dict(
            nome='João',
            email='joao@example.com',
            telefone='1234567890',
            cargo='Professor'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Nome: João', response.data)
        self.assertIn(b'E-mail: joao@example.com', response.data)
        self.assertIn(b'Telefone: 1234567890', response.data)
        self.assertIn(b'Cargo: Professor', response.data)

if __name__ == '__main__':
    unittest.main()
