cypher = '''
MATCH (n)
RETURN count(n)
''';

getPerson = '''
MATCH (person:PERSON{name:'Syed Arbaz'})
RETURN person AS user
'''