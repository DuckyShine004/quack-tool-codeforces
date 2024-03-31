"""This module contains extension constants and compiler constants.

Attributes:
    COMPILER_TYPES (Dict): All valid compiler types.
    EXTENSIONS (Dict): All valid extension types.
"""

COMPILER_TYPES = {
    "cpp",
    "c",
    "csharp",
    "java",
}

EXTENSIONS = {
    "python": {
        "py",
        "pyc",
    },
    "cpp": {
        "cxx",
        "cpp",
        "cc",
        "c++",
    },
    "c": {
        "c",
    },
    "csharp": {
        "cs",
        "csx",
    },
    "java": {
        "java",
    },
}
