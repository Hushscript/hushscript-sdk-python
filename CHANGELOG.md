# Changelog

## Unreleased

### Features

* add the `vet_mode` (Veterinary mode, beta; en, en_au, en_uk, en_us, es, fr, de, de_ch; refused with `medical_mode` and in private mode) and `keep_disfluencies` (free, default off) transcription options, both echoed in the job options summary; the medical language list is synced.

### Bug Fixes

* `transcribe()` no longer forces speaker detection on when `translate_to` is set: `speakers=False` is sent as given, as the API now takes it.
* refuse a `translate_to` of more than 15 distinct targets (trimmed, lowercased) with `PreflightError` `invalid_option` before any request; the API refuses it with `invalid_transcription_options`.
* regenerate the models from the current API spec: translation targets are any base source language code (99), and jobs and transcripts carry `origin_source` and `origin_app`, jobs also `title`.

### Documentation

* README links point at the live pricing page and the SDK section of the developers page; the old `/pricing` and `/sdks` URLs redirect there.

## 1.0.0 (2026-10-13)


### Features

* initial release ([a8fd980](https://github.com/Hushscript/hushscript-sdk-python/commit/a8fd9808c04de2bc42058d70be4e633dc24f7699))


### Miscellaneous Chores

* release 1.0.0 ([911afa9](https://github.com/Hushscript/hushscript-sdk-python/commit/911afa9d956905fd917fe405eccfebd1d0d3f1c5))
