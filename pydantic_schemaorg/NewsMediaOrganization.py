from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization


class NewsMediaOrganization(Organization):
    """A News/Media organization such as a newspaper or TV station.

    See https://schema.org/NewsMediaOrganization.

    """

    actionableFeedbackPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "about public engagement activities (for news media, the newsroom’s), including involving"
     "the public - digitally or otherwise -- in coverage decisions, reporting and activities"
     "after publication.",
    )
    diversityPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]."
     "For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity"
     "policy on both staffing and sources, typically providing staffing data.",
    )
    ethicsPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic"
     "and publishing practices, or of a [[Restaurant]], a page describing food source policies."
     "In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement"
     "describing the personal, organizational, and corporate standards of behavior expected"
     "by the organization.",
    )
    correctionsPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing"
     "(in news media, the newsroom’s) disclosure and correction policy for errors.",
    )
    missionCoveragePrioritiesPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For a [[NewsMediaOrganization]], a statement on coverage priorities, including any"
     "public agenda or stance on issues.",
    )
    ownershipFundingInfo: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a description of organizational ownership structure; funding and grants. In a news/media"
     "setting, this is with particular reference to editorial independence. Note that the"
     "[[funder]] is also available and can be used to make basic funder information machine-readable.",
    )
    noBylinesPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "explaining when authors of articles are not named in bylines.",
    )
    verificationFactCheckingPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Disclosure about verification and fact-checking processes for a [[NewsMediaOrganization]]"
     "or other fact-checking [[Organization]].",
    )
    diversityStaffingReport: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a report on staffing diversity issues. In a news context this might be for example ASNE"
     "or RTDNA (US) reports, or self-reported.",
    )
    unnamedSourcesPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about"
     "policy on use of unnamed sources and the decision process required.",
    )
    masthead: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For a [[NewsMediaOrganization]], a link to the masthead page or a page listing top editorial"
     "management.",
    )
    locals().update({"@type": Field("NewsMediaOrganization", const=True)})


NewsMediaOrganization.update_forward_refs()
