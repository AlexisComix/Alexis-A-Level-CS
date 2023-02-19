from itertools import groupby as b;f=lambda s:"".join([f"{i}{j}"for i,j in[(c,len(list(g)))for c,g in b(s)]])

# TESTS
def main():
    some_str = "11111110000000000101010000000"
    fancy = f(some_str)
    print(fancy)
    print(compression_ratio(some_str, fancy))

def compression_ratio(original: str, compressed: str) -> float:
    return len(compressed) / len(original)

if __name__ == "__main__":
    main()