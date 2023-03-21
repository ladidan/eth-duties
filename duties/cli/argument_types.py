"""Module for argument parser related types
"""

from enum import Enum


class Mode(Enum):
    """Defines the mode at which eth-duties will run"""

    LOG = "log"
    CI_CD = "cicd"
