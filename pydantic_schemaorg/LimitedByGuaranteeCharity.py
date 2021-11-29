from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class LimitedByGuaranteeCharity(UKNonprofitType):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that"
     "is limited by guarantee (UK).

    See https://schema.org/LimitedByGuaranteeCharity.

    """

    locals().update({"@type": Field("LimitedByGuaranteeCharity", const=True)})


LimitedByGuaranteeCharity.update_forward_refs()
