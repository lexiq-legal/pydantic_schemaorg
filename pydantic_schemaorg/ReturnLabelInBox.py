from pydantic import Field
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelInBox(ReturnLabelSourceEnumeration):
    """Specifies that a return label will be provided by the seller in the shipping box.

    See https://schema.org/ReturnLabelInBox.

    """

    locals().update({"@type": Field("ReturnLabelInBox", const=True)})


ReturnLabelInBox.update_forward_refs()
