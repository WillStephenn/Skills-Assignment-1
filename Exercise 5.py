def break_cypher(Text):
    Transformations = []

    # Try all possible shifts (0-25)
    for shift in range(26):
        Result = ''
        Common_Letter_Count = 0

        # Process each character in the text
        for Char in Text:
            if Char.isalpha():
                # Shift character and wrap around using modulo
                Shifted_Character = (ord(Char.upper()) - ord('A') + shift) % 26 + ord('A')

                # Count occurrences of common letters: 'E', 'T', 'A', 'O', 'I'
                if Shifted_Character in (ord('E'), ord('T'), ord('A'), ord('O'), ord('I')):
                    Common_Letter_Count += 1

                Result += chr(Shifted_Character)
            else:
                Result += Char
        
        # Store the transformation and common letter count
        Transformations.append((Result, Common_Letter_Count))

    # Find the transformation with the highest count of common letters
    max_common_letter_count = 0
    best_transformation = ""
    for transformation, common_letter_count in Transformations:
        if common_letter_count > max_common_letter_count:
            max_common_letter_count = common_letter_count
            best_transformation = transformation
    
    return best_transformation

input_text = input("Enter scrambled text: ")
print(break_cypher(input_text))