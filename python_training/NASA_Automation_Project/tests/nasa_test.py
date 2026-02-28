from datetime import date
from playwright.sync_api import expect
from python_training.NASA_Automation_Project.globals import URL, planets
from python_training.NASA_Automation_Project.pages.image_of_the_day_page import ImageOfTheDayPage
from python_training.NASA_Automation_Project.pages.nasa_home_page import NasaHomePage
from python_training.NASA_Automation_Project.pages.search_results_page import SearchResultsPage
from python_training.NASA_Automation_Project.tests.conftest import setup_playwright_nasa


class TestNASAWebsite:

    ## Checks that the homepage title contains the name "NASA".
    def test_homepage_title_contains_nasa(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        assert "NASA" in page.title(), "Homepage title does not contain NASA"

    ## Performs a search of a valid term and checks that the results page contains the search term.
    def test_search_bar_functionality(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        homepage.perform_search(planets[0])
        result_page = SearchResultsPage(page)
        search_results = result_page.get_search_results_title()
        expect(search_results).to_contain_text(planets[0])

    ## Performs a search of a valid term and verifies the search yields results.
    def test_search_results_sum(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        homepage.perform_search(planets[1])
        result_page = SearchResultsPage(page)
        search_results_sum = result_page.extract_results_sum()
        assert search_results_sum > 0, f'0 Results found for "{planets[1]}".'

    ## Performs a search, filters the results to the last year, enters a result and extracts the publishing date
    ## compares the results publishing year to current year.
    def test_radio_button_functionality(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        homepage.perform_search(planets[2])
        results_page = SearchResultsPage(page)
        results_page.filter_search_results()
        results_page.click_search_result()
        results_date = results_page.check_results_date()
        assert results_date == int(date.today().year), "Results date does not match search filter."

    ## Verifies that clicking the top "NASA" logo leads from Image of the day page to homepage.
    def test_logo_link_image_page(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        NasaHomePage(page).go_to_image_of_the_day()
        assert ImageOfTheDayPage(page).verify_logo_link() == URL, f"Logo link does not match '{URL}'."

    ## Goes to "Image of the day" page, extracts the publishing date of the latest uploaded image,
    ## compares to current date using strftime, checks if the latest image was uploaded today.
    def test_image_of_the_day_date(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        NasaHomePage(page).go_to_image_of_the_day()
        image_page = ImageOfTheDayPage(page)
        image_page.click_image_of_the_day()
        image_date = image_page.get_date_image_of_the_day()
        assert image_date == date.today().strftime("%b %d, %Y").upper(), f"The date for the latest 'Image of the day' does not match current date. Latest image upload date is {image_date}"

    ## Opens "Explore" drop-menu, extracts the links into a list, visits each link and checks the result page status,
    ## adds broken links into a list, checks if there are broken links and prints them.
    def test_explore_menu_links_status(self, setup_playwright_nasa):
        page = setup_playwright_nasa
        homepage = NasaHomePage(page)
        links = homepage.get_explore_menu_links()
        broken_links = []
        for link in links:
            response = page.goto(link)
            if response.status >= 400:
                broken_links.append(f"{link} | status: {response.status}")
            # print(f"response status for {link} is {response.status}.")
        assert not broken_links, f"The following links are broken: {broken_links}"
