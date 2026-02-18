

class ImageOfTheDayPage:
    def __init__(self, page):
        self.page = page

    def click_image_of_the_day(self):
        latest_image = self.page.locator(".hds-gallery-item-single.hds-gallery-image").first
        latest_image.click()

    def get_date_image_of_the_day(self):
        image_date = self.page.locator("span.heading-12.text-uppercase").first.inner_text()
        return image_date

    def verify_logo_link(self):
        self.page.locator("#header-logo").click()
        return self.page.url

