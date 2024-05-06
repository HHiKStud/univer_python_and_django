import pytest
from task2 import merge_and_write

def test_merge_and_write():
    assert merge_and_write("file1.txt", "file2.txt", "output_file.txt") == "Hello World"
    assert merge_and_write("file12.txt", "file2.txt", "output_file.txt") == "Один из файлов не найден"

test_merge_and_write() 
