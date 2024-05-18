import requests

def main():
    send_line("Image Send", "test.jpg", api_file="config/line.txt")

def import_key(path="config/line.txt"):
    f = open(path, 'r', encoding='UTF-8')
    key = f.read()
    f.close()
    return key

def send_line(message, file_path=None, api_key=None, api_file=None):
    if api_key is None and api_file is None:
        raise ValueError("Need api_key or api_key_file. \n Prepare api key.")
    if api_file is not None:
        line_notify_token = import_key(file_path=api_file)
    if api_key is not None:
        line_notify_token = api_key

    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': message}

    if(file_path is None):
        requests.post(line_notify_api, headers = headers, data = data)
    else:
        files = {'imageFile': open(file_path, "rb")}
        requests.post(line_notify_api, data=data, headers=headers, files=files)


if __name__ == "__main__":
    main()