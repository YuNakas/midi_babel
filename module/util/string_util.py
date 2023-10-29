import re

def get_filename(strings: list[str], extension: str) -> list[str]:
    """特定の拡張子のファイル名を取り出す

    Args:
        strings (list[str]): ファイル名の配列
        extension (str): 取り出し対象の拡張子

    Returns:
        特定の拡張子のファイル名
    """

    rtnList = []
    for string in strings: 
        match = re.search(r"\." + extension + "$", string)
        if match:
            rtnList.append(string)
            
    return rtnList