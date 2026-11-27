from typing import Literal

TranscriptDetailOriginSourceType1 = Literal["recording", "upload", "url"]

TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_1_VALUES: set[
    TranscriptDetailOriginSourceType1
] = {
    "recording",
    "upload",
    "url",
}


def check_transcript_detail_origin_source_type_1(
    value: str,
) -> TranscriptDetailOriginSourceType1:
    if value in TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_1_VALUES!r}"
    )
