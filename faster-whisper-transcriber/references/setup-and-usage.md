# Setup and usage

## Dependencies

Required:

- Python 3.9 or newer
- `faster-whisper`

Recommended:

- `ffmpeg` on `PATH` so common media formats such as `.m4a`, `.mp3`, `.mp4`, and `.wav` decode reliably

Typical Python packages pulled in by `faster-whisper`:

- `ctranslate2`
- `onnxruntime`
- `tokenizers`
- `huggingface-hub`
- `av`
- `tqdm`

## Install on a new machine

Install Python package:

```powershell
python -m pip install faster-whisper
```

Or use the bundled helper:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\install_dependencies.ps1
```

Linux or macOS:

```bash
bash scripts/install_dependencies.sh
```

Optional: verify import works:

```powershell
python -c "from faster_whisper import WhisperModel; print('ok')"
```

Linux or macOS:

```bash
python3 -c "from faster_whisper import WhisperModel; print('ok')"
```

Optional: verify ffmpeg exists:

```powershell
ffmpeg -version
```

## Human command-line invocation

Run from the skill folder or provide the full script path.

Transcribe one file with defaults:

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a
```

Linux or macOS:

```bash
python3 scripts/transcribe_audio.py /path/to/audio.m4a
```

Use a different model:

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a --model base.en
```

Auto-detect language:

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a --language auto
```

Avoid filename collisions in a folder with many media files:

```powershell
python scripts/transcribe_audio.py C:\path\to\clip1.m4a --transcript-name "{stem}.transcript.md" --segments-name "{stem}.segments.tsv"
```

Overwrite existing outputs:

```powershell
python scripts/transcribe_audio.py C:\path\to\audio.m4a --overwrite
```

## Claude compatibility

This skill is compatible with Claude-style skill folders because it is self-contained and uses `SKILL.md` as the entry file.

Typical Claude Code installation pattern:

```text
~/.claude/skills/faster-whisper-transcriber/
  SKILL.md
  scripts/
  references/
  assets/
```

After copying the folder into a Claude skills directory, invoke the same bundled script commands shown above from a terminal.

## Outputs

By default, the script writes beside the source file:

- `transcript.md`
- `transcript_segments.tsv`

The transcript contains:

- title line
- source filename
- detected language
- language probability
- UTC generation timestamp
- timestamped transcript segments

The TSV contains:

- `start`
- `end`
- `text`

## Troubleshooting

- If `faster_whisper` import fails, install or reinstall the package.
- If the first run is slow, Faster-Whisper may be downloading the model.
- If a file already exists, rerun with `--overwrite` or choose a different output name.
- If decoding fails on compressed media, install or fix `ffmpeg`.
