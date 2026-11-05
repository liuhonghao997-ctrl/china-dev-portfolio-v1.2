"""Playwright test of simulated portfolio data, against local static site.
Usage: pip install playwright; python -m playwright install chromium;
       place this file in repo's tests/ folder and run python tests/browser_regression.py
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
    httpd = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
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
        page.on('pageerror', lambda e: errors.append(str(e)))
        page.goto(base + '/')
        for link in ('inventory.html', 'csv-tool.html', 'quote.html'):
            assert page.locator(f'a[href="{link}"]').count() >= 1
        for anchor in ('services', 'works', 'process'):
            assert page.locator('#' + anchor).count() == 1
        page.goto(base + '/inventory.html')
        page.evaluate("localStorage.removeItem('portfolio_inventory_v1')")
        page.reload()
        assert page.locator('#total').inner_text() == '5'
        page.locator('#add').click()
        for key,value in {'sku':'E2E-001','name':'浏览器测试商品','category':'测试','price':'12.50','quantity':'2','threshold':'3'}.items():
            page.locator('#' + key).fill(value)
        page.locator('#form button[type=submit]').click()
        assert page.locator('#total').inner_text() == '6'
        assert page.locator('#low').inner_text() == '3'
        page.locator('#query').fill('E2E-001')
        assert page.locator('#items tr').count() == 1
        page.locator('[data-edit="E2E-001"]').click()
        page.locator('#quantity').fill('20')
        page.locator('#form button[type=submit]').click()
        assert page.locator('#low').inner_text() == '2'
        assert '正常' in page.locator('#items').inner_text()
        page.reload()
        page.locator('#query').fill('E2E-001')
        assert '20' in page.locator('#items').inner_text()
        with page.expect_download() as exported:
            page.locator('#export').click()
        assert exported.value.suggested_filename == 'inventory.csv'
        exported_file = exported.value.path()
        page.on('dialog', lambda d: d.accept())
        page.locator('#reset').click()
        assert page.locator('#total').inner_text() == '5'
        page.locator('#import').set_input_files(str(exported_file))
        assert page.locator('#total').inner_text() == '6'
        page.locator('#query').fill('E2E-001')
        page.locator('[data-delete="E2E-001"]').click()
        assert page.locator('#total').inner_text() == '5'
        page.reload()
        page.locator('#query').fill('E2E-001')
        assert '没有符合条件的商品' in page.locator('#items').inner_text()
        page.goto(base + '/csv-tool.html')
        assert page.locator('#count').inner_text() == '4'
        assert page.locator('#matched').inner_text() == '3'
        assert page.locator('#missing').inner_text() == '1'
        page.goto(base + '/quote.html')
        page.locator('#qty').fill('2')
        page.locator('#unit').fill('100')
        page.locator('#tax').fill('10')
        assert page.locator('#outTotal').inner_text() == '¥220.00'
        page.evaluate('window.__didPrint = false; window.print = () => { window.__didPrint = true }')
        page.locator('#print').click()
        assert page.evaluate('window.__didPrint') is True
        assert not errors, errors
        browser.close()
    print('BROWSER_REGRESSION_OK')

if __name__ == '__main__':
    run()
