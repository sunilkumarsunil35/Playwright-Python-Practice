# Playwright-Python-Practice: Learn Playwright with Python

A beginner-friendly study plan for browser automation with Playwright and pytest. There are 10 topics
and 104 exercises: 44 core exercises plus 60 practice exercises. Every exercise comes three ways:

- an **exercise** in `src/exercises/`, with the task in its docstring and an empty body for you to fill in
- a worked **solution** in `src/solutions/`, with comments on the API it uses
- **tests** in `test/` that check either one

Everything runs against a small practice website that ships with the repo, so the tests never depend
on the internet.

## Set up

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run the tests

```bash
sh run-tests.sh            # checks the worked solutions; everything should pass
sh run-tests.sh --mine     # checks YOUR code in src/exercises
```

On Windows without `sh`, run `python -m pytest` and `python -m pytest --mine`.

The run ends with one line per topic. With `--mine`, an exercise you haven't written yet shows as
**todo**, not as a failure:

```
------------------------------ progress by topic ------------------------------
ok   basics               5/5 passing, 0 todo, 0 failed
todo basics_practice      2/6 passing, 4 todo, 0 failed
todo locators             0/5 passing, 5 todo, 0 failed
...
```

Handy options (they go straight to pytest):

```bash
sh run-tests.sh --mine -k locators                   # one topic
sh run-tests.sh --mine -k fill_by_label              # one exercise
sh run-tests.sh --mine --headed --slowmo 500         # watch the browser do it
sh run-tests.sh --mine --tracing retain-on-failure   # keep a trace of each failing test
```

CI runs the solutions on every push (`.github/workflows/ci.yml`).

## Layout

```
Playwright-Python-Practice/
├── run-tests.sh                 run everything (add --mine for your own code)
├── requirements.txt             playwright, pytest, pytest-playwright
├── site/                        the practice website: login, todo app, widgets, table, shop, ...
├── src/
│   ├── common/                  server.py (serves site/ plus a small JSON API), target.py
│   ├── exercises/<topic>/       problems.py (core) + practice.py: you fill these in
│   └── solutions/<topic>/       problems.py (core) + practice.py: worked answers
├── test/                        test_<topic>.py + test_<topic>_practice.py per topic, conftest.py
└── tracker/index.html           daily progress tracker
```

Topics: `basics/ locators/ actions/ assertions/ waits/ frames/ network/ pom/ context/ project/`

**Practice tip:** read the exercise's docstring, open the page in a browser to look at it, write your
answer in `src/exercises`, and run `sh run-tests.sh --mine -k <function_name>`. Open the solution
only once your test passes (to compare) or after 20 minutes stuck.

To look at the practice site yourself, run `python -m common.server` from the `src/` folder and open
http://127.0.0.1:8000/.

## 8-week roadmap

Spend about an hour a day: two exercises, then a line in the tracker's daily log. Each week, redo two
exercises from earlier weeks without looking.

| Week | Topics                          | Goal                                                                   |
| ---- | ------------------------------- | ---------------------------------------------------------------------- |
| 1    | Basics, locators                | Open pages; find any element by role, label, text or test id           |
| 2    | Actions                         | Click, type, check, select, hover, upload and drag without extra waits |
| 3    | Assertions, waiting             | Use expect() instead of assert; never call time.sleep()                |
| 4    | Dialogs, frames and tabs        | Handle alerts, iframes, new tabs, popups and downloads                 |
| 5    | Network and API testing         | Mock, block and watch requests; test an API with page.request          |
| 6    | Page objects and pytest         | Write page objects, fixtures and parametrized tests                    |
| 7    | Contexts, sign-in and emulation | Reuse a signed-in state; emulate phones, locales, location, offline    |
| 8    | End-to-end project              | Whole user journeys; debug with traces, videos and ARIA snapshots      |

## Exercises by topic

| Topic | Exercises | Source |
| ----- | --------- | ------ |
| Basics | Open and get title, Get heading text, Navigate by link, Take screenshot, Title with your own browser | [exercise](src/exercises/basics/problems.py) · [solution](src/solutions/basics/problems.py) |
| Locators | Click button by role, Fill by label, Search by placeholder, Read by test id, Find by text | [exercise](src/exercises/locators/problems.py) · [solution](src/solutions/locators/problems.py) |
| Actions | Log in, Tick and pick, Select country, Type and press Enter, Hover menu | [exercise](src/exercises/actions/problems.py) · [solution](src/solutions/actions/problems.py) |
| Assertions | Check title and URL, Check login error, Check todo count, Check form state, Check banner hidden | [exercise](src/exercises/assertions/problems.py) · [solution](src/solutions/assertions/problems.py) |
| Waiting | Wait for new element, Wait until enabled, Wait for spinner, Wait for API response | [exercise](src/exercises/waits/problems.py) · [solution](src/solutions/waits/problems.py) |
| Dialogs, frames and tabs | Read alert, Cancel confirm, Answer prompt, Fill form in iframe, Open link in new tab | [exercise](src/exercises/frames/problems.py) · [solution](src/solutions/frames/problems.py) |
| Network and API testing | Mock products, Break products, Capture login request, API list users, API create user | [exercise](src/exercises/network/problems.py) · [solution](src/solutions/network/problems.py) |
| Page objects and pytest | Login page object, Todo page object | [exercise](src/exercises/pom/problems.py) · [solution](src/solutions/pom/problems.py) |
| Contexts, sign-in and emulation | Save signed-in state, Reuse signed-in state, Two users at once, Emulate iPhone | [exercise](src/exercises/context/problems.py) · [solution](src/solutions/context/problems.py) |
| End-to-end project | Todo journey, Todo filters, Record trace, Record video | [exercise](src/exercises/project/problems.py) · [solution](src/solutions/project/problems.py) |

