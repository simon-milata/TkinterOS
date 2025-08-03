from string import punctuation

from tkinteros.file_management.file_manager import FileManager


def test_start_with_special_character():
    for char in punctuation:
        file_name = char + "a"
        assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is False


def test_start_less_than_2_characters():
    file_name = "a" + punctuation * 2
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is False


def test_file_already_exists():
    file_name = "text_file.txt"
    files = ["passwords.txt", file_name, "notes.txt"]
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=files) is False


def test_name_too_long():
    file_name = "a" * 50
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is False


def test_name_too_short():
    file_name = "a"
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is False


def test_base_name_too_short():
    file_name = "a.txt"
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is False


def test_name_starts_with_number():
    file_name = "4A.txt"
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is True


def test_name_numbers_only():
    file_name = "2002"
    assert FileManager().validate_file_name_on_creation(file_name=file_name, files=[]) is True