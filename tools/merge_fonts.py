#!/usr/bin/env python3
import sys
import argparse
from fontTools.merge import Merger

def main():
    parser = argparse.ArgumentParser(description="Merge multiple font files into one.")
    parser.add_argument("-o", "--output", required=True, help="Output font file path")
    parser.add_argument("inputs", nargs="+", help="Input font files")
    
    args = parser.parse_args()
    
    print(f"Merging {len(args.inputs)} fonts into {args.output}...")
    try:
        merger = Merger()
        font = merger.merge(args.inputs)
        font.save(args.output)
        print("Done.")
    except Exception as e:
        print(f"Error merging fonts: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
