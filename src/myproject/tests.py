from django.test import SimpleTestCase
from django.test import TestCase
from django.db import connection


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class DatabaseConnectionTest(TestCase):
    def test_oracle_connection(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM dual")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1)
        except Exception as e:
            self.fail(f"Falha ao conectar ao banco de dados Oracle: {str(e)}")
