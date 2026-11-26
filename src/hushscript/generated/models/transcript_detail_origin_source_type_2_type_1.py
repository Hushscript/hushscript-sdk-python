from typing import Literal

TranscriptDetailOriginSourceType2Type1 = Literal["recording", "upload", "url"]

TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_2_TYPE_1_VALUES: set[
    TranscriptDetailOriginSourceType2Type1
] = {
    "recording",
    "upload",
    "url",
}


def check_transcript_detail_origin_source_type_2_type_1(
    value: str,
) -> TranscriptDetailOriginSourceType2Type1:
    if value in TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSCRIPT_DETAIL_ORIGIN_SOURCE_TYPE_2_TYPE_1_VALUES!r}"
    )
