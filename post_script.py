import requests


url = "https://ml-fastapi-test.onrender.com/infer"

response = requests.post(
    url,
    json={
            "age": 31,
            "workclass": "Local-gov",
            "fnlgt": 189265,
            "education": "HS-grad",
            "education_num": 9,
            "marital_status": "Never-married",
            "occupation": "Adm-clerical",
            "relationship": "Not-in-family",
            "race": "White",
            "sex": "Male",
            "capital_gain": 20000,
            "capital_loss": 0,
            "hours_per_week": 45,
            "native_country": "United-States",
        }
)

print(f"Status code : {response.status_code}")
print(f"Result: {response.content}")
