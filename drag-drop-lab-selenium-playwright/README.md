# Selenium and Playwright Drag-and-Drop Lab

Code and editable Excalidraw diagrams for the Selenium and Playwright drag-and-drop videos. The static job-tracker board uses sample data and implements four drag behaviors.

## Start the lab

From this folder, start a local server (Python 3 required):

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

On Windows, replace `python3` with `py`. Open <http://localhost:4173> and keep the server running. Stop it with Ctrl+C.

The four tabs demonstrate:

1. **Basic Element Drag** (`/basic-element-drag/`): source-to-target dragging.
2. **Coordinates** (`/coordinates/`): release near the target's top insertion line.
3. **Movement** (`/movement/`): generate at least six movement events during the drag.
4. **DataTransfer** (`/html5/`): send HTML5 drag events with a shared DataTransfer payload.

This is a training interface; search, notifications, and New Application are decorative. Reload or use Reset Demo to reset the board. No backend or account is required.

## Install the automation dependencies

In a second terminal, from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

On Windows, create the environment with `py -m venv .venv`, then activate it with `.venv\Scripts\activate` in Command Prompt or `.venv\Scripts\Activate.ps1` in PowerShell.

Selenium requires Google Chrome; Selenium Manager configures the driver automatically. Playwright uses its separately installed Chromium browser.

## Run the video examples

```bash
python drag-and-drop-demo-Selenium.py
python drag-and-drop-demo-Playwright.py
```

Run one command at a time. These are the recording examples: by default each runs the HTML5 DataTransfer scenario. Uncomment the other calls at the bottom of each file to try basic, coordinate, or movement-sensitive dragging. The Selenium file also includes a second basic drag technique.

The scripts intentionally call `breakpoint()` so the video can pause for inspection. Type `c` at the debugger prompt to continue, or disable debugger pauses:

```bash
PYTHONBREAKPOINT=0 python drag-and-drop-demo-Selenium.py
PYTHONBREAKPOINT=0 python drag-and-drop-demo-Playwright.py
```

In PowerShell, set `$env:PYTHONBREAKPOINT="0"` before running a script. In Command Prompt, use `set PYTHONBREAKPOINT=0`.

`codex-drag-and-drop-demo-Playwright.py` is an alternate example, configured to run the basic drag by default. The `.excalidraw` files are editable video diagrams.

[Playwright's `drag_to(..., steps=10)`](https://playwright.dev/python/docs/api/class-locator#locator-drag-to-option-steps) requires Playwright 1.57 or newer. Sleeps and `slow_mo` are included for viewers; they are not required for production automation.
