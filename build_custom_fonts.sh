#!/bin/bash
set -ue
cd "$(dirname "$0")"

if [ -z "${1:-}" ]; then
  echo "Usage: $0 <FontName>"
  echo "Example: $0 BizEmoji.ttf"
  exit 1
fi

FONT_NAME=$1
FONT_BASENAME=${FONT_NAME%.*}

if [ ! -f "font/${FONT_NAME}" ]; then
  echo "Error: Font file 'font/${FONT_NAME}' not found."
  exit 1
fi

# Ensure custom_fonts directory exists
mkdir -p custom_fonts

# Generate fonts
python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 2 12 font/${FONT_NAME} custom_fonts/001
python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 4 15 font/${FONT_NAME} custom_fonts/003
python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 7 17 font/${FONT_NAME} custom_fonts/005
python3 tools/fontgen.py pfo --extended --list codepoints.json --heightoffset 8 20 font/${FONT_NAME} custom_fonts/007

# Copy font binaries
cd custom_fonts
cp 001 002
cp 003 004
cp 005 006
cp 007 008
cd ..

# Pack the font
python3 tools/pbpack_tool.py pack pbl/${FONT_BASENAME}-ja_JP.pbl custom_fonts/*

echo "Successfully created and packed fonts into 'pbl/${FONT_BASENAME}-ja_JP.pbl'"
