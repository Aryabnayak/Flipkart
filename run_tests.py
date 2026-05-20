import os
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=800)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:5000")
    page.click("text=Shop")
    page.click("text=Add Dress")
    page.click("text=Cart (1)")
    page.fill("input[placeholder='Address']", "123 Main St")
    page.click("text=Submit Order")
    page.wait_for_timeout(5000)