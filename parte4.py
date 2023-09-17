import requests


def solicitar_api(url):
    try:
        response = requests.get (https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv)

       
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de solicitud: {e}")
        return None
