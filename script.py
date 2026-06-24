import json
import requests

BASE_URL = "http://[EvolutionAPI_URL_here]:8080"
API_KEY = "Evolution_API_key_here"

def send_message(instance, number, text):
    url = f"{BASE_URL}/message/sendText/{instance}"

    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "number": number,
        "text": text
    }

    return requests.post(url, headers=headers, json=payload).json()

def main():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for instance in data["instances"]:
        instance_name = instance.get("name", [])
        phone = instance.get("phone", [])

        print(f"Using instance: {instance_name}\n")

        for number in phone:
            for text in data["texts"]:
                print(f"Sending to: {number}: {text[:30]}\n")

                response = send_message(instance_name, number, text)
                print(response)

if __name__ == "__main__":
    main()