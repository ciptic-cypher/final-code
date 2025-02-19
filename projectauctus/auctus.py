import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(root, prefix='', code_dict={}):
    if root:
        if root.char is not None:
            code_dict[root.char] = prefix
        generate_huffman_codes(root.left, prefix + '0', code_dict)
        generate_huffman_codes(root.right, prefix + '1', code_dict)
    return code_dict

def huffman_encode(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    
    root = build_huffman_tree(freq_dict)
    huffman_codes = generate_huffman_codes(root)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    
    original_size = len(text) * 8  # ASCII uses 8 bits per character
    compressed_size = len(encoded_text)
    compression_ratio = original_size / compressed_size if compressed_size > 0 else 1
    
    return encoded_text, huffman_codes, root, compression_ratio

def huffman_decode(encoded_text, huffman_tree):
    decoded_text = ""
    node = huffman_tree
    for bit in encoded_text:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded_text += node.char
            node = huffman_tree
    return decoded_text

def modular_encrypt(binary_string, key):
    return ''.join(chr((ord(c) * key) % 256) for c in binary_string)

def modular_decrypt(encrypted_text, key):
    inverse_key = pow(key, -1, 256)  # Modular inverse
    return ''.join(chr((ord(c) * inverse_key) % 256) for c in encrypted_text)

def main():
    key = 53  # Encryption key
    while True:
        print("\nMenu:")
        print("1. Encode and Encrypt")
        print("2. Decrypt and Decode")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            text = input("Enter text to encode and encrypt: ")
            encoded_text, huffman_codes, huffman_tree, compression_ratio = huffman_encode(text)
            encrypted_text = modular_encrypt(encoded_text, key)
            print(f"\nHuffman Codes: {huffman_codes}")
            print(f"Encoded Binary: {encoded_text}")
            print(f"Encrypted Text: {encrypted_text}")
            print(f"Compression Ratio: {compression_ratio:.2f}")
            
        elif choice == '2':
            encrypted_text = input("Enter encrypted text: ")
            encoded_text = modular_decrypt(encrypted_text, key)
            original_text = huffman_decode(encoded_text, huffman_tree)
            print(f"\nDecrypted Binary: {encoded_text}")
            print(f"Decoded Text: {original_text}")
        
        elif choice == '3':
            break
        
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()
