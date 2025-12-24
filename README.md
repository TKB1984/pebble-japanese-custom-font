# Unofficial japanese language pack and tools for Pebble Time

**Coution: This language pack is unofficial and no warranty.**

Font set generated from Morisawa Inc. BIZ UDPGothic (SIL Open Font License, Version 1.1).

- https://fonts.google.com/specimen/BIZ+UDPGothic/license

## Project Structure

- `tools/`: Font generation and packing tools.
- `cps/`: Scripts and data for generating the `codepoints.json` definition.
- `font/`: Source font files.
- `po/`: Language translation files.

## Codepoint Generation

This project now uses a modular approach to generate `codepoints.json`. The scripts are located in the `cps/` directory.

### 1. Generate Base Codepoints
Generates common Japanese ranges (Hiragana, Katakana, Symbols, etc.).
```bash
python3 cps/generate_base_cps.py
```
Outputs: `cps/base_cps.json`

### 2. Generate Kanji Codepoints
Converts `kanji.txt` (list of characters) to JSON format.
```bash
python3 cps/kanji_to_json.py
```
Outputs: `cps/kanji_cps.json`

### 3. Generate/Extract Emoji Codepoints
(Emoji generation scripts like `extract_wiki_emojis.py` can be used to generate `emoji_cps.json` if needed)

### 4. Merge Codepoints
Merges the base, kanji, and emoji definitions into the final `codepoints.json`.
```bash
python3 cps/merge_cps.py
```
Outputs: `codepoints.json` (in the project root)

## Generate Menu translation file
Generate Menu translation file.
```bash
msgfmt po/ja.po -o custom_fonts/000
```
Outputs: `custom_fonts/000`

## Build Example

```bash
# set tools path
export PEBBLE_SDK_PATH=/path/to/tools

# generate font file.

## 001/002 for height 14. offset is 2.
$ python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 2 12 font/BIZUDGothic-Regular.ttf custom_fonts/001

## 003/004 for height 18. offset is 4
$ python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 4 14 font/BIZUDGothic-Regular.ttf custom_fonts/003

## 005/006 for height 24. offset is 7
$ python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 7 17 font/BIZUDGothic-Regular.ttf custom_fonts/005

## 007/008 for height 28. offset is 8
$ python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 8 20 font/BIZUDGothic-Regular.ttf custom_fonts/007

# packing

$ python3 tools/pbpack_tool.py pack pbl/BIZUDGothic-ja_JP.pbl custom_font/*
```

## Reference and thanks!!
 - https://github.com/polyfusia/pebble-japanese-custom-font ( original project)
- https://github.com/xndcn/pebble-firmware-utils
- https://orange-factory.com/sample/utf8/code3/e3.html

## Contact
 - https://x.com/wadabori
 - https://www.texpress.co.jp/