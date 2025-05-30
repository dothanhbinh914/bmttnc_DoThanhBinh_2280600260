class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1:
            return plain_text
            
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        
        # Place characters in rails
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        # Combine rails to get cipher text
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1:
            return cipher_text
            
        # Calculate length of each rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        # Count characters per rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        # Create rails with correct number of placeholders
        rails = [[] for _ in range(num_rails)]
        pos = 0
        for i in range(num_rails):
            rails[i] = list(cipher_text[pos:pos + rail_lengths[i]])
            pos += rail_lengths[i]
            
        # Reconstruct plain text
        plain_text = []
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            plain_text.append(rails[rail_index].pop(0))
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        return ''.join(plain_text)