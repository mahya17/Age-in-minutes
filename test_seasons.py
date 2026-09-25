from seasons import main
import pytest

def test_valid_date(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "2000-01-01")
    main()
    captured = capsys.readouterr()
    assert "minutes" in captured.out

def test_invalid_format(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "January 1, 2000")
    with pytest.raises(SystemExit):
        main()

def test_invalid_date(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2000-13-40")
    with pytest.raises(SystemExit):
        main()
