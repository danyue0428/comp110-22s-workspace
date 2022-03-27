"""Utility Functions."""

__author__ = "730490913"

from csv import DictReader

def read_csv_rows(filename: str) ->list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding = "utf8")
    
    csv_reaser = DictReader(file_handle)
    
    for row in csv_reader:
        result.append(row)
    
    file_handle.close()
    return result
    
    
    
    
def column_values(rows: list[dict[str, str]], name_of_column: str)) -> list[str]:
    rows: dict[str] = {}
    column_values.append(name_of_column)
    
    