
import json
import os

UTF8_RANGES_HEX = [
    ("0xE291A0", "0xE293BF"), # 丸文字・記号
    ("0xE38080", "0xE380BF"), # 記号及び句読点
    ("0xE38180", "0xE383BF"), # 全角ひらがな・カタカナ
    ("0xE387B0", "0xE387BF"), # 片仮名拡張
    ("0xE38880", "0xE38BBE"), # 囲みCJK文字・月
    ("0xE38C80", "0xE38FBF"), # CJK互換用文字
    ("0xEFBC81", "0xEFBE9F"), # 全角英数字、半角カナ
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(SCRIPT_DIR, "base_cps.json")

def hex_to_codepoint(hex_str):
    # Remove 0x prefix
    clean_hex = hex_str.lower().replace("0x", "")
    
    try:
        b = bytes.fromhex(clean_hex)
        # Attempt to decode as utf-8
        char = b.decode("utf-8")
        
        # If it decoded to exactly one character, use it as a UTF-8 character
        if len(char) == 1:
            return ord(char)
        else:
            # If it decoded to multiple characters (e.g. 004E00 -> \0N\0),
            # or if it's not a single UTF-8 char, assume it represents a raw integer codepoint value.
            return int(clean_hex, 16)
            
    except Exception:
        # If decode failed or bytes conversion failed (e.g. odd length), use raw int value
        return int(clean_hex, 16)


def main():
    codepoints_map = {}
    
    for start_hex, end_hex in UTF8_RANGES_HEX:
        try:
            start_cp = hex_to_codepoint(start_hex)
            end_cp = hex_to_codepoint(end_hex)
            
            print(f"Adding range: {start_hex} -> {end_hex} (U+{start_cp:04X} -> U+{end_cp:04X})")
            
            for cp in range(start_cp, end_cp + 1):
                s_cp = str(cp)
                codepoints_map[s_cp] = s_cp
                
        except Exception as e:
            print(f"Error processing range {start_hex}-{end_hex}: {e}")
            
    # Sort by integer key for nicer output
    sorted_items = sorted(codepoints_map.items(), key=lambda item: int(item[0]))
    data = {"codepoints": dict(sorted_items)}
    
    try:
        with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully generated {OUTPUT_JSON}")
        print(f"Total codepoints: {len(codepoints_map)}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
