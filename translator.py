# Build a basic translator
# Giraffe language
# All vowels become g. Eg: dog -> dgg
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))
