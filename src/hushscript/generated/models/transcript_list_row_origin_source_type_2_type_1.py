from typing import Literal

TranscriptListRowOriginSourceType2Type1 = Literal["recording", "upload", "url"]

TRANSCRIPT_LIST_ROW_ORIGIN_SOURCE_TYPE_2_TYPE_1_VALUES: set[
    TranscriptListRowOriginSourceType2Type1
] = {
    "recording",
    "upload",
    "url",
}


def check_transcript_list_row_origin_source_type_2_type_1(
    value: str,
) -> TranscriptListRowOriginSourceType2Type1:
    if value in TRANSCRIPT_LIST_ROW_ORIGIN_SOURCE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_LIST_ROW_ORIGIN_SOURCE_TYPE_2_TYPE_1_VALUES!r}"
    )
