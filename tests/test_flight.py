import pytest
from Ixigo_Login_Framework.pages.flight_search_page import FlightSearchPage
from Ixigo_Login_Framework.utilities.read_excel import get_flight_data


@pytest.mark.parametrize("from_city,to_city",get_flight_data())
def test_flight_search(driver, from_city, to_city):
    flight = FlightSearchPage(driver)

    flight.enter_from_location(from_city)
    flight.enter_to_location(to_city)
    flight.click_departure_date()
    flight.click_search()

    assert flight.verify_search_results()