import zipfile

from common.target import load

P = load("project", "problems")


def test_todo_journey(page, base_url):
    assert P.todo_journey(page, base_url) == (["Buy milk"], "1 item left")


def test_todo_filters(page, base_url):
    assert P.todo_filters(page, base_url) == (["A", "C"], ["B"])


def test_record_trace(browser, base_url, tmp_path):
    path = P.record_trace(browser, base_url, tmp_path / "trace.zip")
    assert zipfile.is_zipfile(path)


def test_record_video(browser, base_url, tmp_path):
    path = P.record_video(browser, base_url, tmp_path)
    assert path.suffix == ".webm"
    assert path.stat().st_size > 0
