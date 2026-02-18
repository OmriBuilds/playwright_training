from datetime import date
from playwright.sync_api import expect
from python_training.NASA_Automation_Project.globals import URL, planets
from python_training.NASA_Automation_Project.pages.image_of_the_day_page import ImageOfTheDayPage
from python_training.NASA_Automation_Project.pages.nasa_home_page import NasaHomePage
from python_training.NASA_Automation_Project.pages.search_results_page import SearchResultsPage
from python_training.NASA_Automation_Project.tests.conftest import setup_playwright_nasa


class TestNASAHomePage:

    def test_homepage_title_contains_nasa(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        assert "NASA" in page.title(), "Homepage title does not contain NASA"

    def test_search_bar_functionality(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        homepage.perform_search(planets[0])
        result_page = SearchResultsPage(page)
        search_results = result_page.get_search_results_title()
        expect(search_results).to_contain_text(planets[0])


    def test_search_results_sum(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        homepage.perform_search(planets[1])
        result_page = SearchResultsPage(page)
        search_results_sum = result_page.extract_results_sum()
        assert search_results_sum > 0, f'0 Results found for "{planets[1]}".'

    def test_radio_button_functionality(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        homepage.perform_search(planets[2])
        results_page = SearchResultsPage(page)
        results_page.filter_search_results()
        results_page.click_search_result()
        results_date = results_page.check_results_date()
        assert results_date == int(date.today().year), "Results date does not match search filter."
        # print("pause")

    def test_logo_link_image_page(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        NasaHomePage(page).go_to_image_of_the_day()
        ImageOfTheDayPage(page).verify_logo_link()
        assert page.url == URL, "Logo link does not match URL."

    def test_image_of_the_day_date(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        NasaHomePage(page).go_to_image_of_the_day()
        image_page = ImageOfTheDayPage(page)
        image_page.click_image_of_the_day()
        image_date = image_page.get_date_image_of_the_day()
        assert image_date == date.today().strftime("%b %d, %Y").upper(), "Image date does not match current date."




