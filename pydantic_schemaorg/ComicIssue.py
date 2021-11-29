from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PublicationIssue import PublicationIssue


class ComicIssue(PublicationIssue):
    """Individual comic issues are serially published as part of a larger series. For the sake"
     "of consistency, even one-shot issues belong to a series comprised of a single issue."
     "All comic issues can be uniquely identified by: the combination of the name and volume"
     "number of the series to which the issue belongs; the issue number; and the variant description"
     "of the issue (if any).

    See https://schema.org/ComicIssue.

    """

    colorist: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The individual who adds color to inked drawings.",
    )
    artist: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The primary artist for a work in a medium other than pencils or digital line art--for example,"
     "if the primary artwork is done in watercolors or digital paints.",
    )
    letterer: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The individual who adds lettering, including speech balloons and sound effects, to"
     "artwork.",
    )
    variantCover: Optional[Union[List[str], str]] = Field(
        None,
        description="A description of the variant cover for the issue, if the issue is a variant printing. For"
     "example, \"Bryan Hitch Variant Cover\" or \"2nd Printing Variant\".",
    )
    penciler: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The individual who draws the primary narrative artwork.",
    )
    inker: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The individual who traces over the pencil drawings in ink after pencils are complete.",
    )
    locals().update({"@type": Field("ComicIssue", const=True)})


ComicIssue.update_forward_refs()
