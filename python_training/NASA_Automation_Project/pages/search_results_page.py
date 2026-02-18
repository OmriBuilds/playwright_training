

class SearchResultsPage:
    def __init__(self, page):
        self.page = page

    def get_search_results_title(self):
        return self.page.locator("h1.page-title")

    def extract_results_sum(self):
        results_sum_text = self.page.locator("h2.hds-a11y-strong").inner_text()
        results_sum_num = results_sum_text.split(" ")[0]
        return int(results_sum_num)

    def filter_search_results(self):
        self.page.locator("#last-yearlast-year").click()
        self.page.locator("button[class='usa-button hds-button filter']").click()

    def click_search_result(self):
        self.page.locator("li.hds-search-result-position a").first.click()

    def check_results_date(self):
        date = self.page.locator("div.hds-footer-meta-value").first.inner_text()
        year = date.split(", ")[1]
        return int(year)

