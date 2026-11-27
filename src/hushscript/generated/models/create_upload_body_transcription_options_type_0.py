from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUploadBodyTranscriptionOptionsType0")


@_attrs_define
class CreateUploadBodyTranscriptionOptionsType0:
    """Transcription options for this job. Every field is optional; omitting the object requests the account's default
    behaviour (language auto-detection and speaker labels on).

        Attributes:
            language_code (None | str | Unset): Force a specific spoken language instead of auto-detection. Key terms, a
                prompt and filler words (keep_disfluencies) only take effect for the 33 languages AssemblyAI serves with its
                newest model; for the other languages, typed key terms or a typed prompt are refused with
                invalid_transcription_options.
            speaker_detection (bool | Unset): Label distinct speakers in the transcript. Independent of translation_targets.
            keyterms_prompt (list[str] | Unset): Domain vocabulary to bias transcription toward, up to 1000 terms of at most
                6 words each, and at most 1,000 words in total after merging saved dictionaries and one-off terms. Refused with
                invalid_transcription_options when the language (language_code, or every expected language under auto-detection)
                is one where key terms have no effect, or when the merged terms and the prompt together exceed the provider
                token budget (how many fit depends on the script and the length of the terms).
            prompt (None | str | Unset): Free-text context to bias transcription toward. Refused with
                invalid_transcription_options when the language is one where a prompt has no effect. Sent as written, separately
                from the key terms; the two share one provider token budget.
            one_off_keyterms (list[str] | Unset): Key terms for this job only, merged with keyterms_prompt and the terms of
                any dictionary_ids. Same limits as keyterms_prompt: up to 1000 terms of at most 6 words each, and at most 1,000
                words in total across all key terms. Refused with invalid_transcription_options on a language where key terms
                have no effect.
            one_off_prompt (None | str | Unset): Prompt text for this job only, joined to prompt and any prompt_preset_id
                text. Refused with invalid_transcription_options on a language where a prompt has no effect. Shares the provider
                token budget with the key terms.
            dictionary_ids (list[str] | Unset): Saved dictionaries to apply, by the 32-character lowercase hex ids that GET
                /v1/transcription-context lists. Their terms join the key terms and count toward the key-term limits. Duplicates
                are ignored; at most 50 distinct ids. A malformed id or one the caller cannot read is refused with
                invalid_transcription_options. On a language where key terms have no effect the selection is skipped, not
                refused.
            prompt_preset_id (None | str | Unset): A saved prompt preset to apply, by the 32-character lowercase hex id that
                GET /v1/transcription-context lists. Its text is joined to prompt and one_off_prompt. A malformed id or one the
                caller cannot read is refused with invalid_transcription_options. On a language where a prompt has no effect the
                selection is skipped, not refused.
            expected_languages (list[str] | Unset): Auto-detection hint: restrict language detection to these codes (any
                code accepted by language_code). Ignored when language_code is set. An unsupported code is refused with
                invalid_transcription_options. Key terms, a prompt and keep_disfluencies apply when every expected language
                supports them, are skipped when none does, and otherwise apply only if the detected language does.
            fallback_language (None | str | Unset): Auto-detection hint: the language to use when detection is unsure. Must
                be one of expected_languages, otherwise refused with invalid_transcription_options. Ignored when language_code
                is set.
            medical_mode (bool | Unset): Bill and transcribe as a medical dictation. Requires language_code to be one of en,
                en_au, en_uk, en_us, es, fr, de, de_ch; billed at a 100 percent surcharge on the duration. Cannot be combined
                with vet_mode.
            vet_mode (bool | Unset): Beta. Transcribe as a veterinary dictation. Requires a manually set language_code from
                the supported list; auto-detection is refused. Billed at a 100 percent surcharge on the duration, exactly like
                medical_mode, and cannot be combined with medical_mode. Not available in private mode.
            keep_disfluencies (bool | Unset): Keep disfluencies in the transcript instead of removing them. On many
                languages this also keeps repetitions, stutters and false starts; on others it keeps filler words only. Free,
                and allowed in private mode. Defaults to false. Only takes effect for the languages where key terms take effect;
                for any other language the server stores false.
            multichannel (bool | Unset): Transcribe each audio channel independently. Billed per channel: a stereo file
                counts twice, a 3-channel file three times, up to 8 channels, and the medical or vet surcharge applies on top of
                that; translation targets stay on a single duration. The channel count is the most channels any audio track of
                the file carries. A file with more than 8 channels, or one whose channel count cannot be read, falls back to
                mixed audio with speaker labels and is billed once. Without this option the file is transcribed as one mixed
                channel and billed once. The initial hold at upload creation is for a single channel; verification raises it to
                the per-channel amount and fails the job with insufficient_balance if the balance cannot cover it.
            translation_targets (list[str] | Unset): Locales to additionally translate the transcript into: any language
                code accepted by language_code except the regional variants (en_au, en_uk, en_us, de_ch), 99 in all. At most 15
                distinct targets per upload (a saved edit holds the original plus 15 translations); more is refused with
                invalid_transcription_options. A target equal to the source language is refused. Each target adds a 25 percent
                surcharge on the duration.
            auto_generate_insights (bool | None | Unset): Override the account's automatic-Insights default for this upload
                alone. Omit to inherit the account default; an explicit false always suppresses automatic generation for this
                upload.
    """

    language_code: None | str | Unset = UNSET
    speaker_detection: bool | Unset = UNSET
    keyterms_prompt: list[str] | Unset = UNSET
    prompt: None | str | Unset = UNSET
    one_off_keyterms: list[str] | Unset = UNSET
    one_off_prompt: None | str | Unset = UNSET
    dictionary_ids: list[str] | Unset = UNSET
    prompt_preset_id: None | str | Unset = UNSET
    expected_languages: list[str] | Unset = UNSET
    fallback_language: None | str | Unset = UNSET
    medical_mode: bool | Unset = UNSET
    vet_mode: bool | Unset = UNSET
    keep_disfluencies: bool | Unset = UNSET
    multichannel: bool | Unset = UNSET
    translation_targets: list[str] | Unset = UNSET
    auto_generate_insights: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language_code: None | str | Unset
        if isinstance(self.language_code, Unset):
            language_code = UNSET
        else:
            language_code = self.language_code

        speaker_detection = self.speaker_detection

        keyterms_prompt: list[str] | Unset = UNSET
        if not isinstance(self.keyterms_prompt, Unset):
            keyterms_prompt = self.keyterms_prompt

        prompt: None | str | Unset
        if isinstance(self.prompt, Unset):
            prompt = UNSET
        else:
            prompt = self.prompt

        one_off_keyterms: list[str] | Unset = UNSET
        if not isinstance(self.one_off_keyterms, Unset):
            one_off_keyterms = self.one_off_keyterms

        one_off_prompt: None | str | Unset
        if isinstance(self.one_off_prompt, Unset):
            one_off_prompt = UNSET
        else:
            one_off_prompt = self.one_off_prompt

        dictionary_ids: list[str] | Unset = UNSET
        if not isinstance(self.dictionary_ids, Unset):
            dictionary_ids = self.dictionary_ids

        prompt_preset_id: None | str | Unset
        if isinstance(self.prompt_preset_id, Unset):
            prompt_preset_id = UNSET
        else:
            prompt_preset_id = self.prompt_preset_id

        expected_languages: list[str] | Unset = UNSET
        if not isinstance(self.expected_languages, Unset):
            expected_languages = self.expected_languages

        fallback_language: None | str | Unset
        if isinstance(self.fallback_language, Unset):
            fallback_language = UNSET
        else:
            fallback_language = self.fallback_language

        medical_mode = self.medical_mode

        vet_mode = self.vet_mode

        keep_disfluencies = self.keep_disfluencies

        multichannel = self.multichannel

        translation_targets: list[str] | Unset = UNSET
        if not isinstance(self.translation_targets, Unset):
            translation_targets = self.translation_targets

        auto_generate_insights: bool | None | Unset
        if isinstance(self.auto_generate_insights, Unset):
            auto_generate_insights = UNSET
        else:
            auto_generate_insights = self.auto_generate_insights

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language_code is not UNSET:
            field_dict["language_code"] = language_code
        if speaker_detection is not UNSET:
            field_dict["speaker_detection"] = speaker_detection
        if keyterms_prompt is not UNSET:
            field_dict["keyterms_prompt"] = keyterms_prompt
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if one_off_keyterms is not UNSET:
            field_dict["one_off_keyterms"] = one_off_keyterms
        if one_off_prompt is not UNSET:
            field_dict["one_off_prompt"] = one_off_prompt
        if dictionary_ids is not UNSET:
            field_dict["dictionary_ids"] = dictionary_ids
        if prompt_preset_id is not UNSET:
            field_dict["prompt_preset_id"] = prompt_preset_id
        if expected_languages is not UNSET:
            field_dict["expected_languages"] = expected_languages
        if fallback_language is not UNSET:
            field_dict["fallback_language"] = fallback_language
        if medical_mode is not UNSET:
            field_dict["medical_mode"] = medical_mode
        if vet_mode is not UNSET:
            field_dict["vet_mode"] = vet_mode
        if keep_disfluencies is not UNSET:
            field_dict["keep_disfluencies"] = keep_disfluencies
        if multichannel is not UNSET:
            field_dict["multichannel"] = multichannel
        if translation_targets is not UNSET:
            field_dict["translation_targets"] = translation_targets
        if auto_generate_insights is not UNSET:
            field_dict["auto_generate_insights"] = auto_generate_insights

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_language_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        language_code = _parse_language_code(d.pop("language_code", UNSET))

        speaker_detection = d.pop("speaker_detection", UNSET)

        keyterms_prompt = cast(list[str], d.pop("keyterms_prompt", UNSET))

        def _parse_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt = _parse_prompt(d.pop("prompt", UNSET))

        one_off_keyterms = cast(list[str], d.pop("one_off_keyterms", UNSET))

        def _parse_one_off_prompt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        one_off_prompt = _parse_one_off_prompt(d.pop("one_off_prompt", UNSET))

        dictionary_ids = cast(list[str], d.pop("dictionary_ids", UNSET))

        def _parse_prompt_preset_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prompt_preset_id = _parse_prompt_preset_id(d.pop("prompt_preset_id", UNSET))

        expected_languages = cast(list[str], d.pop("expected_languages", UNSET))

        def _parse_fallback_language(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fallback_language = _parse_fallback_language(d.pop("fallback_language", UNSET))

        medical_mode = d.pop("medical_mode", UNSET)

        vet_mode = d.pop("vet_mode", UNSET)

        keep_disfluencies = d.pop("keep_disfluencies", UNSET)

        multichannel = d.pop("multichannel", UNSET)

        translation_targets = cast(list[str], d.pop("translation_targets", UNSET))

        def _parse_auto_generate_insights(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_generate_insights = _parse_auto_generate_insights(
            d.pop("auto_generate_insights", UNSET)
        )

        create_upload_body_transcription_options_type_0 = cls(
            language_code=language_code,
            speaker_detection=speaker_detection,
            keyterms_prompt=keyterms_prompt,
            prompt=prompt,
            one_off_keyterms=one_off_keyterms,
            one_off_prompt=one_off_prompt,
            dictionary_ids=dictionary_ids,
            prompt_preset_id=prompt_preset_id,
            expected_languages=expected_languages,
            fallback_language=fallback_language,
            medical_mode=medical_mode,
            vet_mode=vet_mode,
            keep_disfluencies=keep_disfluencies,
            multichannel=multichannel,
            translation_targets=translation_targets,
            auto_generate_insights=auto_generate_insights,
        )

        create_upload_body_transcription_options_type_0.additional_properties = d
        return create_upload_body_transcription_options_type_0

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