## Practice exercises

60 more exercises, one `practice.py` per topic, each with the same task docstring and its own tests.

| Topic | Exercises | Source |
| ----- | --------- | ------ |
| Basics | Back and forward, URL after a redirect, Count menu links, Read meta description, Phone-sized viewport, Screenshot of pricing | [exercise](src/exercises/basics/practice.py) · [solution](src/solutions/basics/practice.py) |
| Locators | CSS and XPath, First and last rows, Price of a product row, Choose plan, Menu link names, Logo source | [exercise](src/exercises/locators/practice.py) · [solution](src/solutions/locators/practice.py) |
| Actions | Double click, Right click, Pick fruits, Set volume, Type slowly, Replace bio, Upload file, Drag and drop | [exercise](src/exercises/actions/practice.py) · [solution](src/solutions/actions/practice.py) |
| Assertions | Check attribute and class, Check contains text, Check list of texts, Check input value, Assert the opposite with not_, Read a failure message | [exercise](src/exercises/assertions/practice.py) · [solution](src/solutions/assertions/practice.py) |
| Waiting | Wait for counter, Wait for redirect, Wait for network idle, Wait for text change, Wait for removal, Load all items | [exercise](src/exercises/waits/practice.py) · [solution](src/solutions/waits/practice.py) |
| Dialogs, frames and tabs | Accept confirm, Read popup, Nested frame text, Count frames, Download report, Close tab and return | [exercise](src/exercises/frames/practice.py) · [solution](src/solutions/frames/practice.py) |
| Network and API testing | Discount prices, Block images, List API calls, Slow API shows loading, API login then /api/me, API delete user, API bad request | [exercise](src/exercises/network/practice.py) · [solution](src/solutions/network/practice.py) |
| Page objects and pytest | Shop page object, Table page object, Widgets page object | [exercise](src/exercises/pom/practice.py) · [solution](src/solutions/pom/practice.py) |
| Contexts, sign-in and emulation | Dark mode, Fake location, German locale, Go offline, Sign in with cookie, Run JavaScript | [exercise](src/exercises/context/practice.py) · [solution](src/solutions/context/practice.py) |
| End-to-end project | Todos survive reload, Edit todo, Checkout journey, Logout journey, Languages ARIA snapshot, Check ARIA snapshot | [exercise](src/exercises/project/practice.py) · [solution](src/solutions/project/practice.py) |

## Locator cheat sheet

Pick the first one that works. The ones at the top match what a user sees, so they break least.

| To find…                          | Use                                               |
| --------------------------------- | ------------------------------------------------- |
| A button, link, heading, checkbox | `page.get_by_role("button", name="Sign in")`      |
| A form field with a label         | `page.get_by_label("Username")`                   |
| A field with only a placeholder   | `page.get_by_placeholder("Search products")`      |
| Plain text                        | `page.get_by_text("Welcome")`                     |
| An image                          | `page.get_by_alt_text("Company logo")`            |
| An element with data-testid       | `page.get_by_test_id("cart-count")`               |
| Anything else                     | `page.locator("#id .class")` or `"xpath=//…"`     |
| One of many matches               | `.first`, `.last`, `.nth(2)`                      |
| A row or card containing X        | `.filter(has_text="X")` or `.filter(has=locator)` |
| Something inside something        | chain: `card.get_by_role("button", name="Buy")`   |
| Inside an iframe                  | `page.frame_locator("#frame").get_by_label(...)`  |

## Waiting cheat sheet

| Instead of…                         | Use                                                       |
| ----------------------------------- | --------------------------------------------------------- |
| `time.sleep(2)` before a click      | nothing: `click()` already waits for the element          |
| `assert el.inner_text() == "Ready"` | `expect(el).to_have_text("Ready")`, which retries         |
| Waiting for an element to appear    | `locator.wait_for()` or `expect(locator).to_be_visible()` |
| Waiting for a spinner to go away    | `locator.wait_for(state="hidden")`                        |
| Waiting for a page change           | `page.wait_for_url("**/account.html")`                    |
| Waiting for an API call             | `with page.expect_response("**/api/items*") as r:`        |
| Waiting for a JavaScript condition  | `page.wait_for_function("() => window.ready")`            |

## Debugging tips

- `sh run-tests.sh --mine --headed --slowmo 500 -k <name>` shows the browser, slowed down.
- `PWDEBUG=1 sh run-tests.sh --mine -k <name>` opens the Playwright Inspector so you can step through.
- Put `page.pause()` in your code to stop there with the Inspector open.
- `playwright codegen http://127.0.0.1:8000/login.html` records your clicks as Python code. Start the
  practice site first.
- `--tracing retain-on-failure` saves a trace in `test-results/`. Open it with
  `playwright show-trace <file>.zip` to see every step, screenshot and network call.
- "strict mode violation" means your locator matched more than one element. Make it more specific
  with `exact=True`, a role, `.filter()` or chaining.

## Python and pytest tips

- Use the sync API (`from playwright.sync_api import Page, expect`). It reads top to bottom.
- pytest-playwright gives you the `page`, `context`, `browser` and `playwright` fixtures. Each test
  gets a fresh context and page, so tests can't leak cookies into each other.
- Put shared setup in fixtures in `conftest.py`, not in helper calls at the top of every test.
- Use `@pytest.mark.parametrize` to run one test with several inputs.
- Keep locators in page objects, so a page change means one fix, not twenty.

## Progress tracker

`tracker/index.html` is a daily tracker for all 104 exercises, with links to each exercise, its
solution and the Playwright docs page it practises. You can open it on a phone or a computer. Mark
each exercise To do, Attempted, Done or Revise and keep notes on it. Log minutes and a line about each
study day, and see your roadmap week, streak, topic progress and a 12-week activity heatmap.
