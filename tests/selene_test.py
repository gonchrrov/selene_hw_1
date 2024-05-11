import os
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
    s('//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[11]').click()
    s('//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[93]').click()
    s('.react-datepicker__day--003').click()
    s('#dateOfBirthInput').should(have.value_containing('03 Nov 1992'))

    s('#subjectsContainer').click()
    s('#subjectsContainer').element('input').type('Ma').press_tab()

    s('//*[@id="hobbiesWrapper"]/div[2]/div[1]/label').click()
    s('//*[@id="hobbiesWrapper"]/div[2]/div[2]/label').click()

    s('#uploadPicture').send_keys(os.path.abspath('/Users/goncharov/Downloads/picture.jpg'))

    s('#currentAddress').should(be.blank).set_value('Moscow 1, Red Square')
    s('#currentAddress').should(have.value('Moscow 1, Red Square'))

    s('#state').perform(command.js.scroll_into_view).click()
    s('#state').element('[class$=menu]').all('[class$=option]').element_by(have.text('NCR')).click()

    s('#city').click()
    s('#city').element('[class$=menu]').all('[class$=option]').element_by(have.text('Delhi')).click()
