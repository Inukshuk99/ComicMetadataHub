"""
ComicMetadataHub Identity Resolver

Matches comic records across metadata sources.
"""


class IdentityMatchResult:
    """
    Result of identity matching.
    """



    def __init__(
        self,
        matched=False,
        score=0,
        reasons=None,
        confidence=None,
        decision=None
    ):

        self.matched = matched

        self.score = score

        self.reasons = reasons or []

        self.confidence = confidence or "No Match"

        self.decision = decision or "IGNORE"



    def confidence_level(self):

        return self.confidence



    def action(self):

        return self.decision





class IdentityResolver:
    """
    Determines whether two comic records
    represent the same comic.
    """



    def resolve(
        self,
        source,
        candidate
    ):

        score = 0

        reasons = []



        if (
            source.get("identifier")
            and
            source.get("identifier")
            ==
            candidate.get("identifier")
        ):

            score += 100

            reasons.append(
                "Identifier match"
            )



        if (
            source.get("publisher")
            and
            source.get("publisher")
            ==
            candidate.get("publisher")
        ):

            score += 20

            reasons.append(
                "Publisher match"
            )



        if (
            source.get("title")
            and
            source.get("title")
            ==
            candidate.get("title")
        ):

            score += 40

            reasons.append(
                "Title match"
            )



        if (
            source.get("series")
            and
            source.get("series")
            ==
            candidate.get("series")
        ):

            score += 40

            reasons.append(
                "Series match"
            )



        if (
            source.get("volume")
            and
            source.get("volume")
            ==
            candidate.get("volume")
        ):

            score += 20

            reasons.append(
                "Volume match"
            )



        if (
            source.get("issue")
            and
            source.get("issue")
            ==
            candidate.get("issue")
        ):

            score += 40

            reasons.append(
                "Issue match"
            )



        if (
            source.get("edition")
            and
            source.get("edition")
            ==
            candidate.get("edition")
        ):

            score += 10

            reasons.append(
                "Edition match"
            )



        if score >= 150:

            confidence = "Strong Match"

            decision = "AUTO_APPLY"



        elif score >= 100:

            confidence = "Possible Match"

            decision = "REVIEW"



        else:

            confidence = "No Match"

            decision = "IGNORE"



        return IdentityMatchResult(

            matched=score >= 100,

            score=score,

            reasons=reasons,

            confidence=confidence,

            decision=decision

        )
