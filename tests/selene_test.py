import os
from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss


def test_fill_form():
    browser.open('/automation-practice-form')
    s('.text-center').should(have.text('Practice Form'))

    # Заполнение ФИО
    s('#firstName').should(be.blank).type('Name')
    s('#firstName').should(have.value('Name'))
    s('#lastName').should(be.blank).type('Surname')
    s('#lastName').should(have.value('Surname'))

    # Заполнение почты
    s('#userEmail').should(be.blank).type('fakemail@mail.ru')
    s('#userEmail').should(have.value('fakemail@mail.ru'))

    # Проставление радиокнопки "пол"
    ss('.custom-control-label')[0].click()

    # Заполнение номера телефона
    s('#userNumber').should(be.blank).type('9939998833')
    s('#userNumber').should(have.value('9939998833'))

    # Заполнение блока даты рождения c помощью datepicker
    s('#dateOfBirthInput').should(have.value_containing('May'))
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click()
    s('.react-datepicker__month-select option[value="10"]').click()
    s('.react-datepicker__year-select').click()
    s('.react-datepicker__year-select option[value="1992"]').click()
    s('.react-datepicker__day--003').click()
    s('#dateOfBirthInput').should(have.value_containing('03 Nov 1992'))

    # Выбор предметов математика и история
    s('#subjectsContainer input').should(be.visible).type('Math')
    browser.config.timeout = 5
    s('#subjectsContainer input').should(have.value('Math')).press_tab()
    s('#subjectsContainer input').should(be.visible).type('History')
    browser.config.timeout = 5
    s('#subjectsContainer input').should(have.value('History')).press_tab()

    # Проставление чекбокса "хобби"
    ss('#hobbiesWrapper [class*=checkbox]')[1].click()
    ss('#hobbiesWrapper [class*=checkbox]')[0].click()

    # Загрузка файла
    s('#uploadPicture').send_keys(os.path.abspath('/Users/goncharov/Downloads/picture.jpg'))

    # Заполнение адреса
    s('#currentAddress').should(be.blank).type('Moscow 1, Red Square')
    s('#currentAddress').should(have.value('Moscow 1, Red Square'))

    # Заполнение штата
    s('#state').click()
    s('#state [class$=menu] [class$=option]').should(have.text('NCR')).click()

    # Заполнение города
    s('#city').click()
    s('#city [class$=menu] [class$=option]').should(have.text('Delhi')).click()

    # Подтверждение
    s('#submit').should(have.text('Submit'))
    s('#submit').click()

    # Проверка заполненных данных
    browser.element('.modal-content').element('table').all('tr').all('td')[1::2].should(
        have.exact_texts(
            'Name Surname',
            'fakemail@mail.ru',
            'Male',
            '9939998833',
            '03 November,1992',
            'Maths, History',
            'Reading, Sports',
            'picture.jpg',
            'Moscow 1, Red Square',
            'NCR Delhi'
        ))

