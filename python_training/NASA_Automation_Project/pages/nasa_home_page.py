

class NasaHomePage:
    def __init__(self, page):
        self.page = page

    def get_homepage_title(self):
        return self.page.title()

    def perform_search(self, search_value:str):
        search_bar = self.page.locator("[id='search-field-en-small--desktop']")
        search_bar.click()
        search_bar.fill(search_value)
        self.page.keyboard.press("Enter")

    def go_to_image_of_the_day(self):
        multimedia_menu = self.page.get_by_role("button", name="Multimedia")
        multimedia_menu.click()
        image_of_the_day_link = self.page.get_by_role("link", name="Image of the Day")
        image_of_the_day_link.click()

    def get_explore_menu_links(self):
        self.page.get_by_role("button", name="Explore").click()
        links_list = self.page.locator("ul.hds-global-menu-primary.global-nav__primary-list.usa-nav__submenu-list").get_by_role("link").all()
        # for link in links_list:
        #     print(f"Link: '{link.inner_text()}' | '{link.get_attribute('href')}'")
        return [link.get_attribute('href') for link in links_list]

