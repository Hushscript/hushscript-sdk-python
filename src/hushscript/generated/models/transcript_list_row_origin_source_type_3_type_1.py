from typing import Literal

TranscriptListRowOriginSourceType3Type1 = Literal["recording", "upload", "url"]

TRANSCRIPT_LIST_ROW_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES: set[
    TranscriptListRowOriginSourceType3Type1
] = {
    "recording",
    "upload",
    "url",
}


def check_transcript_list_row_origin_source_type_3_type_1(
    value: str,
) -> TranscriptListRowOriginSourceType3Type1:
    if value in TRANSCRIPT_LIST_ROW_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_LIST_ROW_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES!r}"
    )
