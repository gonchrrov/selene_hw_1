import os
import time

from selene import browser, have, be, command
from selene.support.shared.jquery_style import s, ss


def test_fill_form():
    browser.open('/automation-practice-form')
    s('.text-center').should(have.text('Practice Form'))

    s('#firstName').should(be.blank).type('UserName')
    s('#firstName').should(have.value('UserName'))

    s('#lastName').should(be.blank).type('Surname')
    s('#lastName').should(have.value('Surname'))

    s('#userEmail').should(be.blank).type('fakemail@mail.ru')
    s('#userEmail').should(have.value('fakemail@mail.ru'))

    ss('.custom-control-label')[0].click()

    s('#userNumber').should(be.blank).type('9939998833')
    s('#userNumber').should(have.value('9939998833'))

    s('#dateOfBirthInput').should(have.value_containing('May'))
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click()
    s('.react-datepicker__month-select option[value="10"]').click()
    s('.react-datepicker__year-select').click()
    s('.react-datepicker__year-select option[value="1992"]').click()
    s('.react-datepicker__day--003').click()
    s('#dateOfBirthInput').should(have.value_containing('03 Nov 1992'))

    # Ввод предмета и адреса
    s('#subjectsContainer').click()
    s('#subjectsContainer input').type('Ma').press_tab()

    s('#uploadPicture').send_keys(os.path.abspath('/Users/goncharov/Downloads/picture.jpg'))

    s('#currentAddress').should(be.blank).set_value('Moscow 1, Red Square')
    s('#currentAddress').should(have.value('Moscow 1, Red Square'))

    s('#state').perform(command.js.scroll_into_view).click()
    s('#state [class$=menu] [class$=option]').should(have.text('NCR')).click()

    s('#city').click()
    s('#city [class$=menu] [class$=option]').should(have.text('Delhi')).click()

    s('#submit').should(have.text('Submit'))
    s('#submit').click()
    time.sleep(5)
