from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness
from pydantic_schemaorg.CivicStructure import CivicStructure


class Campground(LodgingBusiness, CivicStructure):
    """A camping site, campsite, or [[Campground]] is a place used for overnight stay in the"
     "outdoors, typically containing individual [[CampingPitch]] locations. In British"
     "English a campsite is an area, usually divided into a number of pitches, where people"
     "can camp overnight using tents or camper vans or caravans; this British English use of"
     "the word is synonymous with the American English expression campground. In American"
     "English the term campsite generally means an area where an individual, family, group,"
     "or military unit can pitch a tent or park a camper; a campground may contain many campsites"
     "(Source: Wikipedia see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite))."
     "See also the dedicated [document on the use of schema.org for marking up hotels and other"
     "forms of accommodations](/docs/hotels.html).

    See https://schema.org/Campground.

    """

    locals().update({"@type": Field("Campground", const=True)})


Campground.update_forward_refs()
