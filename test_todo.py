# test_todo.py
from todo import add, clear, todos
# Now your tests go here

def test_add():
    """Test adding a task to the to-do list"""
    add("Buy milk")
    assert len(todos) == 1

    def test_clear():
        """Test celaring the to-do list"""
        add("buy milk")
        clear()
        assert len(todos) == 0