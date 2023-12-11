# Copyright 2023 Charles Andrews
"""Unit tests for encryptedkvs.main."""

from encryptedkvs import main


class TestMain:
    """Unit tests for encryptedkvs.Main."""

    @staticmethod
    def test_main() -> None:
        """Unit test for happy-path cases of encryptedkvs.Main.main."""
        main()
