from itertools import groupby

def string_rle(string: str) -> list:
    return [( character, len(list(group)) ) for character, group in groupby(string)]

def fancy_string_rle(string: str) -> str:
    return "".join([f"{count}{item}" for item, count in string_rle(string)])

def main():
    some_str = "11111110000000000101010000000"
    rle = string_rle(some_str)
    fancy = fancy_string_rle(some_str)
    print(rle)
    print(fancy)
    print(compression_ratio(some_str, fancy))

def compression_ratio(original: str, compressed: str) -> float:
    return len(compressed) / len(original)

if __name__ == "__main__":
    main()