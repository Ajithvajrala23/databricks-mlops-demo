# tests/test_hello.py
from hello import get_message

def test_message():
    message = get_message()
    assert message.startswith("Hello")
    assert "Stage" in message
