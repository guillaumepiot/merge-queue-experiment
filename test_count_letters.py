from count_letters import count_letters_fn

def test_response():
    assert count_letters_fn("") == "Empty string!"
    assert count_letters_fn("A") == "There is 1 letter in this string."
    assert count_letters_fn("Hello") == "There are 5 letters in this string."
    assert count_letters_fn("I love cheese") == "There are 11 letters in this string."
