from utils import get_profile_directory, wait_for_file
from web_driver import WebDriver
from wolt_automation import WoltAutomation

if __name__ == '__main__':
    user_id = wait_for_file('user_id.txt')
    user_profile_path = get_profile_directory("saved_profiles", user_id)
    web_driver = WebDriver(profile_path=user_profile_path)
    WoltAutomation(web_driver)
