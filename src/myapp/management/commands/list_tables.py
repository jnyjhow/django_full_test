from django.core.management.base import BaseCommand
from django.db import connections

class Command(BaseCommand):
    help = 'List all tables in the Oracle database'

    def handle(self, *args, **kwargs):
        try:
            with connections['default'].cursor() as cursor:
                cursor.execute("""
                    SELECT table_name
                    FROM all_tables
                    WHERE owner = 'ADMIN' -- Substitua 'ADMIN' pelo nome do usuário ou esquema correto
                """)
                
                tables = cursor.fetchall()
                for table in tables:
                    self.stdout.write(table[0])
            
            self.stdout.write("Connection successful and tables listed.")
        
        except Exception as e:
            self.stdout.write(f"Error: {e}")
