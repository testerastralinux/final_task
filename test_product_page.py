import pytest
from .pages.product_page import ProductPage


links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{N}" for N in range(10)]
links[7] = pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                        marks=pytest.mark.xfail(reason="Bug"))


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_name_in_message_add_product_to_basket()
    page.should_be_right_price_in_message_add_product_to_basket()
