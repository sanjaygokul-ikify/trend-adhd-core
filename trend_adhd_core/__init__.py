from typing import Any
import logging

class TrendADHDCoreError(Exception):
    pass

class InvalidDataError(TrendADHDCoreError):
    pass

class TrendADHDCore:
    def __init__(self) -> None:
        pass

    def process_data(self, data: Any) -> None:
        try:
            # Add data processing logic here
            logging.info('Data processed successfully')
        except InvalidDataError as e:
            # Handle InvalidDataError
            logging.error(f'Invalid data: {e}')
            raise
        except Exception as e:
            # Handle other exceptions
            logging.error(f'An error occurred: {e}')
            raise