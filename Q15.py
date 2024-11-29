def char_in_text(text, char):
    if not text:
        return 0
    elif text[0] == char:
        return 1 + char_in_text(text[1:], char)
    else:
        return char_in_text(text[1:], char)

print(char_in_text("banana", "a"))  # Saída: 3
print(char_in_text("auditorio", "o"))  # Saída: 3