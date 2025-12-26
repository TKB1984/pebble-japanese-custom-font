# Unofficial japanese language pack and tools for Pebble Time

**Coution: This language pack is unofficial and no warranty.**

Font set generated from BIZ UDPGothic (https://fonts.google.com/specimen/BIZ+UDPGothic/about) and Noto Emoji (https://fonts.google.com/specimen/Noto+Emoji/about)

## Project Structure

- `tools/`: Font generation and packing tools.
- `cps/`: Scripts and data for generating the `codepoints.json` definition.
- `font/`: Source font files.
- `po/`: Language translation files.
- `custom_fonts/`: Custom font files.
- `pbl/`: Generated language pack files.

## Setup
```bash
git clone https://github.com/TKB1984/pebble-japanese-custom-font
cd pebble-japanese-custom-font
python3 -m venv pebble-font
source pebble-font/bin/activate
pip install -r requirements.txt
```

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
bash build_custom_fonts.sh BizEmoji.ttf
```

## Reference and thanks!!
 - https://github.com/polyfusia/pebble-japanese-custom-font ( original project)
 - https://github.com/xndcn/pebble-firmware-utils
 - https://gist.github.com/medicalwei/c9fdcd9ec19b0c363ec1
 - https://ja.wikipedia.org/wiki/Unicode%E3%81%AEEmoji%E3%81%AE%E4%B8%80%E8%A6%A7
 - https://x0213.org/joyo-kanji-code/
 - https://orange-factory.com/dnf/utf-8.html

## Contact
 - https://x.com/wadabori
 - https://www.texpress.co.jp/