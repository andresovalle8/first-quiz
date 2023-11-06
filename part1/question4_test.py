import pets_db as pets_db
from question4 import sql_pets_owned_by_nobody, sql_only_owned_by_bessie, sql_pets_older_than_owner

def test_question4_pets_older_than_owner():
    pets_db.create_db()
    with pets_db.get_connection() as con:
        res = con.execute(sql_pets_older_than_owner)
        result = res.fetchone()
    
    assert len(result) == 1
    assert result[0] == 2

def test_question4_pets_owned_by_nobody():
    pets_db.create_db()
    with pets_db.get_connection() as con:
        res = con.execute(sql_pets_owned_by_nobody)
        rows = res.fetchall()
    
    rows.sort()
    expected_rows = [('petey', 'gray whale', 38), ('shannon', 'cow', 14)]
    
    assert len(rows) == len(expected_rows)
    assert rows == expected_rows

def test_question4_only_owned_by_bessie():
    pets_db.create_db()
    with pets_db.get_connection() as con:
        res = con.execute(sql_only_owned_by_bessie)
        rows = res.fetchall()
    
    rows.sort()
    expected_rows = [('bessie', 'leyla', 'gray whale'), ('bessie', 'randolph', 'lemur')]
    
    assert len(rows) == len(expected_rows)
    assert rows == expected_rows
