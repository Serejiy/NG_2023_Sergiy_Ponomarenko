import requests

def add_urls():
    urls = []
    elmnt_num = 0
    lst_size = int(input("Enter the size of the list: "))
    for url in range(lst_size):
        elmnt_num += 1
        input_url = input(f"Enter url {elmnt_num}: ")
        urls.append(input_url)
    return urls

urls = add_urls()

start = input("Urls added to the list.\nType 'y' to start checking: ")
if start == 'y':
    print ("Processing...")
    num = 0
    status_codes = {
        200: "OK",
        201: "Created",
        202: "Accepted",
        204: "No Content",
        301: "Moved Permanently",
        302: "Found",
        304: "Not Modified",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable"
    }
    for url in urls:
        num += 1
        try:
            response = requests.get(url)
            if response.status_code in status_codes:
                print(f"The status of the {num} url: {status_codes[response.status_code]}")
            else:
                print(f"The status of the {num} url: Unknown status code")
        except requests.ConnectionError:
            print(f"The {num} url is invalid or there is no internet connection")
else:
    print("Wrong input.")




