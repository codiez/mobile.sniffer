"""

    Django configuration file for pre-existing Apex Vertex MySQL databse.

    MySQL SQL dump distribution settings.
    
    Bind Django models to existing MySQL table. 

"""
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'apex'             # Or path to database file if using sqlite3.
DATABASE_USER = 'apex'             # Not used with sqlite3.
DATABASE_PASSWORD = 'apex'             # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

HANDSET_HACK = True

INSTALLED_APPS = (    
    'mobile.sniffer.apexvertex',
)

