from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DeliveryMethod(Enumeration):
    """A delivery method is a standardized procedure for transferring the product or service"
     "to the destination of fulfillment chosen by the customer. Delivery methods are characterized"
     "by the means of transportation used, and by the organization or group that is the contracting"
     "party for the sending organization or person. Commonly used values: * http://purl.org/goodrelations/v1#DeliveryModeDirectDownload"
     "* http://purl.org/goodrelations/v1#DeliveryModeFreight * http://purl.org/goodrelations/v1#DeliveryModeMail"
     "* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet * http://purl.org/goodrelations/v1#DeliveryModePickUp"
     "* http://purl.org/goodrelations/v1#DHL * http://purl.org/goodrelations/v1#FederalExpress"
     "* http://purl.org/goodrelations/v1#UPS

    See https://schema.org/DeliveryMethod.

    """

    locals().update({"@type": Field("DeliveryMethod", const=True)})


DeliveryMethod.update_forward_refs()
