# SeleniumCookieSaver
Small tool to save cookies, for example, after passing captcha using Selenium

This Python script utilizes Selenium to automate interaction with a website and manage cookies.

1. Imports necessary libraries:
   - selenium: To automate the web browser.
   - pickle: To serialize and deserialize Python objects (in this case, cookies).
   - os: To interact with the operating system, such as checking if a file exists.
   - keyboard: To detect key presses.

2. Defines the WEBSITE and COOKIES variables:
   - WEBSITE: The URL of the website to be automated.
   - COOKIES: The name of the file where cookies will be stored.

3. Configures the Chrome driver:
   - Creates a Service object with the path to the chromedriver.
   - Creates a webdriver.Chrome object using the configured service.

4. Checks if saved cookies exist:
   - If the COOKIES file exists, loads the cookies using pickle.load, adds them to the driver with driver.add_cookie, and reloads the page.
   - If the file does not exist, opens the website, waits for the user to press Enter after accepting cookies, and saves the cookies using pickle.dump.

5. Waits for the spacebar to be pressed:
   - Displays a message indicating that the spacebar should be pressed.
   - Uses keyboard.wait to pause execution until the spacebar is pressed.

6. Closes the browser:
   - Uses driver.quit to close the browser.

This script allows for automating website login using saved cookies, avoiding the need to enter credentials each time.
