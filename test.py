"""
This module contains test cases for piff.
"""

from piff import edit_distance, read_entire_file, DiffSubcommand

def test_edit_distance():
    """Test edit_distance function"""
    assert not edit_distance([], [])

def test_read_entire_file():
    """Test read_entire_file function"""
    try:
        read_entire_file("non_existing_file.txt")
        assert False, "Exception not raised"
    except FileNotFoundError:
        assert True

def test_diff_subcommand():
    """Test DiffSubcommand class"""
    diff_subcommand = DiffSubcommand()
    assert diff_subcommand.run("program_name", ["file1.txt", "file2.txt"]) == 0
