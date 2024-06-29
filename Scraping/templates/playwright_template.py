import asyncio
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto('')

    await context.close()
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())