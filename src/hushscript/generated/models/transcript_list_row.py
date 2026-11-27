from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcript_list_row_insights_state import (
    TranscriptListRowInsightsState,
    check_transcript_list_row_insights_state,
)
from ..models.transcript_list_row_origin_app_type_1 import (
    TranscriptListRowOriginAppType1,
    check_transcript_list_row_origin_app_type_1,
)
from ..models.transcript_list_row_origin_app_type_2_type_1 import (
    TranscriptListRowOriginAppType2Type1,
    check_transcript_list_row_origin_app_type_2_type_1,
)
from ..models.transcript_list_row_origin_app_type_3_type_1 import (
    TranscriptListRowOriginAppType3Type1,
    check_transcript_list_row_origin_app_type_3_type_1,
)
from ..models.transcript_list_row_origin_source_type_1 import (
    TranscriptListRowOriginSourceType1,
    check_transcript_list_row_origin_source_type_1,
)
from ..models.transcript_list_row_origin_source_type_2_type_1 import (
    TranscriptListRowOriginSourceType2Type1,
    check_transcript_list_row_origin_source_type_2_type_1,
)
from ..models.transcript_list_row_origin_source_type_3_type_1 import (
    TranscriptListRowOriginSourceType3Type1,
    check_transcript_list_row_origin_source_type_3_type_1,
)

if TYPE_CHECKING:
    from ..models.options_summary import OptionsSummary


T = TypeVar("T", bound="TranscriptListRow")


@_attrs_define
class TranscriptListRow:
    """
    Attributes:
        id (str):
        title (str):
        language_detected (None | str):
        duration_seconds (int):
        created_at (int):
        auto_delete_at (int | None):
        tags (list[str]):
        options (OptionsSummary): A content-free summary of the transcription options a job was submitted with: what was
            requested, never the free-text content itself.
        insights_state (TranscriptListRowInsightsState): A display hint only, never an authority on whether Insights may
            be generated or charged for.
        origin_source (None | TranscriptListRowOriginSourceType1 | TranscriptListRowOriginSourceType2Type1 |
            TranscriptListRowOriginSourceType3Type1): How the audio entered Hushscript: a file upload, an import from a
            link, or an in-app recording. Null when unknown, which is always the case for rows created before this field
            existed.
        origin_app (None | TranscriptListRowOriginAppType1 | TranscriptListRowOriginAppType2Type1 |
            TranscriptListRowOriginAppType3Type1): The app the job was created from: the web app, the Chrome extension, the
            Android or iOS app, or the API. Null when unknown, which is always the case for rows created before this field
            existed.
    """

    id: str
    title: str
    language_detected: None | str
    duration_seconds: int
    created_at: int
    auto_delete_at: int | None
    tags: list[str]
    options: OptionsSummary
    insights_state: TranscriptListRowInsightsState
    origin_source: (
        None
        | TranscriptListRowOriginSourceType1
        | TranscriptListRowOriginSourceType2Type1
        | TranscriptListRowOriginSourceType3Type1
    )
    origin_app: (
        None
        | TranscriptListRowOriginAppType1
        | TranscriptListRowOriginAppType2Type1
        | TranscriptListRowOriginAppType3Type1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        language_detected: None | str
        language_detected = self.language_detected

        duration_seconds = self.duration_seconds

        created_at = self.created_at

        auto_delete_at: int | None
        auto_delete_at = self.auto_delete_at

        tags = self.tags

        options = self.options.to_dict()

        insights_state: str = self.insights_state

        origin_source: None | str
        if isinstance(self.origin_source, str):
            origin_source = self.origin_source
        elif isinstance(self.origin_source, str):
            origin_source = self.origin_source
        elif isinstance(self.origin_source, str):
            origin_source = self.origin_source
        else:
            origin_source = self.origin_source

        origin_app: None | str
        if isinstance(self.origin_app, str):
            origin_app = self.origin_app
        elif isinstance(self.origin_app, str):
            origin_app = self.origin_app
        elif isinstance(self.origin_app, str):
            origin_app = self.origin_app
        else:
            origin_app = self.origin_app

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "language_detected": language_detected,
                "duration_seconds": duration_seconds,
                "created_at": created_at,
                "auto_delete_at": auto_delete_at,
                "tags": tags,
                "options": options,
                "insights_state": insights_state,
                "origin_source": origin_source,
                "origin_app": origin_app,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.options_summary import OptionsSummary  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_language_detected(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language_detected = _parse_language_detected(d.pop("language_detected"))

        duration_seconds = d.pop("duration_seconds")

        created_at = d.pop("created_at")

        def _parse_auto_delete_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        auto_delete_at = _parse_auto_delete_at(d.pop("auto_delete_at"))

        tags = cast(list[str], d.pop("tags"))

        options = OptionsSummary.from_dict(d.pop("options"))

        insights_state = check_transcript_list_row_insights_state(
            d.pop("insights_state")
        )

        def _parse_origin_source(
            data: object,
        ) -> (
            None
            | TranscriptListRowOriginSourceType1
            | TranscriptListRowOriginSourceType2Type1
            | TranscriptListRowOriginSourceType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_source_type_1 = check_transcript_list_row_origin_source_type_1(
                    data
                )

                return origin_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_source_type_2_type_1 = (
                    check_transcript_list_row_origin_source_type_2_type_1(data)
                )

                return origin_source_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_source_type_3_type_1 = (
                    check_transcript_list_row_origin_source_type_3_type_1(data)
                )

                return origin_source_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TranscriptListRowOriginSourceType1
                | TranscriptListRowOriginSourceType2Type1
                | TranscriptListRowOriginSourceType3Type1,
                data,
            )

        origin_source = _parse_origin_source(d.pop("origin_source"))

        def _parse_origin_app(
            data: object,
        ) -> (
            None
            | TranscriptListRowOriginAppType1
            | TranscriptListRowOriginAppType2Type1
            | TranscriptListRowOriginAppType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_app_type_1 = check_transcript_list_row_origin_app_type_1(data)

                return origin_app_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_app_type_2_type_1 = (
                    check_transcript_list_row_origin_app_type_2_type_1(data)
                )

                return origin_app_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_app_type_3_type_1 = (
                    check_transcript_list_row_origin_app_type_3_type_1(data)
                )

                return origin_app_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TranscriptListRowOriginAppType1
                | TranscriptListRowOriginAppType2Type1
                | TranscriptListRowOriginAppType3Type1,
                data,
            )

        origin_app = _parse_origin_app(d.pop("origin_app"))

        transcript_list_row = cls(
            id=id,
            title=title,
            language_detected=language_detected,
            duration_seconds=duration_seconds,
            created_at=created_at,
            auto_delete_at=auto_delete_at,
            tags=tags,
            options=options,
            insights_state=insights_state,
            origin_source=origin_source,
            origin_app=origin_app,
        )

        transcript_list_row.additional_properties = d
        return transcript_list_row

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
