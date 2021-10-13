SELECT 'CREATE DATABASE mercado_bitcoin'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'mercado_bitcoin')\gexec