from time import sleep

from playwright.sync_api import Playwright, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    iphone = p.devices['iPhone 6']
    print()
    context = browser.new_context(
        color_scheme='dark',
        record_video_dir='.',
        # viewport={'width':1200, 'height': 100}

    )
    page = browser.new_page()
    page.goto('http://dgg.gg')
    sleep(5)

    print(page.title())

    browser.close()
