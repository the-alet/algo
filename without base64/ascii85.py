import sys

def encode_ascii85(data):
    encoded = []
    padding = 0

    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        if len(chunk) < 4:
            padding = 4 - len(chunk)
            chunk += b'\x00' * padding

        value = int.from_bytes(chunk, 'big')
        if value == 0 and padding == 0:
            encoded.append('z')
            continue

        for _ in range(5):
            encoded.append(chr((value % 85) + 33))
            value = value // 85

    if padding:
        encoded = encoded[:-padding]

    return ''.join(encoded)

def decode_ascii85(data):
    decoded = []
    value = 0
    count = 0

    for char in data:
        if char == 'z':
            if count != 0:
                raise ValueError("Invalid 'z' in ASCII85 data")
            decoded.extend(b'\x00\x00\x00\x00')
            continue

        if char < '!' or char > 'u':
            raise ValueError("Invalid character in ASCII85 data")

        value = value * 85 + (ord(char) - 33)
        count += 1

        if count == 5:
            decoded.extend(value.to_bytes(4, 'big'))
            value = 0
            count = 0

    if count > 0:
        if count == 1:
            raise ValueError("Invalid length of ASCII85 data")
        value = value * (85 ** (5 - count))
        decoded.extend(value.to_bytes(4, 'big')[:count-1])

    return bytes(decoded)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        # Декодирование
        input_data = sys.stdin.read().replace('\n', '')
        try:
            decoded_data = decode_ascii85(input_data)
            sys.stdout.buffer.write(decoded_data)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Кодирование
        input_data = sys.stdin.buffer.read()
        encoded_data = encode_ascii85(input_data)
        print(encoded_data)

if __name__ == "__main__":
    main()