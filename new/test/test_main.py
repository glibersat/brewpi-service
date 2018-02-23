"""
Tests brewblox_service.__main__.py
"""

from brewblox_service import __main__ as main


TESTED = main.__name__


def test_main(loop, mocker):
    create_mock = mocker.patch(TESTED + '.service.create')
    furnish_mock = mocker.patch(TESTED + '.service.furnish')
    run_mock = mocker.patch(TESTED + '.service.run')
    app_mock = create_mock.return_value

    main.main()

    assert create_mock.call_count == 1
    furnish_mock.assert_called_once_with(app_mock)
    run_mock.assert_called_once_with(app_mock)