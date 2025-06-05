import pytest
from Ex2.resources.context_menu import ContextMenu


@pytest.fixture
def driver(mocker):
    return mocker.Mock()


@pytest.fixture
def wait(mocker):
    return mocker.Mock()


@pytest.fixture
def actions(mocker):
    return mocker.Mock()


class TestContextMenu:

    # Setup
    @pytest.fixture(autouse=True)
    def setup(self, driver, wait, actions):
        self.context_menu = ContextMenu(driver, wait, actions)

    # Tests
    def test_switch_to_iframe(self, wait, driver):
        iframe = wait.until.return_value
        self.context_menu.switch_to_iframe()
        wait.until.assert_called_once()
        driver.switch_to.frame.assert_called_once_with(iframe)

    def test_switch_to_default(self, driver):
        self.context_menu.switch_to_default()
        driver.switch_to.default_content.assert_called_once()

    def test_underline_text(self, mocker, wait, actions):
        side_effect_mocks = [mocker.Mock() for _ in range(4)]
        wait.until.side_effect = side_effect_mocks
        self.context_menu.underline_text()
        actions.context_click.assert_called_once()
        actions.move_to_element.assert_called_once()
        side_effect_mocks[-1].click.assert_called_once()
