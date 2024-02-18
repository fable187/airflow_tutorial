import json

def parse_json_strings(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            dictionary[key] = parse_json_strings(value)
        elif isinstance(value, str):
            try:
                parsed_json = json.loads(value)
                if isinstance(parsed_json, dict):
                    dictionary[key] = parse_json_strings(parsed_json)
            except json.JSONDecodeError:
                pass  # Ignore strings that are not valid JSON
        # You may add more conditions here to handle other types if needed
    return dictionary

# Example usage:
input_dict = {
    "key1": '{"nested_key1": "value1", "nested_key2": "value2"}',
    "key2": '{"nested_key3": "value3"}',
    "key3": {"nested_key4": "value4"},
    "key4": "not_a_json_string",
    "key5": 123,  # Int value
    "key6": None,  # None value
    "key7": "",  # Empty string
}

parsed_dict = parse_json_strings(input_dict)
print(parsed_dict)
