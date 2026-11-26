from typing import Literal

JobOriginSourceType1 = Literal["recording", "upload", "url"]

JOB_ORIGIN_SOURCE_TYPE_1_VALUES: set[JobOriginSourceType1] = {
    "recording",
    "upload",
    "url",
}


def check_job_origin_source_type_1(value: str) -> JobOriginSourceType1:
    if value in JOB_ORIGIN_SOURCE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {JOB_ORIGIN_SOURCE_TYPE_1_VALUES!r}"
    )
