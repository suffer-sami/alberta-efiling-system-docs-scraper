import csv
import json
import sys

input_csv = sys.argv[1]
output_jsonl = sys.argv[2]

with open(input_csv, 'r') as csv_file, open(output_jsonl, 'w') as jsonl_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        jsonl_file.write(json.dumps(row) + '\n')
