import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

try:
    import pyfiglet  # noqa: F401
except ImportError:
    class _FakePyfiglet:
        def figlet_format(self, text, font="slant"):
            return text

    sys.modules["pyfiglet"] = _FakePyfiglet()