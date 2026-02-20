from difflib import SequenceMatcher


class IndustryBrain:
    """
    Detects similarity between industries.
    Enables cross-industry learning.
    """

    # Initial knowledge map (expand over time)
    INDUSTRY_RELATIONS = {
        "dentist": ["clinic", "healthcare", "cosmetic"],
        "real estate": ["builder", "property", "construction"],
        "salon": ["beauty", "spa", "cosmetics"],
        "gym": ["fitness", "wellness", "health"],
        "restaurant": ["cafe", "food", "cloud kitchen"],
        "ecommerce": ["retail", "fashion", "online store"]
    }

    @staticmethod
    def similarity(a: str, b: str):
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    @staticmethod
    def get_related_industries(industry: str):

        related = set()

        # Direct mapping
        for key, values in IndustryBrain.INDUSTRY_RELATIONS.items():
            if IndustryBrain.similarity(industry, key) > 0.6:
                related.add(key)
                related.update(values)

        # include itself
        related.add(industry)

        return list(related)
