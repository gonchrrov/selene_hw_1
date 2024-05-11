import os

from selene import browser, have
from selene.support.shared.jquery_style import s, ss


def test_fill_form():
    browser.open('/automation-practice-form')
    s('.text-center').should(have.text('Practice Form'))

    # Заполнение ФИО
    s('#firstName').type('Name')
    s('#lastName').type('Surname')

    # Заполнение почты
    s('#userEmail').type('fakemail@mail.ru')

    # Проставление радиокнопки "пол"
    ss('.custom-control-label')[0].click()

    # Заполнение номера телефона
    s('#userNumber').type('9939998833')

    # Заполнение блока даты рождения c помощью date-picker
    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click()
    s('.react-datepicker__month-select option[value="10"]').click()
    s('.react-datepicker__year-select').click()
    s('.react-datepicker__year-select option[value="1992"]').click()
    s('.react-datepicker__day--003').click()

    # Выбор предметов математика и история
    s('#subjectsInput').type('Maths').press_tab()

    # Проставление чекбокса "хобби"
    ss('#hobbiesWrapper [class*=checkbox]')[0].click()
    ss('#hobbiesWrapper [class*=checkbox]')[1].click()

    # Загрузка файла
    s('#uploadPicture').send_keys(os.path.abspath('./pics/picture.jpg'))

    # Заполнение адреса
    s('#currentAddress').type('Moscow 1, Red Square')

    # Заполнение штата
    s('#state').click()
    s('#state').s('[class$=option]').should(have.text('NCR')).click()

    # Заполнение города
    s('#city').click()
    s('#city').s('[class$=option]').should(have.text('Delhi')).click()

    # Подтверждение
    s('#submit').click()

    # Проверка заполненных данных
    s('.modal-content').s('table').ss('tr').all('td').even.should(
        have.exact_texts(
            'Name Surname',
            'fakemail@mail.ru',
            'Male',
            '9939998833',
            '03 November,1992',
            'Maths',
            'Sports, Reading',
            'picture.jpg',
            'Moscow 1, Red Square',
            'NCR Delhi'
        )
    )
