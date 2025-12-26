
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_A = os.path.join(SCRIPT_DIR, "base_cps.json")
FILE_B = os.path.join(SCRIPT_DIR, "kanji_cps.json")
FILE_C = os.path.join(SCRIPT_DIR, "emoji_cps.json")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "../codepoints.json")

def load_json(path):
    if not os.path.exists(path):
        print(f"Error: {path} not found.")
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def main():
    print(f"Merging {FILE_A}, {FILE_B}, and {FILE_C} into {OUTPUT_FILE}...")
    
    data_a = load_json(FILE_A)
    data_b = load_json(FILE_B)
    data_c = load_json(FILE_C)
    
    codepoints = {}
    
    if 'codepoints' in data_a:
        codepoints.update(data_a['codepoints'])
        print(f"Loaded {len(data_a['codepoints'])} codepoints from {FILE_A}")
    
    if 'codepoints' in data_b:
        codepoints.update(data_b['codepoints'])
        print(f"Loaded {len(data_b['codepoints'])} codepoints from {FILE_B}")
        
    if 'codepoints' in data_c:
        codepoints.update(data_c['codepoints'])
        print(f"Loaded {len(data_c['codepoints'])} codepoints from {FILE_C}")
        
    # Sort
    sorted_items = sorted(codepoints.items(), key=lambda item: int(item[0]))
    merged_data = {"codepoints": dict(sorted_items)}
    
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, indent=2, ensure_ascii=False)
        print(f"Successfully generated {OUTPUT_FILE}")
        print(f"Total merged codepoints: {len(sorted_items)}")
    except Exception as e:
        print(f"Error writing output: {e}")

if __name__ == "__main__":
    main()
