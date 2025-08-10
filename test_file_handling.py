# -*- coding: utf-8 -*-
from isConnected import loadGraph
import os

def test_valid_file():
    with open("valid.map", "w") as f:
        f.write("# Valid map file\n")
        f.write("2\n")
        f.write("A B\n")
        f.write("B C\n")
    g = loadGraph("valid.map")
    assert g.neighbours("A") == ["B"]
    assert g.neighbours("B") == ["C"]
    os.remove("valid.map")

def test_missing_file():
    try:
        loadGraph("does_not_exist.map")
    except SystemExit:
        print("Correctly exited on missing file.")

def test_bad_format():
    with open("bad.map", "w") as f:
        f.write("X Y Z\n")  # Invalid format for edge count
    try:
        loadGraph("bad.map")
    except SystemExit:
        print("Correctly exited on bad format.")
    os.remove("bad.map")

if __name__ == "__main__":
    test_valid_file()
    test_missing_file()
    test_bad_format()
    print("All file handling tests passed.")
