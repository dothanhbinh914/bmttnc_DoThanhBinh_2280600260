class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        if not key:
            raise ValueError("Key cannot be empty")
        
        # Replace J with I and convert to uppercase
        key = key.replace("J", "I").upper()
        # Remove duplicates while preserving order
        seen = set()
        key_unique = [char for char in key if not (char in seen or seen.add(char))]
        
        # Create matrix with key letters first
        matrix = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # Add unique key letters
        for char in key_unique:
            if char in alphabet and char not in matrix:
                matrix.append(char)
        
        # Add remaining alphabet letters
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        
        # Convert to 5x5 matrix
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        letter = letter.upper().replace("J", "I")
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        raise ValueError(f"Letter {letter} not found in matrix")

    def prepare_text(self, text):
        # Replace J with I, convert to uppercase, remove non-letters
        text = ''.join(char.upper() for char in text if char.isalpha()).replace("J", "I")
        # Add padding if necessary
        prepared = ""
        i = 0
        while i < len(text):
            prepared += text[i]
            if i + 1 < len(text):
                # If same letter, insert X
                if text[i] == text[i + 1]:
                    prepared += "X"
                else:
                    prepared += text[i + 1]
                    i += 1
            else:
                # If odd length, add X
                prepared += "X"
            i += 1
        return prepared

    def playfair_encrypt(self, plain_text, matrix):
        if not plain_text or not matrix:
            raise ValueError("Text and matrix cannot be empty")
        
        plain_text = self.prepare_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Same row: shift right
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Same column: shift down
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                # Rectangle: swap columns
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        if not cipher_text or not matrix:
            raise ValueError("Text and matrix cannot be empty")
        
        cipher_text = ''.join(char.upper() for char in cipher_text if char.isalpha())
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Same row: shift left
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Same column: shift up
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                # Rectangle: swap columns
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Remove padding Xs (simple approach)
        result = ""
        i = 0
        while i < len(decrypted_text):
            result += decrypted_text[i]
            if i + 2 < len(decrypted_text) and decrypted_text[i + 1] == 'X' and decrypted_text[i] == decrypted_text[i + 2]:
                i += 2  # Skip the X if it's between identical letters
            else:
                i += 1
        # Remove trailing X if present
        if result.endswith('X'):
            result = result[:-1]
        
        return result