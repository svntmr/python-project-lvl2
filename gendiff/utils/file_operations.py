from json import load


def get_json_file_content(file_path: str) -> dict:
    with open(file_path, "r") as json_file:
        file_content = load(json_file)

    return dict(file_content)
