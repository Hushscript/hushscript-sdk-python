from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcript_detail_origin_app_type_1 import (
    TranscriptDetailOriginAppType1,
    check_transcript_detail_origin_app_type_1,
)
from ..models.transcript_detail_origin_app_type_2_type_1 import (
    TranscriptDetailOriginAppType2Type1,
    check_transcript_detail_origin_app_type_2_type_1,
)
from ..models.transcript_detail_origin_app_type_3_type_1 import (
    TranscriptDetailOriginAppType3Type1,
    check_transcript_detail_origin_app_type_3_type_1,
)
from ..models.transcript_detail_origin_source_type_1 import (
    TranscriptDetailOriginSourceType1,
    check_transcript_detail_origin_source_type_1,
)
from ..models.transcript_detail_origin_source_type_2_type_1 import (
    TranscriptDetailOriginSourceType2Type1,
    check_transcript_detail_origin_source_type_2_type_1,
)
from ..models.transcript_detail_origin_source_type_3_type_1 import (
    TranscriptDetailOriginSourceType3Type1,
    check_transcript_detail_origin_source_type_3_type_1,
)

if TYPE_CHECKING:
    from ..models.transcript_detail_speaker_names import TranscriptDetailSpeakerNames
    from ..models.transcript_envelope import TranscriptEnvelope


T = TypeVar("T", bound="TranscriptDetail")


@_attrs_define
class TranscriptDetail:
    """
    Attributes:
        id (str):
        title (str):
        language_detected (None | str):
        duration_seconds (int):
        speaker_names (TranscriptDetailSpeakerNames): Provider speaker label mapped to a display name, for every speaker
            the caller has renamed.
        tags (list[str]):
        created_at (int):
        updated_at (int):
        auto_delete_at (int | None): When this transcript is scheduled to be purged, or null to keep it indefinitely.
        edited (bool): Whether the original body has been edited since transcription.
        matter_code (None | str): The workspace matter this transcript is filed under, or null. Set at upload time and
            editable afterwards; always null for a transcript that was never funded by a workspace.
        client_code (None | str): The workspace client this transcript is filed under, or null. Set at upload time and
            editable afterwards; always null for a transcript that was never funded by a workspace.
        body (TranscriptEnvelope): The transcript's full structured body.
        origin_source (None | TranscriptDetailOriginSourceType1 | TranscriptDetailOriginSourceType2Type1 |
            TranscriptDetailOriginSourceType3Type1): How the audio entered Hushscript: a file upload, an import from a link,
            or an in-app recording. Null when unknown, which is always the case for rows created before this field existed.
        origin_app (None | TranscriptDetailOriginAppType1 | TranscriptDetailOriginAppType2Type1 |
            TranscriptDetailOriginAppType3Type1): The app the job was created from: the web app, the Chrome extension, the
            Android or iOS app, or the API. Null when unknown, which is always the case for rows created before this field
            existed.
    """

    id: str
    title: str
    language_detected: None | str
    duration_seconds: int
    speaker_names: TranscriptDetailSpeakerNames
    tags: list[str]
    created_at: int
    updated_at: int
    auto_delete_at: int | None
    edited: bool
    matter_code: None | str
    client_code: None | str
    body: TranscriptEnvelope
    origin_source: (
        None
        | TranscriptDetailOriginSourceType1
        | TranscriptDetailOriginSourceType2Type1
        | TranscriptDetailOriginSourceType3Type1
    )
    origin_app: (
        None
        | TranscriptDetailOriginAppType1
        | TranscriptDetailOriginAppType2Type1
        | TranscriptDetailOriginAppType3Type1
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        language_detected: None | str
        language_detected = self.language_detected

        duration_seconds = self.duration_seconds

        speaker_names = self.speaker_names.to_dict()

        tags = self.tags

        created_at = self.created_at

        updated_at = self.updated_at

        auto_delete_at: int | None
        auto_delete_at = self.auto_delete_at

        edited = self.edited

        matter_code: None | str
        matter_code = self.matter_code

        client_code: None | str
        client_code = self.client_code

        body = self.body.to_dict()

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
                "speaker_names": speaker_names,
                "tags": tags,
                "created_at": created_at,
                "updated_at": updated_at,
                "auto_delete_at": auto_delete_at,
                "edited": edited,
                "matter_code": matter_code,
                "client_code": client_code,
                "body": body,
                "origin_source": origin_source,
                "origin_app": origin_app,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transcript_detail_speaker_names import (
            TranscriptDetailSpeakerNames,  # noqa: PLC0415
        )
        from ..models.transcript_envelope import TranscriptEnvelope  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_language_detected(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        language_detected = _parse_language_detected(d.pop("language_detected"))

        duration_seconds = d.pop("duration_seconds")

        speaker_names = TranscriptDetailSpeakerNames.from_dict(d.pop("speaker_names"))

        tags = cast(list[str], d.pop("tags"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_auto_delete_at(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        auto_delete_at = _parse_auto_delete_at(d.pop("auto_delete_at"))

        edited = d.pop("edited")

        def _parse_matter_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        matter_code = _parse_matter_code(d.pop("matter_code"))

        def _parse_client_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        client_code = _parse_client_code(d.pop("client_code"))

        body = TranscriptEnvelope.from_dict(d.pop("body"))

        def _parse_origin_source(
            data: object,
        ) -> (
            None
            | TranscriptDetailOriginSourceType1
            | TranscriptDetailOriginSourceType2Type1
            | TranscriptDetailOriginSourceType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_source_type_1 = check_transcript_detail_origin_source_type_1(
                    data
                )

                return origin_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_source_type_2_type_1 = (
                    check_transcript_detail_origin_source_type_2_type_1(data)
                )

                return origin_source_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_source_type_3_type_1 = (
                    check_transcript_detail_origin_source_type_3_type_1(data)
                )

                return origin_source_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TranscriptDetailOriginSourceType1
                | TranscriptDetailOriginSourceType2Type1
                | TranscriptDetailOriginSourceType3Type1,
                data,
            )

        origin_source = _parse_origin_source(d.pop("origin_source"))

        def _parse_origin_app(
            data: object,
        ) -> (
            None
            | TranscriptDetailOriginAppType1
            | TranscriptDetailOriginAppType2Type1
            | TranscriptDetailOriginAppType3Type1
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_app_type_1 = check_transcript_detail_origin_app_type_1(data)

                return origin_app_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_app_type_2_type_1 = (
                    check_transcript_detail_origin_app_type_2_type_1(data)
                )

                return origin_app_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_app_type_3_type_1 = (
                    check_transcript_detail_origin_app_type_3_type_1(data)
                )

                return origin_app_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | TranscriptDetailOriginAppType1
                | TranscriptDetailOriginAppType2Type1
                | TranscriptDetailOriginAppType3Type1,
                data,
            )

        origin_app = _parse_origin_app(d.pop("origin_app"))

        transcript_detail = cls(
            id=id,
            title=title,
            language_detected=language_detected,
            duration_seconds=duration_seconds,
            speaker_names=speaker_names,
            tags=tags,
            created_at=created_at,
            updated_at=updated_at,
            auto_delete_at=auto_delete_at,
            edited=edited,
            matter_code=matter_code,
            client_code=client_code,
            body=body,
            origin_source=origin_source,
            origin_app=origin_app,
        )

        transcript_detail.additional_properties = d
        return transcript_detail

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
