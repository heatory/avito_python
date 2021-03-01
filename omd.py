steps = [
    {
        'question': 'Утка-маляр решила погулять. '
                    'Взять ей зонтик? ',
        'positive': 'Теперь уточка точно не промокнет :)',
        'negative': 'Ну и ладненько, вроде дождика не обещали.',
        'positive_link': 1,
        'negative_link': 2,
    },
    {
        'question': 'Дождика не было, но при этом очень сильно печёт солнце. '
                    'Открыть ей зонтик? ',
        'positive': 'Отлично, уточке не было столь жарко и она не обгорела,',
        'negative': 'Уточке стало невероятно жарко.'
                    'Она поймала солнечный удар и её отвели домой',
        'positive_link': 3,
        'negative_link': 9999,
    },
    {
        'question': 'Как назло пошёл дождик. '
                    'Бежать уточке домой? ',
        'positive': 'Уточка побежала домой.',
        'negative': 'Уточке зашла в магазин, чтобы переждать дождик.',
        'positive_link': 9999,
        'negative_link': 7,
    },
    {
        'question': 'По пути уточке встретился парк. '
                    'Зайти в парк? ',
        'positive': 'Уточка зашла в парк и пошла по главной аллее.',
        'negative': 'Уточке прошла мимо.',
        'positive_link': 5,
        'negative_link': 4,
    },
    {
        'question': 'По пути уточке встретился парк. '
                    'Зайти в парк? ',
        'positive': 'Уточка зашла в парк и пошла по главной аллее.',
        'negative': 'Уточке прошла мимо.',
        'positive_link': 5,
        'negative_link': 5,
    },
    {
        'question': 'Уточка увидела киоск с мороженым. '
                    'Купить пломбир? ',
        'positive': 'Уточка объелась пломбиром и пошла домой.',
        'negative': '',
        'positive_link': 9999,
        'negative_link': 6,
    },
    {
        'question': 'Купить фруктовый лёд? ',
        'positive': 'Фруктовый лёд был обжигающе холодным. '
                    'У уточки заболело горло и она пошла домой.',
        'negative': 'Уточка ничего не купила, расстроилась и пошла домой',
        'positive_link': 9999,
        'negative_link': 9999,
    },
    {
        'question': 'Дождик закончился. '
                    'Идти гулять дальше? ',
        'positive': 'Уточка вышла из магазина и пошла гулять дальше.',
        'negative': 'Уточке пошла домой.',
        'positive_link': 4,
        'negative_link': 9999,
    }
]


def go(step_number):
    print(steps[step_number]['question'])
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        print(steps[step_number]['positive'])
        return steps[step_number]['positive_link']
    else:
        print(steps[step_number]['negative'])
        return steps[step_number]['negative_link']


if __name__ == '__main__':
    i = 0
    while i < len(steps):
        i = go(i)
    print(
        'Уточка дома и ложится спать'
    )
