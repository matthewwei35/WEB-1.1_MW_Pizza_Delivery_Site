import json

dictionary = {
  "key":"value"
}

dictionary_joke = {
  "type": "success",
  "value": {
    "id": 493,
    "joke": "Chuck Norris can binary search unsorted data.",
    "categories": ["nerdy"]
  }
}

with open('example_obj.json', 'w') as outfile:
  json.dump(dictionary_joke, outfile, indent=4)
