import heapq
import collections

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_dict = collections.Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_huffman_codes(root, prefix="", code_dict={}):
    if root:
        if root.char is not None:
            code_dict[root.char] = prefix
        build_huffman_codes(root.left, prefix + "0", code_dict)
        build_huffman_codes(root.right, prefix + "1", code_dict)
    return code_dict

def encrypt_text(text, key):
    return "".join(chr((ord(char) + key) % 256) for char in text)

def decrypt_text(text, key):
    return "".join(chr((ord(char) - key) % 256) for char in text)

def huffman_encode(text, key):
    encrypted_text = encrypt_text(text, key)
    root = build_huffman_tree(encrypted_text)
    huffman_codes = build_huffman_codes(root)
    encoded_text = "".join(huffman_codes[char] for char in encrypted_text)
    return encoded_text, root

def huffman_decode(encoded_text, root, key):
    current = root
    decoded_text = ""
    for bit in encoded_text:
        current = current.left if bit == "0" else current.right
        if current.char:
            decoded_text += current.char
            current = root
    return decrypt_text(decoded_text, key)

def calculate_compression(text, encoded_text):
    original_size = len(text) * 8  # Each character takes 8 bits in ASCII
    compressed_size = len(encoded_text)  # Encoded text is in bits
    compression_percentage = (1 - (compressed_size / original_size)) * 100
    return round(compression_percentage, 2)

def menu():
    while(1):
        key = int(input("Enter decryption key (integer): "))
        if key==0:
            break
        while True:
            print("\n1. Encode Text")
            print("2. Decode Text")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                text = input("Enter text to encode: ")
                
                encoded_text, tree = huffman_encode(text, key)
                print("Encoded Text:", encoded_text)
                
                print(f"Compression Percentage: {calculate_compression(text,encoded_text)}%")
                
            elif choice == "2":
                encoded_text = input("Enter encoded text: ")
                
                decoded_text = huffman_decode(encoded_text, tree, key)
                print("Decoded Text:", decoded_text)
                
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
