from django.test import SimpleTestCase
from django.test import TestCase
from django.db import connections, DatabaseError


class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class DatabaseConnectionTest(TestCase):
    def setUp(self):
        self.connection = connections["default"]
        self.engine = self.connection.settings_dict["ENGINE"]

    def test_database_connection(self):
        if "sqlite" in self.engine:
            self._test_sqlite_connection()
        elif "oracle" in self.engine:
            self._test_oracle_connection()
        elif "postgresql" in self.engine or "psycopg2" in self.engine:
            self._test_postgresql_connection()
        else:
            self.skipTest(f"Banco de dados não suportado: {self.engine}")

    def _test_oracle_connection(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM dual")
                result = cursor.fetchone()
                self.assertIsNotNone(result)
        except DatabaseError as e:
            self.fail(f"Falha ao conectar ao banco de dados Oracle: {str(e)}")

    def _test_sqlite_connection(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT sqlite_version()")
                result = cursor.fetchone()
                self.assertIsNotNone(result)
                print(f"SQLite version: {result[0]}")
        except DatabaseError as e:
            self.fail(f"Falha ao conectar ao banco de dados SQLite: {str(e)}")

    def _test_postgresql_connection(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT version()")
                result = cursor.fetchone()
                self.assertIsNotNone(result)
                print(f"PostgreSQL version: {result[0]}")
        except DatabaseError as e:
            self.fail(f"Falha ao conectar ao banco de dados PostgreSQL: {str(e)}")
