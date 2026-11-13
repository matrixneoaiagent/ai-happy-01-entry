import os, shutil
from pathlib import Path

# Copy the bundled image byte-for-byte into the requested output directory.
src = Path(__file__).with_name("entry.png")
outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
outdir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, outdir / "entry.png")
print(outdir / "entry.png")
