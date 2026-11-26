from typing import Literal

JobOriginAppType3Type1 = Literal["android", "api", "extension", "ios", "web"]

JOB_ORIGIN_APP_TYPE_3_TYPE_1_VALUES: set[JobOriginAppType3Type1] = {
    "android",
    "api",
    "extension",
    "ios",
    "web",
}


def check_job_origin_app_type_3_type_1(value: str) -> JobOriginAppType3Type1:
    if value in JOB_ORIGIN_APP_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {JOB_ORIGIN_APP_TYPE_3_TYPE_1_VALUES!r}"
    )
