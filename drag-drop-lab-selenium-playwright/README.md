# Follow the video: Selenium and Playwright Drag-and-Drop Lab

This folder contains the practice website and Python code for two videos: **drag and drop with Selenium** and **drag and drop with Playwright**. Both videos use the same job-tracker board, with four different drag implementations. Run the website first, then run the Python script for the video you are following.

## Which file should I use?

| File | Use it for |
| --- | --- |
| [drag-and-drop-demo-Selenium.py](./drag-and-drop-demo-Selenium.py) | **Selenium video.** Shows `ActionChains` for basic, coordinate-based, and movement-sensitive dragging, plus JavaScript drag events for HTML5. |
| [drag-and-drop-demo-Playwright.py](./drag-and-drop-demo-Playwright.py) | **Playwright video.** Shows `drag_to()`, target positions, movement steps, and a shared `DataTransfer` object for HTML5. |
| `index.html`, `app.js`, `styles.css`, and the four page folders | The practice website used by both videos. No Node.js, database, account, or backend is needed. |
| `*.excalidraw` | Editable teaching diagrams. These are optional and are not needed to run the code. |

The job cards contain sample data. Search, notifications, and New Application are decorative; dragging and Reset Demo are functional.

## 1. Get the code

Clone the YouTube repository, or download its ZIP and extract it. If you cloned it:

```bash
git clone https://github.com/supersqa1/YouTube.git
cd YouTube/drag-drop-lab-selenium-playwright
```

If you already have the repository, open a terminal inside **`drag-drop-lab-selenium-playwright`**. Run all commands below from that folder.

You need Python 3 and a desktop environment to see the browser. For the Selenium video, also install Google Chrome. For the Playwright video, the browser installation command is included below.

## 2. Start the practice app — terminal 1

On macOS or Linux:

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

On Windows:

```powershell
py -m http.server 4173 --bind 127.0.0.1
```

Open **<http://localhost:4173>** in your browser. You should see the SuperSQA Job Tracker and four implementation tabs. Try moving the SuperSQA card from **Potential** to **Applied**. Use **Reset Demo** or reload the page to start again.

**Leave this terminal running.** The test scripts need this server. Stop it with Ctrl+C when you finish.

## 3. Install the Python dependencies — terminal 2

Open a second terminal in the same project folder. Create and activate a virtual environment:

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

For Windows Command Prompt, activate with `.venv\Scripts\activate.bat` instead.

The requirements install both frameworks. **If you are following Playwright**, also install its Chromium browser:

```bash
python -m playwright install chromium
```

**If you are following Selenium**, Google Chrome must be installed. Selenium Manager automatically configures the Chrome driver when the script starts; a separate manual ChromeDriver setup is normally unnecessary.

Reactivate this environment whenever you open a new terminal to run the scripts.

## 4. Run the script for your video

### Selenium video

```bash
python drag-and-drop-demo-Selenium.py
```

### Playwright video

```bash
python drag-and-drop-demo-Playwright.py
```

Run one script at a time. Each opens its own visible browser, loads a page from your local server, and performs the selected drag. Successful examples move the source card into **Applied**, display a **Success** message, and print a passed message in the terminal.

**Both main scripts currently select the HTML5 example by default.** To start with the first example in the video, change the selected function as described next.

### Choose the example you want to follow

The functions are defined earlier in each file; the calls near the bottom select what actually runs. In either main script, replace the call **inside the `try:` block**, keeping its indentation. Leave the `finally:` cleanup in place.

For example, start with the basic Selenium drag:

```python
try:
    basic_element_drag_v1()
finally:
    driver.quit()
```

Or start with the basic Playwright drag:

```python
try:
    basic_element_drag()
finally:
    browser.close()
    playwright.stop()
```

Save the file and rerun its command after changing the selected function. Use one function at a time to follow the video. Some commented-out lines within functions illustrate attempts that fail for a particular page; leave those commented unless you are deliberately comparing the approaches.

## What each example demonstrates

| App tab / page | Selenium function and technique | Playwright function and technique |
| --- | --- | --- |
| **1. Basic Element Drag** — `/basic-element-drag/` | `basic_element_drag_v1()`: `ActionChains.drag_and_drop(source, target)`. `basic_element_drag_v2()` breaks the operation into move, hold, pause, move, and release actions. | `basic_element_drag()`: `source.drag_to(target)`. |
| **2. Coordinates** — `/coordinates/` | `coordinate_drag()`: calculates the offset from the source center to a point near the target's top, then uses `drag_and_drop_by_offset()`. | `coordinate_drag()`: uses `target_position` to drop at the target's horizontal center and 48 pixels below its top. |
| **3. Movement** — `/movement/` | `movement_drag()`: holds the card and moves through ten smaller offsets before releasing. | `movement_drag()`: uses `source.drag_to(target, steps=10)`. |
| **4. DataTransfer** — `/html5/` | `data_transfer_drag_html5()`: executes JavaScript to dispatch HTML5 drag events with a shared `DataTransfer` payload. | `data_transfer_drag_html5()`: creates a `DataTransfer` handle and passes it through `dragstart`, `dragenter`, `dragover`, and `drop`. |

The coordinate page accepts drops only near the top insertion line. The movement page requires at least six movement events. The HTML5 page requires the job ID in the drag payload. The pages look similar, but these implementation differences explain why the same automation technique does not work everywhere.

## Why does the script pause at `(Pdb)`?

These are the recording scripts used for the videos. They intentionally include `breakpoint()` calls so you can inspect the browser and variables. **A `(Pdb)` prompt means the script is paused, not stuck.** Type `c` and press Enter to continue. Some pauses occur before the final assertion, so continue until the script finishes.

To run without debugger pauses:

### macOS / Linux

```bash
PYTHONBREAKPOINT=0 python drag-and-drop-demo-Selenium.py
PYTHONBREAKPOINT=0 python drag-and-drop-demo-Playwright.py
```

### Windows PowerShell

```powershell
$env:PYTHONBREAKPOINT="0"
python drag-and-drop-demo-Selenium.py
# Or: python drag-and-drop-demo-Playwright.py
```

In Command Prompt, run `set PYTHONBREAKPOINT=0` before running the script. With pauses disabled, the browser may close quickly after the example completes. Sleeps and Playwright's `slow_mo` are there to make the video easier to follow.

## Troubleshooting

| What you see | What to check |
| --- | --- |
| Connection refused / page does not load | Keep terminal 1 running and confirm <http://localhost:4173> opens. The scripts expect port **4173**. |
| Directory listing or missing lab pages | Start the server inside `drag-drop-lab-selenium-playwright`, where `index.html` and `app.js` live. |
| `ModuleNotFoundError` | Activate `.venv` in terminal 2, then run `python -m pip install -r requirements.txt`. |
| Playwright says its browser executable is missing | Run `python -m playwright install chromium` in the activated environment. |
| Selenium cannot start Chrome | Confirm Google Chrome is installed and that Selenium Manager can download its driver. |
| `drag_to()` rejects `steps` | Update dependencies with `python -m pip install --upgrade -r requirements.txt`. The [steps option requires Playwright 1.57+](https://playwright.dev/python/docs/api/class-locator#locator-drag-to-option-steps). |
| The example stops at `(Pdb)` | Type `c` to continue, or disable pauses as described above. |
| The wrong scenario runs | Check the selected function call in the script's bottom `try:` block. Defining a function does not run it. |
| Port 4173 is already in use | Stop the previous lab server or other process using that port, then start the server again. |

When finished, stop the server with Ctrl+C and run `deactivate` in the automation terminal to leave the virtual environment.
