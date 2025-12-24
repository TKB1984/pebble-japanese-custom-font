
import json
import os

INPUT_FILE = "kanji.txt"
OUTPUT_FILE = "kanji_cps.json"

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    codepoints_map = {}
    total_chars = 0
    
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for char in content:
            # Skip whitespace/newlines
            if char.strip() == "":
                continue
                
            code = ord(char)
            s_code = str(code)
            codepoints_map[s_code] = s_code
            total_chars += 1
            
    except Exception as e:
        print(f"Error reading input: {e}")
        return

    # Sort
    sorted_items = sorted(codepoints_map.items(), key=lambda item: int(item[0]))
    data = {"codepoints": dict(sorted_items)}
    
    print(f"Writing {OUTPUT_FILE}...")
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully generated {OUTPUT_FILE}")
        print(f"Total separate characters: {len(sorted_items)}")
    except Exception as e:
        print(f"Error writing output: {e}")

if __name__ == "__main__":
    main()
