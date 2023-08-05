import urllib.request as urllib  # import module to check for url connectivity


def main(url):  # function to check for connectivity
    print("Checking connectivity ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code was: ", response.getcode())  # code to get response code


print("This is a URL connectivity checker")
input_url = (input("What is the url you want to check?: "))

main(input_url)
