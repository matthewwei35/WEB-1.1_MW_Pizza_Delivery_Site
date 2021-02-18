import requests

# A text-based response object
result1 = requests.get("http://127.0.0.1:3000/")
print("base result 1 print out === ", result1)

result1_text = result1.text
print(result1_text)

# A json-based response object
result2 = requests.get("http://127.0.0.1:3000/json-example")
print("base result 2 print out === ", result2)

result2_json = result2.json()
print(result2_json)
