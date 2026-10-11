from common.target import load

P = load("frames", "practice")


def test_accept_confirm(page, base_url):
    assert P.accept_confirm(page, base_url) == "You pressed OK"


def test_read_popup(page, base_url):
    assert P.read_popup(page, base_url) == "button"


def test_nested_frame_text(page, base_url):
    assert P.nested_frame_text(page, base_url) == "The secret is 42"


def test_count_frames(page, base_url):
    assert P.count_frames(page, base_url) == 4


def test_download_report(page, base_url, tmp_path):
    assert P.download_report(page, base_url, tmp_path) == "name,score\ntom,90\nana,85\n"
    assert (tmp_path / "report.csv").exists()


def test_close_tab_and_return(page, base_url):
    assert P.close_tab_and_return(page, base_url) == (1, "Tabs")
