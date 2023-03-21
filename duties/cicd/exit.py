"""Module for continuous deployment usage
"""

from sys import exit as sys_exit
from typing import List

from cli.arguments import Mode
from fetcher.data_types import ValidatorDuty


def exit_on_cicd_mode(running_mode: Mode, duties: List[ValidatorDuty]) -> None:
    """Exits the running application if mode is 'cicd' and duties could be found
    for the provided validators

    Args:
        running_mode (Mode): Running mode of eth-duties
        duties (List[ValidatorDuty]): List of fetched validator duties
    """
    match running_mode:
        case Mode.CI_CD:
            if len(duties) > 0:
                sys_exit(1)
            sys_exit(0)
        case _:
            pass
