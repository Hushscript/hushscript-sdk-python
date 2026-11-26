from typing import Literal

TranscriptListRowOriginAppType2Type1 = Literal[
    "android", "api", "extension", "ios", "web"
]

TRANSCRIPT_LIST_ROW_ORIGIN_APP_TYPE_2_TYPE_1_VALUES: set[
    TranscriptListRowOriginAppType2Type1
] = {
    "android",
    "api",
    "extension",
    "ios",
    "web",
}


def check_transcript_list_row_origin_app_type_2_type_1(
    value: str,
) -> TranscriptListRowOriginAppType2Type1:
    if value in TRANSCRIPT_LIST_ROW_ORIGIN_APP_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_LIST_ROW_ORIGIN_APP_TYPE_2_TYPE_1_VALUES!r}"
    )
