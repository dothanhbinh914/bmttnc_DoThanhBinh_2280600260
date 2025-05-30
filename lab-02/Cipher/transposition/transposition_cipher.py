class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        if key <= 1:
            return text
            
        encrypted_text = ''
        # Iterate through each column
        for col in range(key):
            pointer = col
            # Add characters from each column with step size of key
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    
    def decrypt(self, text, key):
        if key <= 1:
            return text
            
        # Calculate number of rows needed
        num_rows = (len(text) + key - 1) // key
        # Calculate number of columns in the last row
        num_last_row_cols = len(text) % key if len(text) % key != 0 else key
        
        # Initialize grid
        grid = [[''] * num_rows for _ in range(key)]
        pos = 0
        
        # Fill the grid column by column
        for col in range(key):
            # Determine how many rows to fill in this column
            rows_to_fill = num_rows if col < num_last_row_cols else num_rows - 1
            for row in range(rows_to_fill):
                if pos < len(text):
                    grid[col][row] = text[pos]
                    pos += 1
        
        # Read the grid row by row to get decrypted text
        decrypted_text = ''
        for row in range(num_rows):
            for col in range(key):
                if grid[col][row]:
                    decrypted_text += grid[col][row]
                    
        return decrypted_text