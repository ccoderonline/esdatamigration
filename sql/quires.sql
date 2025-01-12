-- List available schemas
SELECT schema_name
FROM information_schema.schemata;

-- Create new schema
CREATE SCHEMA NEW_SCHEMA_NAME;

-- Delete schema
DROP SCHEMA SCHEMA_NAME_TO_DELETE;

-- List available tables in schema
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'YOUR_SCHEMA_NAME';

-- Delete table by name
DROP TABLE YOUR_SCHEMA_NAME.YOUR_TABLE_NAME;

-- Drop all content from tables in the schema
TRUNCATE TABLE collection;

