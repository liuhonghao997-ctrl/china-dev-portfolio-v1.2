"""V1.3 quality checks for synthetic demo data. Run: python tests/v13_quality.py"""
import os
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright, expect
ROOT = Path(__file__).resolve().parents[1]

@contextmanager
def server():
    httpd=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
    t=Thread(target=httpd.serve_forever,daemon=True)
    t.start()
    try: yield f'http://127.0.0.1:{httpd.server_port}'
    finally: httpd.shutdown();t.join()

def run():
    with server() as base, sync_playwright() as p:
        opts={'headless':True}
        if os.environ.get('CHROMIUM_PATH'): opts['executable_path']=os.environ['CHROMIUM_PATH']
        browser=p.chromium.launch(**opts)
        page=browser.new_page(viewport={'width':390,'height':844})
        errs=[]
        page.on('pageerror',lambda error:errs.append(str(error)))
        page.goto(base+'/quote.html')
        page.locator('#qty').fill('2')
        page.locator('#unit').fill('100.10')
        page.locator('#tax').fill('10')
        expect(page.locator('#outTotal')).to_have_text('¥220.22')
        page.locator('#qty').fill('1.5')
        expect(page.locator('#print')).to_be_disabled()
        expect(page.locator('#validation')).to_contain_text('整数')
        page.locator('#qty').fill('2')
        page.locator('#unit').fill('-1')
        expect(page.locator('#print')).to_be_disabled()
        page.locator('#unit').fill('100')
        page.locator('#tax').fill('101')
        expect(page.locator('#print')).to_be_disabled()
        page.locator('#tax').fill('10')
        expect(page.locator('#print')).to_be_enabled()
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1')
        page.goto(base+'/inventory.html')
        page.evaluate("localStorage.removeItem('portfolio_inventory_v1')")
        page.reload()
        expect(page.locator('#total')).to_have_text('5')
        # Force storage failure; mutation must not be reported as saved or appear in list.
        page.evaluate("Storage.prototype.setItem = () => { throw new DOMException('quota','QuotaExceededError') }")
        page.locator('#add').click()
        for field, value in {'sku':'FAIL-001','name':'保存失败测试','category':'模拟','price':'10','quantity':'2','threshold':'3'}.items():
            page.locator('#'+field).fill(value)
        page.locator('#form button[type=submit]').click()
        expect(page.locator('#status')).to_contain_text('本地保存失败')
        expect(page.locator('#total')).to_have_text('5')
        assert page.locator('[data-edit="FAIL-001"]').count() == 0
        assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 1')
        assert not errs,errs
        browser.close()
    print('V13_QUALITY_OK')

if __name__=='__main__':run()
