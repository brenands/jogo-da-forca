
from functions import helpers

def test_change_word_to_underline():
    result = helpers.change_word_to_underline("banana")
    expected = "_ _ _ _ _ _"

    assert  expected == result

def test_remove_special_characters():
    result = helpers.remove_special_characters("órfão")
    expected = "orfao"
    
    assert  expected == result

def test_check_if_exists_on_word_should_return_true():
    result = helpers.check_if_exists_on_word("banana", "a")
    expected = True
    
    assert  expected == result

def test_check_if_exists_on_word_should_return_false():
    result = helpers.check_if_exists_on_word("banana", "y")
    expected = False
    
    assert  expected == result

def test_show_correct_letters_doesnt_show_letters():
    result = helpers.show_correct_letters("banana", ["y", "p"])
    expected = "_ _ _ _ _ _"
    
    assert  expected == result

def test_show_correct_letters_should_show_letters():
    result = helpers.show_correct_letters("banana", ["a"])
    expected = "_ a _ a _ a"
    
    assert  expected == result
