# faster-whisper-transcriber

`faster-whisper-transcriber` is a reusable skill for transcribing local audio or video files into:

- `transcript.md`
- `transcript_segments.tsv`

It is designed to avoid regenerating one-off Python transcription scripts. Instead, it provides a reusable `transcribe_audio.py` script plus setup and usage instructions that work for both Codex-style and Claude-style skill folders.

## Purpose

Use this skill when you want to:

- transcribe local media files with Faster-Whisper
- save transcript outputs beside the source file
- reuse a stable command-line workflow
- support knowledge-bundle or similar text-first archival workflows

Supported input examples include:

- `.m4a`
- `.mp3`
- `.wav`
- `.mp4`

## Skill contents

```text
faster-whisper-transcriber/
├─ SKILL.md
├─ README.md
├─ assets/
│  └─ transcript-header.md.tmpl
├─ references/
│  ├─ model-notes.md
│  └─ setup-and-usage.md
└─ scripts/
   ├─ install_dependencies.ps1
   ├─ install_dependencies.sh
   ├─ requirements.txt
   └─ transcribe_audio.py
```

## Requirements

Required:

- Python 3.9 or newer
- `faster-whisper`

Recommended:

- `ffmpeg` available on `PATH`

Common Python dependencies installed with `faster-whisper` include:

- `ctranslate2`
- `onnxruntime`
- `tokenizers`
- `huggingface-hub`
- `av`
- `tqdm`

## Installation

### Option 1: Install Python dependency directly

Windows:

```powershell
python -m pip install faster-whisper
```

Linux/macOS:

```bash
python3 -m pip install faster-whisper
```

### Option 2: Use the bundled installer

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install_dependencies.ps1
```

Linux/macOS:

```bash
bash scripts/install_dependencies.sh
```

### Verify installation

Windows:

```powershell
python -c "from faster_whisper import WhisperModel; print('ok')"
```

Linux/macOS:

```bash
python3 -c "from faster_whisper import WhisperModel; print('ok')"
```

Optional:

```powershell
ffmpeg -version
```

## Usage

Run the script from the skill folder or provide the full script path.

### Basic transcription

Windows:

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a
```

Linux/macOS:

```bash
python3 scripts/transcribe_audio.py /path/to/audio.m4a
```

This writes:

- `transcript.md`
- `transcript_segments.tsv`

beside the source file.

### Use a different model

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a --model base.en
```

### Auto-detect language

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a --language auto
```

### Avoid output filename collisions

```powershell
python scripts/transcribe_audio.py C:\path\to\clip1.m4a --transcript-name "{stem}.transcript.md" --segments-name "{stem}.segments.tsv"
```

### Overwrite existing outputs

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a --overwrite
```

## Default behavior

Defaults:

- model: `tiny.en`
- language: `en`
- device: `cpu`
- compute type: `int8`
- VAD filter: enabled

The generated transcript includes:

- title
- source filename
- detected language
- language probability
- UTC generation timestamp
- timestamped transcript segments

The TSV contains:

- `start`
- `end`
- `text`

## Claude compatibility

This skill is self-contained and compatible with Claude-style skill folders that use `SKILL.md`.

Example installation location:

```text
~/.claude/skills/faster-whisper-transcriber/
```

## Codex compatibility

This skill also works in a Codex skills folder such as:

```text
~/.codex/skills/faster-whisper-transcriber/
```

or in a project-local `Skills/` directory.

## Troubleshooting

- If `faster_whisper` import fails, install or reinstall dependencies.
- If transcription is slow on first run, the model may still be downloading.
- If a file already exists, use `--overwrite` or change output names.
- If compressed media does not decode, check `ffmpeg`.

## References

See:

- `SKILL.md`
- `references/setup-and-usage.md`
- `references/model-notes.md`
