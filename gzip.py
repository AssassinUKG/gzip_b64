import base64
import zlib




def gzipB64_compress(file_to_compress):
    try:
        fBytes = open(file_to_compress, "rb").read()
    except Exception as e:
        print(f"Error: {e}")

    compressed = zlib.compress(fBytes)
    b64 = base64.b64encode(compressed)
    return b64


def gzipB64_uncompress(gzipb64_str):
    data = base64.b64decode(gzipb64_str)
    uncompressed = zlib.decompress(data)
    return uncompressed





fileToCompress = "/home/ac1d/Downloads/meter.elf"

comp = gzipB64_compress(fileToCompress)

print("Compressed:\n")
print(comp)

print("")

uncomp = gzipB64_uncompress(comp)

print("Uncompressed:\n")
print(uncomp)

