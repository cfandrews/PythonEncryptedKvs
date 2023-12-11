# Copyright 2023 Charles Andrews
# fmt: off
"""[![Build Status](https://github.com/cfandrews/PythonEncryptedKvs/actions/workflows/build.yml/badge.svg)](https://github.com/cfandrews/PythonEncryptedKvs/actions)
[![Documentation Status](https://github.com/cfandrews/PythonEncryptedKvs/actions/workflows/documentation.yml/badge.svg)](https://github.com/cfandrews/PythonEncryptedKvs/actions)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Encrypted on-disk key-value store for arbitrary Python data.

[Source](https://github.com/cfandrews/PythonEncryptedKvs/)  
[Documentation](https://cfandrews.github.io/PythonEncryptedKvs/encryptedkvs.html)
"""  # noqa: W291, D205, D415
# fmt: on
from __future__ import annotations

from typing import Final

from .main import main

__all__: Final[list[str]] = ["main"]
__docformat__: Final[str] = "google"
