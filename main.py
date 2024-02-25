from utils import get_profile_directory, wait_for_file
from web_driver import WebDriver
from wolt.wolt_automation import WoltAutomation
from wolt.wolt_shopping_actions import WoltShoppingActions

if __name__ == '__main__':
    user_id = wait_for_file('saved_texts_files/user_id.txt')
    user_profile_path = get_profile_directory("saved_profiles", user_id)

    web_driver = WebDriver(profile_path=user_profile_path)
    shopping_actions = WoltShoppingActions(web_driver)
    WoltAutomation(web_driver, shopping_actions)
