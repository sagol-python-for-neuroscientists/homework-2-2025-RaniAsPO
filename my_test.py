from pathlib import Path

OUTPUT_FILE_NAME = "lorem_morse.txt"
OUTPUT_PATH = Path(__file__).parent / OUTPUT_FILE_NAME

# Replace OUTPUT_FILE_NAME with the actual file name
data = Path(OUTPUT_FILE_NAME).read_text()

dash_count = data.count("-")
dot_count = data.count(".")
newline_count = data.count("\n")

print(f"Dashes: {dash_count}, Periods: {dot_count}, Newlines: {newline_count}")