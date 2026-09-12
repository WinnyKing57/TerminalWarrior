from cli_lab import terminal


def test_game_commands_contains_key_commands():
    words = set(terminal.GAME_COMMANDS)
    for expected in ("ls -la", "cat Flag.txt", "cd Flag", "challenge", "help", "exit"):
        assert expected in words


def test_complete_returns_matching_candidates():
    candidates = ["ls", "ls -a", "ls -la", "cat", "cd"]
    assert terminal.complete("ls", candidates) == ["ls", "ls -a", "ls -la"]
    assert terminal.complete("cat", candidates) == ["cat"]


def test_complete_is_case_insensitive():
    candidates = ["cp", "chmod 777 HelloWorld.exe", "cat hidden.txt"]
    matches = terminal.complete("CAT", candidates)
    assert matches == ["cat hidden.txt"]


def test_complete_empty_prefix_returns_everything():
    candidates = ["ls", "cat"]
    assert terminal.complete("", candidates) == ["cat", "ls"]


def test_set_and_reset_completions():
    terminal.set_completions(["ls", "cd"])
    assert terminal.complete("") == ["cd", "ls"]
    terminal.reset_completions()
    assert "ls -la" in terminal.complete("ls -la")