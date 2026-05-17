import os

from contextlib import asynccontextmanager

from datastar_py.consts import ElementPatchMode
from datastar_py.fastapi import DatastarResponse, ServerSentEventGenerator as SSE
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse

from db import get_all_numbers, init_db, store_numbers


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


def render_rows():
    rows = get_all_numbers()
    if not rows:
        return '<tr><td colspan="4" class="empty-state">No numbers stored yet</td></tr>'

    html = ""
    for row in rows:
        html += f"""
        <tr>
            <td class="py-2 px-4">{row[0]}</td>
            <td class="py-2 px-4">{row[1]}</td>
            <td class="py-2 px-4">{row[2]}</td>
            <td class="py-2 px-4">{row[3]}</td>
        </tr>
        """
    return html


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    with open("templates/index.html") as f:
        return f.read()


@app.post("/api/numbers")
async def create_numbers(
    seven_digit: str = Form(...),
    long_digit: str = Form(...),
):
    # Validate seven_digit: must be exactly 7 digits
    if not seven_digit.isdigit() or len(seven_digit) != 7:
        return DatastarResponse(
            SSE.patch_elements(
                '<div id="message" class="error">Seven digit number must be exactly 7 digits</div>',
                selector="#message",
                mode=ElementPatchMode.INNER,
            )
        )

    # Validate long_digit: must be 10-14 digits
    if not long_digit.isdigit() or not (10 <= len(long_digit) <= 14):
        return DatastarResponse(
            SSE.patch_elements(
                '<div id="message" class="error">Second number must be between 10 and 14 digits</div>',
                selector="#message",
                mode=ElementPatchMode.INNER,
            )
        )

    store_numbers(int(seven_digit), long_digit)

    return DatastarResponse(
        [
            SSE.patch_elements(
                '<div id="message" class="success">Numbers stored successfully!</div>',
                selector="#message",
                mode=ElementPatchMode.INNER,
            ),
            SSE.patch_elements(
                render_rows(),
                selector="#numbers-table",
                mode=ElementPatchMode.INNER,
            ),
        ]
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
