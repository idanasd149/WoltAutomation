import undetected_chromedriver as uc


class WebDriver:
    def __init__(self, profile_path=None):
        self.profile_path = profile_path
        options = uc.ChromeOptions()
        if profile_path:
            options.user_data_dir = profile_path
        self.driver = uc.Chrome(options=options)

    def quit(self):
        self.driver.quit()
