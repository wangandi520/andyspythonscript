import re

def merge_crlf_before_chinese(text: str) -> str:
    return re.sub(r'\r\n(?=[\u4e00-\u9fff])', '', text)


def merge_file_crlf_before_chinese(path: str, encoding: str = 'utf-8') -> None:
    with open(path, 'r', encoding=encoding, newline='') as f:
        text = f.read()
    new_text = merge_crlf_before_chinese(text)
    if new_text != text:
        with open(path, 'w', encoding=encoding, newline='') as f:
            f.write(new_text)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python 1.py <path>')
        sys.exit(1)
    merge_file_crlf_before_chinese(sys.argv[1])
