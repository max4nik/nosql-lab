def split_class_name(class_name: str) -> str:
    new_string = ''
    for char in class_name:
        if char.islower():
            new_string += char
        else:
            new_string += f' {char}'
    return new_string
