from evosnap import constants


class ReturnInformation:
    def __init__(self, return_code=None, return_date=None, return_reason=None):
        """
        Contains information regarding the reason the bank rejected the transaction. This element is Optional.
        :param activation: Contains information for activating an account. This is a required element.
        """
        self.__camelcase=constants.ALL_FIELDS
        self.return_code=return_code
        self.return_date=return_date
        self.return_reason=return_reason
