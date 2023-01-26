def get_page_number(filename):
    """
    Returns the page number from the filename.
    """
    array_filename = filename.split("_")
    number = int(array_filename[0])
    return number
