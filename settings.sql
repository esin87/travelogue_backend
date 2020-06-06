DROP
DATABASE IF EXISTS
travelogue;
DROP USER IF EXISTS
travelogueuser;

CREATE DATABASE travelogue;
CREATE USER travelogueuser
WITH PASSWORD 'travelogue';
GRANT ALL PRIVILEGES ON DATABASE travelogue TO travelogueuser;
