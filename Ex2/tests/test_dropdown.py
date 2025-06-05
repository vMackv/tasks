import pytest
from Ex2.resources.dropdown import DropdownElement


@pytest.fixture
def driver(mocker):
    return mocker.Mock()


@pytest.fixture
def wait(mocker):
    return mocker.Mock()


class TestDropdownElement:
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait):
        self.dropdown = DropdownElement(driver, wait)

    def test_switch_to_iframe(self, wait, driver):
        iframe = wait.until.return_value
        self.dropdown.switch_to_iframe()
        wait.until.assert_called_once()
        driver.switch_to.frame.assert_called_once_with(iframe)

    def test_switch_to_default(self, driver):
        self.dropdown.switch_to_default()
        driver.switch_to.default_content.assert_called_once()

    def test_scroll_down(self, mocker, wait, driver):
        wait.until.side_effect = [mocker.Mock(), mocker.Mock()]
        self.dropdown.scroll_down()
        driver.execute_script.assert_called_once()

    def test_change_theme(self, mocker, wait):
        btn1, btn2 = mocker.Mock(), mocker.Mock()
        wait.until.side_effect = [btn1, btn2]
        self.dropdown.change_theme()
        btn1.click.assert_called_once()
        btn2.click.assert_called_once()
