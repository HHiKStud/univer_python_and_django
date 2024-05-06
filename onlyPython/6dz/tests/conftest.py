import pytest

@pytest.fixture(autouse=True)
def my_fixture():
    with open("file1.txt", "r") as f:
        pass

    with open("file2.txt", "r") as f:
        pass

    with open("output_file.txt", "w") as f:
        pass