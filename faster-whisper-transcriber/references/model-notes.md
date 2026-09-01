# Model notes

## Common models

- `tiny.en` — fastest, lowest accuracy, good for rough first-pass English transcription
- `base.en` — better accuracy, still relatively small
- `small.en` — slower, better accuracy again

Use English-specific `.en` models when the source is English only.

## Default choices in this skill

- model: `tiny.en`
- device: `cpu`
- compute type: `int8`
- language: `en`
- VAD filter: on

These defaults match the local workflow previously used in this workspace.

## Output naming notes

Default output names match the prior knowledge-bundle workflow:

- `transcript.md`
- `transcript_segments.tsv`

If a folder may contain multiple media files, use stem-based names:

```powershell
python scripts/transcribe_audio.py .\clip1.m4a --transcript-name "{stem}.transcript.md" --segments-name "{stem}.segments.tsv"
```

## Knowledge-bundle workflow

When used with a source folder like:

```text
corpus/raw/InterviewName/
  audio.m4a
```

The intended result is:

```text
corpus/raw/InterviewName/
  audio.m4a
  transcript.md
  transcript_segments.tsv
```

Add source metadata separately if the larger workflow requires `source.md`.
