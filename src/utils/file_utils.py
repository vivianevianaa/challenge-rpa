def get_page_number(file):
    '''Returns the page number'''
    numbers = file.split("_")
    number = numbers[0]
    return number
