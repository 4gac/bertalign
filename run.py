from bertalign import Bertalign
import argparse


def read_file_to_string(file_path) -> str:
    try:
        with open(file_path, "r") as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None


def main():
    parser = argparse.ArgumentParser(description="BertAligner")
    parser.add_argument("src", help="Source file")
    parser.add_argument("tgt", help="Target file")

    args = parser.parse_args()

    src = read_file_to_string(args.src)

    tgt = read_file_to_string(args.tgt)

    aligner = Bertalign(src, tgt)
    aligner.align_sents()

    aligner.print_sents()


if __name__ == "__main__":
    main()
