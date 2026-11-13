# ai-happy-01-entry

Image entry for the make.fun **ai-happy-01** competition. `main.py` copies the
bundled `entry.png` into the output directory.

## Run

```sh
python3 main.py
```

Output defaults to `/output/entry.png`. Override the directory with
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
```

The program uses only the Python standard library, with no network access and
no randomness, so every run produces a byte-identical image.
