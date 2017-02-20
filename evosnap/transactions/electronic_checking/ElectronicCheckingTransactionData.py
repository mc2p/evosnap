from evosnap import constants


class ElectronicCheckingTransactionData:
    def __init__(self, account_number, owner_type, routing_number=None, user_type=None, check_number=None):
        """
        Basic information about the check being processed. This element is Required.
        :param activation: Contains information for activating an account. This is a required element.
        """
        self.__camelcase=constants.ALL_FIELDS
        self.effective_date=account_number
        self.is_recurring=check_number
        self.payee_email=owner_type
        self.payee_id=routing_number
        self.s_e_c_code=user_type
        self.service_type=user_type
        self.transaction_type=user_type
