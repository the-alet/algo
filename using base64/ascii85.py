import sys
import base64

def encode_ascii85():
    data = sys.stdin.buffer.read()
    encoded = base64.a85encode(data, adobe=False)
    sys.stdout.buffer.write(encoded + b'\n')

def decode_ascii85():
    try:
        data = sys.stdin.buffer.read()
        decoded = base64.a85decode(data, adobe=False)
        sys.stdout.buffer.write(decoded)
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == "-e":
        encode_ascii85()
    elif sys.argv[1] == "-d":
        decode_ascii85()
    else:
        print("Usage: ascii85.py [-e | -d]", file=sys.stderr)
        sys.exit(1)
