from evosnap import constants


class CheckData:
    def __init__(self, account_number, owner_type, routing_number=None, user_type=None, check_number=None):
        """
        Basic information about the check being processed. This element is Required.
        :param activation: Contains information for activating an account. This is a required element.
        """
        self.__camelcase=constants.ALL_FIELDS
        self.account_number=account_number
        self.check_number=check_number
        self.owner_type=owner_type
        self.routing_number=routing_number
        self.user_type=user_type
