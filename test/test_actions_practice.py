from common.target import load

P = load("actions", "practice")


def test_double_click(page, base_url):
    assert P.double_click(page, base_url) == "Double clicked"


def test_right_click(page, base_url):
    assert P.right_click(page, base_url) == "Context menu opened"


def test_pick_fruits(page, base_url):
    assert P.pick_fruits(page, base_url, ["apple", "cherry"]) == "Fruits: apple, cherry"


def test_set_volume(page, base_url):
    assert P.set_volume(page, base_url, 75) == "75"


def test_type_slowly(page, base_url):
    assert P.type_slowly(page, base_url, "playwright") == "Characters: 10"


def test_replace_bio(page, base_url):
    assert P.replace_bio(page, base_url, "I like Python.") == "I like Python."


def test_upload_file(page, base_url, tmp_path):
    file = tmp_path / "report.txt"
    file.write_text("hello")
    assert P.upload_file(page, base_url, file) == "report.txt"


def test_drag_and_drop(page, base_url):
    assert P.drag_and_drop(page, base_url) == "Dropped: Item A"
