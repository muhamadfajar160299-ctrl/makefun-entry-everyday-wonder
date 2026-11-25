"""Copy entry.txt byte-identical to $MAKEFUN_OUTPUT_DIR/entry.txt (mode 0644).

Stdlib only, no temp file: the bytes are read from the entry.txt shipped
beside this script and written straight to the output path.
"""

import os
import sys

try:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    dst = os.path.join(out_dir, "entry.txt")
except KeyError:
    print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
    raise SystemExit(1)

try:
    with open(src, "rb") as f:
        data = f.read()
except OSError as exc:
    print(f"cannot read entry.txt: {exc}", file=sys.stderr)
    raise SystemExit(1)

if not data.strip():
    print("entry.txt is empty", file=sys.stderr)
    raise SystemExit(1)

try:
    with open(dst, "wb") as f:
        f.write(data)
    os.chmod(dst, 0o644)
except OSError as exc:
    print(f"cannot write output: {exc}", file=sys.stderr)
    raise SystemExit(1)
