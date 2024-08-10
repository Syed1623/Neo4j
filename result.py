from  services.neo4jSetUp import kg
from queries.cypherQueries import *

result = kg.query(getPerson);
print(f'result----->{result}');