import pytest
from rock_paper_scissors import RockPaperScissors

@pytest.fixture
def game_object():
    return RockPaperScissors()


def test_valid_answer(game_object):
    assert game_object.valid_answer("rock") == True
    assert game_object.valid_answer("paper") == True
    assert game_object.valid_answer("scissors") == True
    assert game_object.valid_answer("invalid_choice") == False


def test_winning_answer(game_object):
    assert game_object.winning_answer("rock", "scissors") == True
    assert game_object.winning_answer("paper", "rock") == True
    assert game_object.winning_answer("scissors", "paper") == True
    assert game_object.winning_answer("rock", "paper") == False
    assert game_object.winning_answer("paper", "scissors") == False
    assert game_object.winning_answer("scissors", "rock") == False


def test_equal_answer(game_object):
    assert game_object.equal_answer("rock","rock") == True
    assert game_object.equal_answer("paper","paper") == True
    assert game_object.equal_answer("scissors","scissors") == True
    assert game_object.equal_answer("rock","paper") == False
    assert game_object.equal_answer("rock","scissors") == False
    assert game_object.equal_answer("paper","scissors") == False
