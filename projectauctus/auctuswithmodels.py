import heapq
from collections import defaultdict
import zlib

def huffman_encode(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1
    
    heap = [[weight, [char, ""]] for char, weight in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huffman_dict = dict(heapq.heappop(heap)[1:])
    encoded_text = ''.join(huffman_dict[char] for char in text)
    return encoded_text, huffman_dict

def huffman_decode(encoded_text, huffman_dict):
    reversed_dict = {v: k for k, v in huffman_dict.items()}
    temp = ""
    decoded_text = ""
    for bit in encoded_text:
        temp += bit
        if temp in reversed_dict:
            decoded_text += reversed_dict[temp]
            temp = ""
    return decoded_text

def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    current = ""
    compressed_data = []
    code = 256
    
    for char in text:
        temp = current + char
        if temp in dictionary:
            current = temp
        else:
            compressed_data.append(dictionary[current])
            dictionary[temp] = code
            code += 1
            current = char
    
    if current:
        compressed_data.append(dictionary[current])
    return compressed_data

def lzw_decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}
    current = chr(compressed_data.pop(0))
    result = current
    code = 256
    
    for data in compressed_data:
        entry = dictionary.get(data, current + current[0])
        result += entry
        dictionary[code] = current + entry[0]
        code += 1
        current = entry
    return result

def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

def main():
    while True:
        print("\nMenu:")
        print("1. Encode and Encrypt")
        print("2. Decrypt and Decode")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            text = input("Enter text to encode and encrypt: ")
            huffman_encoded, huffman_dict = huffman_encode(text)
            lzw_compressed = lzw_compress(huffman_encoded)
            key = int(input("Enter encryption key (integer 0-255): "))
            encrypted_data = xor_encrypt_decrypt(bytes(lzw_compressed), key)
            
            original_size = len(text) * 8
            compressed_size = len(encrypted_data) * 8
            compression_ratio = original_size / compressed_size if compressed_size > 0 else 1
            compression_percentage = (1 - (compressed_size / original_size)) * 100
            
            print(f"\nHuffman Codes: {huffman_dict}")
            print(f"LZW Compressed: {lzw_compressed}")
            print(f"Encrypted Data: {encrypted_data}")
            print(f"Compression Ratio: {compression_ratio:.2f}")
            print(f"Compression Percentage: {compression_percentage:.2f}%")
            
        elif choice == '2':
            encrypted_data = input("Enter encrypted data: ")
            key = int(input("Enter decryption key: "))
            decrypted_data = xor_encrypt_decrypt(eval(encrypted_data), key)
            lzw_decompressed = lzw_decompress(list(decrypted_data))
            decoded_text = huffman_decode(lzw_decompressed, huffman_dict)
            
            print(f"\nDecoded Text: {decoded_text}")
            
        elif choice == '3':
            break
        else:
            print("Invalid option, try again!")

if __name__ == "__main__":
    main()