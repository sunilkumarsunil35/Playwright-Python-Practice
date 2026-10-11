from common.target import load

P = load("context", "problems")


def test_save_and_reuse_signed_in_state(browser, base_url, tmp_path):
    path = P.save_signed_in_state(browser, base_url, tmp_path / "tom.json")
    assert '"session"' in path.read_text()
    assert P.reuse_signed_in_state(browser, base_url, path) == "Signed in as tom"


def test_reuse_signed_in_state(browser, base_url, tmp_path):
    # A hand-made state file, so this test does not depend on the one above.
    host = base_url.split("//")[1].split(":")[0]
    state = tmp_path / "ana.json"
    state.write_text(
        '{"cookies": [{"name": "session", "value": "session-ana", "domain": "%s", "path": "/",'
        ' "expires": -1, "httpOnly": true, "secure": false, "sameSite": "Lax"}], "origins": []}' % host
    )
    assert P.reuse_signed_in_state(browser, base_url, state) == "Signed in as ana"


def test_two_users_at_once(browser, base_url):
    assert P.two_users_at_once(browser, base_url) == ("Signed in as tom", "Signed in as ana")


def test_emulate_iphone(playwright, browser, base_url):
    viewport, ua = P.emulate_iphone(playwright, browser, base_url)
    assert viewport == "390x664"
    assert "iPhone" in ua
