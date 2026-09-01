---
name: faster-whisper-transcriber
description: Transcribe local audio or video files into markdown transcripts and TSV segment files using Faster-Whisper. Use when a user wants reusable local transcription workflow instead of regenerating an inline Python snippet, especially for .m4a, .mp3, .wav, .mp4, or similar media files, and when the output should be saved beside the source file or prepared for an ICM/knowledge-bundle workflow.
---

# Faster Whisper Transcriber

Use the bundled script instead of writing ad hoc transcription code.

This skill is structured so it can be copied into either a Codex skills folder or a Claude-compatible skills folder that reads `SKILL.md`.

## Quick start

1. Confirm Python is available.
2. If dependencies are missing, read `references/setup-and-usage.md` or run one of the bundled installer scripts:
   - Windows PowerShell: `scripts/install_dependencies.ps1`
   - Linux/macOS Bash: `scripts/install_dependencies.sh`
3. Run `scripts/transcribe_audio.py` against a local media file.
4. Review the generated `transcript.md` and `transcript_segments.tsv`.

## Default behavior

- Input: one local media file path
- Model: `tiny.en`
- Device: CPU
- Compute type: `int8`
- Outputs written beside the source file:
  - `transcript.md`
  - `transcript_segments.tsv`

The script uses `assets/transcript-header.md.tmpl` for the markdown header.

## Common invocations

Transcribe one English file with defaults:

```powershell
python scripts/transcribe_audio.py path\to\audio.m4a
```

Use a larger model:

```powershell
python scripts/transcribe_audio.py path\to\audio.m4a --model base.en
```

Let Faster-Whisper auto-detect language:

```powershell
python scripts/transcribe_audio.py path\to\audio.m4a --language auto
```

Use audio-stem-based output names to avoid collisions:

```powershell
python scripts/transcribe_audio.py path\to\clip1.m4a --transcript-name "{stem}.transcript.md" --segments-name "{stem}.segments.tsv"
```

## Read these references when needed

- `references/setup-and-usage.md` — dependencies, install commands, human CLI usage, troubleshooting
- `references/model-notes.md` — model choices, output naming, and workflow notes

## Skill-specific guidance

- Prefer this script over generating a new inline Python heredoc.
- For Claude compatibility, keep the skill self-contained under one folder with `SKILL.md`, `scripts/`, `references/`, and `assets/`.
- Keep raw media outside normal Git history when possible; commit text outputs and metadata instead.
- State clearly if transcription dependencies are absent or if model download is required.
- For knowledge-bundle ingestion, store the raw source, generated transcript, and segment TSV in the same source folder unless the user asks for a different layout.
