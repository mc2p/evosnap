from evosnap import constants


class ElectronicCheckingCustomerData:
    def __init__(self, additional_billing_data=None):
        """
        Basic information about the check being processed. This element is Required.
        :param activation: Contains information for activating an account. This is a required element.
        """
        self.__camelcase=constants.ALL_FIELDS
        self.additional_billing_data=additional_billing_data
