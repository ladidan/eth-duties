"""Defines logging messages
"""

CONNECTION_ERROR_MESSAGE = "Couldn't connect to beacon client. Retry in 2 second."
READ_TIMEOUT_ERROR_MESSAGE = "Couldn't read from beacon client. Retry in 5 seconds."
NO_RESPONSE_ERROR_MESSAGE = "Couldn't fetch any data from the beacon client."
NO_DATA_FIELD_IN_RESPONS_JSON_ERROR_MESSAGE = (
    "Response object does not include a 'data' field"
)
SYSTEM_EXIT_MESSAGE = "Detected user intervention (SIGINT). Shutting down."
NEXT_INTERVAL_MESSAGE = "Logging next interval..."
NO_UPCOMING_DUTIES_MESSAGE = "No upcoming duties detected!"
TOO_MANY_PROVIDED_VALIDATORS_FOR_FETCHING_ATTESTATION_DUTIES_MESSAGE = (
    "Provided number of validators for fetching attestion duties is high (> %s). "
    "This pollutes the console output and prevents checking important duties. "
    "Checking attestion duties will be skipped! "
    "To increase the max. number of logged attestation duties use '--max-attestation-duty-logs'"
)
HIGHER_PROCESSING_TIME_INFO_MESSAGE = (
    "You provided %s validators. Fetching all necessary data may take some time."
)
INACTIVE_VALIDATORS_MESSAGE = (
    "The following provided validators are not active "
    "and therefore will be skipped for further processing: %s"
)
WRONG_CHARACTER_IN_PROVIDED_VALIDATOR_IDENTIFIER_MESSAGE = (
    "Provided character is not supported for validator '%s'. "
    "Please only use ';' for separation of <INDEX_OR_PUBKEY> "
    "and <ALIAS> (e.g. 123;Validator_1). "
    "Furthermore only '-' and '_' are allowed for multiword alias.",
)
WRONG_OR_INCOMPLETE_PUBKEY_MESSAGE = "Wrong or incomplete provided pubkey: 0x%s"
PUBKEY_IS_NOT_HEXADECIMAL_MESSAGE = "Pubkey 0x%s is not hexadecimal: %s"
DUPLICATE_VALIDATORS_MESSAGE = (
    "Filtered duplicated validators with different identifiers: %s"
)
