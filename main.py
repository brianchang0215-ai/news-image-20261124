#!/usr/bin/env python3
"""Write the 24 November 2026 front-page image to /output/entry.png.

No network. Standard library only. Running this program twice writes
the same bytes both times: it decodes the bundled base64 image
(entry.png.b64, the base64 form of the 1024x1024 PNG) and writes the
decoded bytes verbatim. The image itself is stored as text so the
repository holds only UTF-8 files.
"""

import base64
import hashlib
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png.b64"
    if not source.is_file():
        source = Path.cwd() / "entry.png.b64"
    data = base64.b64decode(source.read_text(), validate=True)
    try:
        dest_dir = Path("/output")
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / "entry.png"
    except OSError:
        dest_dir = here / "output"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / "entry.png"
    dest.write_bytes(data)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    print(f"wrote {dest} ({dest.stat().st_size} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
