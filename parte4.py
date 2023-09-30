import requests


def solicitar_api(url):
    url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
        return None
