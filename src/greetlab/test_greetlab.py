import pytest
import sys
from greetlab.cli import main

def test_whitespace_name_raises_system_exit():
    """当name只含空白字符时，main应以SystemExit(2)结束"""
    sys.argv = ["cli", "--name", "   "]
    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2
