from typing import Literal

JobOriginSourceType3Type1 = Literal["recording", "upload", "url"]

JOB_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES: set[JobOriginSourceType3Type1] = {
    "recording",
    "upload",
    "url",
}


def check_job_origin_source_type_3_type_1(value: str) -> JobOriginSourceType3Type1:
    if value in JOB_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {JOB_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES!r}"
    )
