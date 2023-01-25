#Returns the page number
def get_page_number(file):
    numbers = file.split("_")
    number = numbers[0]
    return number