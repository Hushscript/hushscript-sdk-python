from typing import Literal

CreateUploadBodyOriginSourceType3Type1 = Literal["recording", "upload"]

CREATE_UPLOAD_BODY_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES: set[
    CreateUploadBodyOriginSourceType3Type1
] = {
    "recording",
    "upload",
}


def check_create_upload_body_origin_source_type_3_type_1(
    value: str,
) -> CreateUploadBodyOriginSourceType3Type1:
    if value in CREATE_UPLOAD_BODY_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_UPLOAD_BODY_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES!r}"
    )
