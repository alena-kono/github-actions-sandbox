"""Here I try to reproduce errors displayed by flake8-isort."""
from typing import Tuple

from try_github_actions.main.imports_src import (
    ResponseStatus,
    TimeoutSec,
    UrlStatus,
    Urls,
)


def get_import_type() -> Tuple[str, str, str, str]:
    """Get import type.

    Returns:
        Import type.
    """
    return (
        type(ResponseStatus),
        type(TimeoutSec),
        type(Urls),
        type(UrlStatus),
    )
