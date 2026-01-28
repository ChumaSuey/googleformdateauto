// This Playwright script goes to specified Google forms (in this case 3, in Spanish)
// And its function is just to pick today's date.
// Playwright - JavaScript script by Chuma and Nepta

const { chromium } = require('playwright');

(async () => {
    // Get today's date in YYYY-MM-DD format (required for HTML date inputs)
    const today = new Date();
    const todayDate = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, '0')}-${String(today.getDate()).padStart(2, '0')}`;

    // Launch browser with persistent context (keeps browser open after script finishes)
    const browser = await chromium.launch({
        headless: false,
        args: ['--start-maximized']
    });

    const context = await browser.newContext({
        viewport: null // Use full window size
    });

    // First form
    const page1 = await context.newPage();
    await page1.goto('https://docs.google.com/forms/d/e/1FAIpQLSewqr62ef2zxsB_2ZS-jQHz6BRbv_kny52WIRZ82lESUPS7EQ/viewform?usp=sf_link');
    await page1.waitForTimeout(1000);
    await page1.locator('input[type="date"]').fill(todayDate);
    await page1.waitForTimeout(3000);

    // Second form - open in new tab
    const page2 = await context.newPage();
    await page2.goto('https://docs.google.com/forms/d/e/1FAIpQLSeBmm5GJeKML_Oyi7hyhjof3vXl72ap5pvMFDD5nB-8kREP8g/viewform?usp=sf_link');
    await page2.waitForTimeout(1000);
    await page2.locator('input[type="date"]').fill(todayDate);
    await page2.waitForTimeout(3000);

    // Third form - open in new tab
    const page3 = await context.newPage();
    await page3.goto('https://docs.google.com/forms/d/e/1FAIpQLSfb6Xu4DRV4gbcw0DdvhC_QykN9O4pPzaotf2N1QMUY28-qaA/viewform?usp=sf_link');
    await page3.waitForTimeout(1000);
    await page3.locator('input[type="date"]').fill(todayDate);

    // Browser stays open - user can manually close it
    // If you want to close automatically, uncomment the line below:
    // await browser.close();
})();
