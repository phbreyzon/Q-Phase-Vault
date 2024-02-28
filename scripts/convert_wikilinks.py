import pathlib
from pathlib import Path

def convert_wikilinks_to_absolute(md_file_path, base_path):
    content = ""
    with open(md_file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "[[" in line and "]]" in line:
                # This is a very simple parser and might need to be adjusted
                start = line.find("[[") + 2
                end = line.find("]]", start)
                wikilink = line[start:end]
                absolute_path = pathlib.PurePath(base_path, wikilink).as_posix()
                line = line.replace(wikilink, absolute_path)
            content += line

    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    base_path = Path(__file__).parent.parent / "content"
    for md_file in base_path.glob("**/*.md"):
        convert_wikilinks_to_absolute(md_file, base_path)

if __name__ == "__main__":
    main()