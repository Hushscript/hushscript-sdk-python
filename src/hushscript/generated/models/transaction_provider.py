from typing import Literal

TransactionProvider = Literal["apple", "google", "stripe"]

TRANSACTION_PROVIDER_VALUES: set[TransactionProvider] = {
    "apple",
    "google",
    "stripe",
}


def check_transaction_provider(value: str) -> TransactionProvider:
    if value in TRANSACTION_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSACTION_PROVIDER_VALUES!r}"
    )
