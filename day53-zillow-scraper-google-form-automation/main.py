from soup import Parser
from driver import Driver

def get_parsed_data(parser):
    unformatted_data = parser.get_data()
    data = parser.parse_data(unformatted_data)
    return data

def main():
    driver = Driver()
    parser = Parser()
    formatted_data = get_parsed_data(parser)
    driver.record_data(formatted_data)
    driver.driver.close()

main()