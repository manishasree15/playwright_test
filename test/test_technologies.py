
from playwright.sync_api._generated import Page
import pytest

from pages.technologies import technology

@pytest.mark.smoke 
def test_technology(page: Page):
    technologys=technology(page)
    technologys.ecomm_options()
@pytest.mark.smoke 
def test_mobileapp(page: Page):
    technologys=technology(page)
    technologys.mobileapp_options()
@pytest.mark.smoke 
def test_Ai(page: Page):
    technologys=technology(page)
    technologys.Ai_Options()
