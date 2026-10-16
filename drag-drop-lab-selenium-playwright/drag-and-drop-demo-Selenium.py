from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.implicitly_wait(5)

def go_to_url(url):
    driver.get(url)
    driver.implicitly_wait(5)
    time.sleep(1)  # just so we can visually see the drag happen, not necessary for the test to pass


def basic_element_drag_v1():
    URL_BASIC_ELEMENT_DRAG = "http://localhost:4173/basic-element-drag/"
    go_to_url(URL_BASIC_ELEMENT_DRAG)

    source = driver.find_element(By.CSS_SELECTOR, '[data-testid="task-card"]')
    target = driver.find_element(By.CSS_SELECTOR, '[data-testid="done-column"]')

    ActionChains(driver).drag_and_drop(source, target).perform()
    status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    assert "Success" in status.text
    print("Basic element drag passed")
    breakpoint()

def basic_element_drag_v2():
    URL_BASIC_ELEMENT_DRAG = "http://localhost:4173/basic-element-drag/"
    go_to_url(URL_BASIC_ELEMENT_DRAG)

    source = driver.find_element(By.CSS_SELECTOR, '[data-testid="task-card"]')
    target = driver.find_element(By.CSS_SELECTOR, '[data-testid="done-column"]')


    pause_seconds = 2
    actions = ActionChains(driver)


    actions.move_to_element(source)
    actions.click_and_hold()
    actions.pause(pause_seconds)
    actions.move_to_element(target)
    actions.pause(pause_seconds)
    actions.release()
    actions.perform()


def coordinate_drag():
    URL_COORDINATE_DRAG = "http://localhost:4173/coordinates/"
    go_to_url(URL_COORDINATE_DRAG)


    source = driver.find_element(By.CSS_SELECTOR, '[data-testid="task-card"]')
    target = driver.find_element(By.CSS_SELECTOR, '[data-testid="done-column"]')

    # # example of why drag drop won't work with coordinates, the source and target are not aligned
    # ActionChains(driver).drag_and_drop(source, target).perform()
    # status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    # breakpoint()
    # assert "Success" in status.text, "Success message not displayed."
    # print("Basic element drag passed")


    # we have to calculate where to drop off the source
    # source center → exact destination point
    # offset = destination point − source center

    source_box = source.rect  # size and cordinates of element {'height': 273, 'width': 243, 'x': 117, 'y': 446}
    target_box = target.rect

    # Find the center of the source card
    source_x = source_box["x"] + source_box["width"] / 2
    source_y = source_box["y"] + source_box["height"] / 2

    # Choose the exact drop point inside the target
    target_x = target_box["x"] + target_box["width"] / 2
    target_y = target_box["y"] + 48

    # Calculate the distance from the source to the drop point
    x_offset = target_x - source_x
    y_offset = target_y - source_y



    ActionChains(driver).drag_and_drop_by_offset(
        source, x_offset, y_offset
    ).perform()

    # actions = ActionChains(driver)
    # actions.move_to_element(source)
    # actions.click_and_hold()
    # actions.pause(1)
    # actions.move_by_offset(x_offset, y_offset)
    # actions.pause(1)
    # actions.release()
    # actions.perform()

    status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    assert "Success" in status.text, "Success message not displayed."
    print("Basic element drag passed")
    breakpoint()



def movement_drag():
    URL_MOVEMENT_DRAG = "http://localhost:4173/movement/"
    go_to_url(URL_MOVEMENT_DRAG)

    source = driver.find_element(By.CSS_SELECTOR, '[data-testid="task-card"]')
    target = driver.find_element(By.CSS_SELECTOR, '[data-testid="done-column"]')

    # # example of why drag drop won't work with coordinates, the source and target are not aligned
    # ActionChains(driver).drag_and_drop(source, target).perform()
    # status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    # breakpoint()
    # assert "Success" in status.text, "Success message not displayed."
    # print("Basic element drag passed")

    # """
    source_box = source.rect
    target_box = target.rect

    # Find the center of the source card
    source_x = source_box["x"] + source_box["width"] / 2
    source_y = source_box["y"] + source_box["height"] / 2

    # Choose the exact drop point inside the target
    target_x = target_box["x"] + target_box["width"] / 2
    target_y = target_box["y"] + 48

    # Calculate the distance from the source to the drop point
    x_offset = target_x - source_x
    y_offset = target_y - source_y

    steps = 10
    x_step = x_offset / steps
    y_step = y_offset / steps

    actions = ActionChains(driver).move_to_element(source).click_and_hold()
    for _ in range(steps):
        actions.move_by_offset(x_step, y_step)
        actions.pause(0.1)  # Optional: add a small pause for visual effect
    actions.release().perform()
    breakpoint()
    status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    assert "Success" in status.text, "Success message not displayed."
    print("Movement drag passed")
    # """


def data_transfer_drag_html5():
    URL_DATA_TRANSFER_DRAG = "http://localhost:4173/html5/"
    go_to_url(URL_DATA_TRANSFER_DRAG)

    card = driver.find_element(By.CSS_SELECTOR, '[data-testid="task-card"]')
    done_column = driver.find_element(By.CSS_SELECTOR, '[data-testid="done-column"]')

    # ActionChains(driver).drag_and_drop(card, done_column).perform()
    # status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    # breakpoint()
    # assert "Success" in status.text, "Success message not displayed."
    # print("Data transfer drag passed")


    driver.execute_script(
        """
        const source = arguments[0];
        const target = arguments[1];
        const data = new DataTransfer();
        data.setData('application/x-job-id', source.dataset.jobId);

        const eventOptions = {
          bubbles: true,
          cancelable: true,
          dataTransfer: data
        };

        source.dispatchEvent(new DragEvent('dragstart', eventOptions));
        target.dispatchEvent(new DragEvent('dragenter', eventOptions));
        target.dispatchEvent(new DragEvent('dragover', eventOptions));
        target.dispatchEvent(new DragEvent('drop', eventOptions));
        """,
        card,
        done_column,
    )
    status = driver.find_element(By.CSS_SELECTOR, '[data-testid="status"]')
    breakpoint()
    assert "Success" in status.text, "Success message not displayed."
    print("Data transfer drag passed")


# basic_element_drag_v1()
# basic_element_drag_v2()

# coordinate_drag()

# movement_drag()

try:
    data_transfer_drag_html5()
finally:
    driver.quit()
