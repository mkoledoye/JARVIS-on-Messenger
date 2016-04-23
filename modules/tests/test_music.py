import modules

def test_movie():
    assert('music' == modules.process_query('ophelia song')[0])
    assert('music' == modules.process_query('who sang Hold You Up?')[0])
    assert('music' == modules.process_query('When was the Fast Car song released?')[0])
    assert('music' != modules.process_query('something random')[0])
