from typing import Literal

TranscriptDetailOriginSourceType3Type1 = Literal["recording", "upload", "url"]

TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES: set[
    TranscriptDetailOriginSourceType3Type1
] = {
    "recording",
    "upload",
    "url",
}


def check_transcript_detail_origin_source_type_3_type_1(
    value: str,
) -> TranscriptDetailOriginSourceType3Type1:
    if value in TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_3_TYPE_1_VALUES!r}"
    )
