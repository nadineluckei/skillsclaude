#!/usr/bin/env python
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys

try:
    from faster_whisper import WhisperModel
except ImportError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "Missing dependency: faster-whisper. Install requirements from "
        "references/setup-and-usage.md."
    ) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Transcribe local audio/video files into markdown transcript and TSV "
            "segment files using Faster-Whisper."
        )
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="One or more local media files to transcribe.",
    )
    parser.add_argument(
        "--model",
        default="tiny.en",
        help="Model name to load (default: tiny.en). Examples: tiny.en, base.en, small.en.",
    )
    parser.add_argument(
        "--language",
        default="en",
        help='Language code, or "auto" for auto-detect (default: en).',
    )
    parser.add_argument(
        "--device",
        default="cpu",
        help='Inference device (default: cpu). Examples: cpu, cuda.',
    )
    parser.add_argument(
        "--compute-type",
        default="int8",
        help='Faster-Whisper compute type (default: int8). Examples: int8, float16.',
    )
    parser.add_argument(
        "--beam-size",
        type=int,
        default=5,
        help="Beam size for decoding (default: 5).",
    )
    parser.add_argument(
        "--transcript-name",
        default="transcript.md",
        help=(
            'Output transcript filename pattern (default: "transcript.md"). '
            'Supports {stem}.'
        ),
    )
    parser.add_argument(
        "--segments-name",
        default="transcript_segments.tsv",
        help=(
            'Output segment TSV filename pattern (default: "transcript_segments.tsv"). '
            'Supports {stem}.'
        ),
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Optional transcript title. Defaults to the media stem.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output files if they already exist.",
    )
    parser.add_argument(
        "--no-vad",
        action="store_true",
        help="Disable VAD filtering (enabled by default).",
    )
    parser.add_argument(
        "--header-template",
        default=None,
        help="Optional path to a custom markdown header template.",
    )
    return parser.parse_args()


def default_template_path() -> Path:
    return Path(__file__).resolve().parent.parent / "assets" / "transcript-header.md.tmpl"


def resolve_output_name(pattern: str, audio_path: Path) -> Path:
    filename = pattern.format(stem=audio_path.stem)
    return audio_path.with_name(filename)


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def load_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_outputs(
    audio_path: Path,
    transcript_path: Path,
    segments_path: Path,
    title: str,
    info,
    segments,
    template_text: str,
) -> None:
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    with transcript_path.open("w", encoding="utf-8", newline="\n") as transcript_file, \
        segments_path.open("w", encoding="utf-8", newline="\n") as segments_file:
        transcript_file.write(
            template_text.format(
                title=title,
                source_audio=audio_path.name,
                detected_language=info.language,
                language_probability=f"{info.language_probability:.4f}",
                generated_at=generated_at,
            )
        )
        segments_file.write("start\tend\ttext\n")

        for segment in segments:
            text = segment.text.strip()
            if not text:
                continue
            transcript_file.write(
                f"[{segment.start:08.2f} - {segment.end:08.2f}] {text}\n\n"
            )
            segments_file.write(f"{segment.start:.2f}\t{segment.end:.2f}\t{text}\n")


def main() -> int:
    args = parse_args()

    header_template_path = Path(args.header_template) if args.header_template else default_template_path()
    if not header_template_path.exists():
        raise SystemExit(f"Header template not found: {header_template_path}")

    language = None if args.language.lower() == "auto" else args.language
    model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)
    template_text = load_template(header_template_path)

    for raw_input in args.inputs:
        audio_path = Path(raw_input).expanduser().resolve()
        if not audio_path.exists():
            raise SystemExit(f"Input file not found: {audio_path}")
        if not audio_path.is_file():
            raise SystemExit(f"Input path is not a file: {audio_path}")

        transcript_path = resolve_output_name(args.transcript_name, audio_path)
        segments_path = resolve_output_name(args.segments_name, audio_path)

        if not args.overwrite:
            for output in (transcript_path, segments_path):
                if output.exists():
                    raise SystemExit(
                        f"Refusing to overwrite existing file without --overwrite: {output}"
                    )

        ensure_parent(transcript_path)
        ensure_parent(segments_path)

        segments, info = model.transcribe(
            str(audio_path),
            language=language,
            vad_filter=not args.no_vad,
            beam_size=args.beam_size,
        )
        write_outputs(
            audio_path=audio_path,
            transcript_path=transcript_path,
            segments_path=segments_path,
            title=args.title or audio_path.stem,
            info=info,
            segments=segments,
            template_text=template_text,
        )
        print(transcript_path)
        print(segments_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
