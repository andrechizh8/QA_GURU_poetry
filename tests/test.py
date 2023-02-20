from selene.support.shared import browser
from selene.support.conditions import have, be


def test_1():
    browser.open('https://www.google.com/')
    browser.element("[name='q']").should(be.blank).type('qa').press_enter()
    browser.element("[class='hdtb-mitem hdtb-msel']").should(have.text('Все'))
