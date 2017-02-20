from evosnap import constants


class ElectronicCheckingTransaction:
    def __init__(self, electronic_checking_tender_data, electronic_checking_transaction_data,
                 electronic_checking_customer_data=None):
        """
        Basic information about the check being processed. This element is Required.
        :param activation: Contains information for activating an account. This is a required element.
        """
        self.__camelcase=constants.ALL_FIELDS
        self.electronic_checking_customer_data=electronic_checking_customer_data
        self.electronic_checking_tender_data=electronic_checking_tender_data
        self.electronic_checking_transaction_data=electronic_checking_transaction_data
