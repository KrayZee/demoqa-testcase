def pytest_generate_tests(metafunc):
    metafunc.parametrize('browser', metafunc.config.option.browser)


def pytest_addoption(parser):
    parser.addoption('-B', '--browser',
                     dest='browser',
                     action='append',
                     default=['firefox', 'chrome'],
                     help='Browser. Valid options are firefox, ie, safari and chrome')
