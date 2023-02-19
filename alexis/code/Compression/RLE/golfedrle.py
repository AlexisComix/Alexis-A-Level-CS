from itertools import groupby;r=lambda s:[(c,len(list(g)))for c,g in groupby(s)];f=lambda s:"".join([f"{i}{j}"for i,j in r(s)]);

# TESTS
def main():
    some_str = "11111110000000000101010000000"
    rle = r(some_str)
    fancy = f(some_str)
    print(rle)
    print(fancy)
    print(compression_ratio(some_str, fancy))

def compression_ratio(original: str, compressed: str) -> float:
    return len(compressed) / len(original)

if __name__ == "__main__":
    main()