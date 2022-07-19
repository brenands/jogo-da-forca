# Test Report

*Report generated on 19-Jul-2022 at 20:33:52 by [pytest-md]*

[pytest-md]: https://github.com/hackebrot/pytest-md

## Summary

6 tests ran in 0.06 seconds

- 1 failed
- 5 passed

## 1 failed

### tests/test_helpers.py

`test_check_if_exists_on_word_should_return_false` 0.00s

```
def test_check_if_exists_on_word_should_return_false():
        result = helpers.check_if_exists_on_word("banana", "y")
        expected = False
    
>       assert  expected == result
E       assert False == None

tests/test_helpers.py:26: AssertionError
```

## 5 passed

### tests/test_helpers.py

`test_change_word_to_underline` 0.00s

`test_remove_special_characters` 0.00s

`test_check_if_exists_on_word_should_return_true` 0.00s

`test_show_correct_letters_doesnt_show_letters` 0.00s

`test_show_correct_letters_should_show_letters` 0.00s
