import subprocess


def test_normal_name():
    p = subprocess.run(["sdt-greet", "--name", "王帅"], capture_output=True, text=True, check=False)
    assert p.returncode == 0
    assert "Hello, 王帅!" in p.stdout


def test_blank_name_fails():
    p = subprocess.run(["sdt-greet", "--name", "   "], capture_output=True, text=True, check=False)
    assert p.returncode == 2
