# Changelog

## Unreleased

### Features

* add the `vet_mode` (Veterinary mode, beta; en, en_au, en_uk, en_us, es, fr, de, de_ch; refused with `medical_mode` and in private mode) and `keep_disfluencies` (free, default off) transcription options, both echoed in the job options summary; the medical language list is synced.

### Bug Fixes

* sync `openapi.json` with the production spec (`translation_targets` loses `maxItems`: the API counts the 15-target cap after dedup, as the preflight already does) and pin the conformance suite to `v1.1.0`.
* `transcribe()` no longer forces speaker detection on when `translate_to` is set: `speakers=False` is sent as given, as the API now takes it.
* refuse a `translate_to` of more than 15 distinct targets (trimmed, lowercased) with `PreflightError` `invalid_option` before any request; the API refuses it with `invalid_transcription_options`.
* regenerate the models from the current API spec: translation targets are any base source language code (99), and jobs and transcripts carry `origin_source` and `origin_app`, jobs also `title`.

### Documentation

* README links point at the live pricing page and the SDK section of the developers page; the old `/pricing` and `/sdks` URLs redirect there.

## [1.2.0](https://github.com/Hushscript/hushscript-sdk-python/compare/v1.1.2...v1.2.0) (2026-11-27)


### Bug Fixes

* compare the language for medical and vet as the api normalizes it ([6dcc30f](https://github.com/Hushscript/hushscript-sdk-python/commit/6dcc30fdf34b5c9a6b1bdb9462e69f088a5a777c))
* send speaker_detection as given with translations, cap translate_to at 15 targets, regenerate from current spec ([ec679f8](https://github.com/Hushscript/hushscript-sdk-python/commit/ec679f8fa86a2c54f791663ad971dbcded7fe1b0))
* sync the api spec with production and pin conformance v1.1.0 ([0b19c62](https://github.com/Hushscript/hushscript-sdk-python/commit/0b19c62ced48bcade817e121cf9e862d568868f2))

## [1.1.2](https://github.com/Hushscript/hushscript-sdk-python/compare/v1.1.1...v1.1.2) (2026-11-09)


### Miscellaneous Chores

* release 1.1.2 ([d101668](https://github.com/Hushscript/hushscript-sdk-python/commit/d101668023c8eb97fdcda9aa4851f13facf3d026))

## [1.1.1](https://github.com/Hushscript/hushscript-sdk-python/compare/v1.1.0...v1.1.1) (2026-10-31)


### Bug Fixes

* **deps:** update dependencies to latest ([f74c0d8](https://github.com/Hushscript/hushscript-sdk-python/commit/f74c0d8ab32ed86d50345c4b3b453f87dde15e47))

## [1.1.0](https://github.com/Hushscript/hushscript-sdk-python/compare/v1.0.0...v1.1.0) (2026-10-23)


### Features

* sync with the api spec ([801a89e](https://github.com/Hushscript/hushscript-sdk-python/commit/801a89e899d962ef4d551b34503593ab48d1c3df))

## 1.0.0 (2026-10-13)


### Features

* initial release ([a8fd980](https://github.com/Hushscript/hushscript-sdk-python/commit/a8fd9808c04de2bc42058d70be4e633dc24f7699))


### Miscellaneous Chores

* release 1.0.0 ([911afa9](https://github.com/Hushscript/hushscript-sdk-python/commit/911afa9d956905fd917fe405eccfebd1d0d3f1c5))
