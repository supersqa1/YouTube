from playwright.sync_api import expect, sync_playwright


BASE_URL = "http://localhost:4173"
SOURCE = '[data-testid="task-card"]'
TARGET = '[data-testid="done-column"]'
STATUS = '[data-testid="status"]'


playwright = sync_playwright().start()
browser = playwright.chromium.launch(
    headless=False,
    slow_mo=1000,  # Slows the actions for the video. Not required for the test.
)
page = browser.new_page()
page.set_default_timeout(3_000)


def go_to_url(path):
    page.goto(f"{BASE_URL}/{path}/")
    page.wait_for_timeout(1_000)  # Gives viewers time to see the page.

def check_success():
    expect(page.locator(STATUS)).to_contain_text("Success")


def basic_element_drag():
    go_to_url("basic-element-drag")

    source = page.locator(SOURCE)
    target = page.locator(TARGET)

    source.drag_to(target)

    check_success()
    print("Basic element drag passed")
    breakpoint()



def coordinate_drag():
    go_to_url("coordinates")

    source = page.locator(SOURCE)
    target = page.locator(TARGET)

    # source.drag_to(target)  # This will fail because the source and target are not aligned.

    target_box = target.bounding_box()
    assert target_box is not None

    # Drop in the horizontal center, 48 pixels below the target's top edge.
    drop_position = {
        "x": target_box["width"] / 2,
        "y": 48,
    }

    source.drag_to(target, target_position=drop_position)

    check_success()
    print("Coordinate drag passed")
    breakpoint()



def movement_drag():
    go_to_url("movement")

    source = page.locator(SOURCE)
    target = page.locator(TARGET)

    # Generate several mousemove events between the source and target.
    # source.drag_to(target)
    source.drag_to(target, steps=10)

    check_success()
    print("Movement-sensitive drag passed")
    breakpoint()

def data_transfer_drag_html5():
    go_to_url("html5")

    source = page.locator(SOURCE)
    target = page.locator(TARGET)

    # Always try Playwright's normal drag first.
    # source.drag_to(target, steps=2)

    # check_success()
    # print("HTML5 drag passed")
    # breakpoint()

    # If drag_to() fails on a stricter application, reload the page and use
    # the DataTransfer fallback below instead:
    #
    data_transfer = page.evaluate_handle("new DataTransfer()")
    source.dispatch_event("dragstart", {"dataTransfer": data_transfer})
    target.dispatch_event("dragenter", {"dataTransfer": data_transfer})
    target.dispatch_event("dragover", {"dataTransfer": data_transfer})
    target.dispatch_event("drop", {"dataTransfer": data_transfer})
    data_transfer.dispose()

    check_success()
    print("HTML5 drag passed")
    breakpoint()

# basic_element_drag()
# coordinate_drag()
# movement_drag()
try:
    data_transfer_drag_html5()
finally:
    browser.close()
    playwright.stop()
