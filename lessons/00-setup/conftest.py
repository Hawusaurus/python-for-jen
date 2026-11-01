# Lets the tests find your code in exercises/ and bughunt/.
# You don't need to touch this file.
import sys
from pathlib import Path

HERE = Path(__file__).parent
for folder in ("exercises", "bughunt"):
    sys.path.insert(0, str(HERE / folder))
