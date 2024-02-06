import allure
# from allure_commons.types import Severity
from selene import browser, have, command


# from model.pages.registration_page import RegistrationPage


# @allure.tag("web")
# @allure.label("owner", "Andrey R")
# @allure.feature("Search")
#
# @allure.severity(Severity.CRITICAL)
# @allure.story("Пользователь может искать Каналы на nuum.ru")
# @allure.title("categories search")
def test_search_by_chanel_name():
    with allure.step("Открываем портал"):
        browser.open('/')

    with ((allure.step("Ищем канал по названию"))):
        browser.element('.header  .search-form input').click().type('boys_talks').element(
            '//*[text()=(" Найти ")]').click()

    with allure.step("Результат поиска содержит раздел Каналы"):
        browser.element('.top-channels h2').should(have.exact_text('Каналы'))
    with allure.step("Результат поиска содержит искомый канал"):
        browser.element('.top-channels .top-channel-card__name').should(have.exact_text('boys_talks'))


