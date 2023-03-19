"""Module for continuous deployment usage
"""

from enum import Enum


class Mode(Enum):
    """Defines the mode at which eth-duties will run"""

    LOG = 0
    CONTINUOUS_DEPLOYMENT = 1


def exit_on_duty() -> None:
    ...
