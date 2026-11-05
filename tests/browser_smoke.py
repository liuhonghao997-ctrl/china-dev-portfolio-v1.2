"""Optional Playwright E2E test for local developer environment.
Run after: python3 -m pip install playwright && python3 -m playwright install chromium
The environment used to package this release blocks Chromium navigation, so it was not verified here.
"""
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

@contextmanager
def server():
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    httpd = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = Thread(target=httpd.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{httpd.server_port}'
    finally:
        httpd.shutdown()
        thread.join()

def run():
    with server() as base, sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(accept_downloads=True)
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(base, wait_until='load')
        assert page.locator('a[href="inventory.html"]').count() >= 1
        page.goto(base+'/inventory.html', wait_until='load')
        assert page.locator('#total').inner_text() == '5'
        page.locator('#add').click()
        for k,v in {'sku':'E2E-001','name':'浏览器测试商品','category':'测试','price':'12.50','quantity':'2','threshold':'3'}.items():
            page.locator('#'+k).fill(v)
        page.locator('#form button[type=submit]').click()
        assert page.locator('#total').inner_text() == '6'
        assert page.locator('#status').inner_text() == '商品已保存'
        page.reload(wait_until='load')
        assert page.locator('#total').inner_text() == '6'
        with page.expect_download() as info:
            page.locator('#export').click()
        assert info.value.suggested_filename == 'inventory.csv'
        page.on('dialog', lambda dialog: dialog.accept())
        page.locator('#reset').click()
        assert page.locator('#total').inner_text() == '5'
        page.goto(base+'/csv-tool.html', wait_until='load')
        assert page.locator('#status').inner_text().startswith('处理完成')
        page.goto(base+'/quote.html', wait_until='load')
        assert page.title()
        assert not errors, errors
        browser.close()
    print('BROWSER_SMOKE_OK')

if __name__ == '__main__': run()
