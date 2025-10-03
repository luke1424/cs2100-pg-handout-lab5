"""Package marker for the assignment repository.

This file exists so tools that expect a package (like some pylint
invocations) won't fail when they attempt to import the repository.
"""

# Module name is the repository name and may contain hyphens; silence
# the invalid-name check for this file only.
# pylint: disable=invalid-name
__all__: list[str] = []
