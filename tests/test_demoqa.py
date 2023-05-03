from src.DemoQAPages import SiteHelper


def test_demoqa(browser):
    demoqa_page = SiteHelper(browser, base_url='https://demoqa.com')
    demoqa_page.go_to_site()
    demoqa_page.click_elements_button()
    demoqa_page.select_checkbox_in_menu()
    demoqa_page.expand_home()
    demoqa_page.expand_downloads()
    demoqa_page.check_wordfile()
    selection = demoqa_page.check_result()
    assert 'You have selected :\nwordFile' in selection
