from evosnap import constants


class ElectronicCheckingCustomerData:
    def __init__(self, check_data):
        """
        Basic information about the check being processed. This element is Required.
        :param activation: Contains information for activating an account. This is a required element.
        """
        self.__camelcase=constants.ALL_FIELDS
        self.check_data=check_data
