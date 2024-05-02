alphabet = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', # Lowercase
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', # Uppercase
    'á', 'é', 'í', 'ó', 'ú', 'ü', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ü', # Accented characters
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', # 0-9
    '@', '=', ':', ';', '"', "'", ',', '<', '>', '.', '?', ' ', '¡', '¿', '\\' # Symbols
}

special_chars = {
    '*', '(', ')', '-', '=', '+', '[', ']', '|', '`', '~', '!', '\n', '\t', '/'  # Special characters, they have to be escaped e.g. \special_char
}

latex_escaped = {
    '#', '$', '%', '&', '_' # Special characters, they have to be escaped e.g. \special_char in latex
}