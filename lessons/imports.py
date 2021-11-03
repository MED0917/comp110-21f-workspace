"""Examples of imports."""

from lessons import helpers

# Import using an alias
from lessons import helpers as hp

from lessons.helpers import powerful

print(helpers.powerful(2, 4))
print(hp.THE_ANSWER)
print(f"imports.py: {__name__}")