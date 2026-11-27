from typing import Literal

CreateUploadBodyModeType1 = Literal["private", "standard"]

CREATE_UPLOAD_BODY_MODE_TYPE_1_VALUES: set[CreateUploadBodyModeType1] = {
    "private",
    "standard",
}


def check_create_upload_body_mode_type_1(value: str) -> CreateUploadBodyModeType1:
    if value in CREATE_UPLOAD_BODY_MODE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_UPLOAD_BODY_MODE_TYPE_1_VALUES!r}"
    )
