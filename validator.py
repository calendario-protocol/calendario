
import json
import sys
from jsonschema import validate, ValidationError, Draft7Validator

SCHEMA_FILE = "calendario-schema-v0.1.json"

def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def validate_profile(profile_path):
    schema = load_json_file(SCHEMA_FILE)
    profile = load_json_file(profile_path)
    validator = Draft7Validator(schema)

    errors = sorted(validator.iter_errors(profile), key=lambda e: e.path)
    if not errors:
        print("✅ Validation successful: profile matches schema")
        return 0

    print("❌ Validation failed with the following issues:")
    for error in errors:
        path = ".".join([str(p) for p in error.absolute_path])
        print(f" - {path or 'root'}: {error.message}")
    return 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validator.py <profile-file.json>")
        sys.exit(2)

    profile_path = sys.argv[1]
    exit(validate_profile(profile_path))
