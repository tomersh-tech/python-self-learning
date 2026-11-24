"""Exercise 5.2 - Piece of cake.

Calculate how much it costs to buy the ingredients of a recipe.
"""
from typing import Optional

GRAMS_PER_PRICE_UNIT = 100


def piece_of_cake(
    prices: dict[str, float],
    optionals: Optional[list[str]] = None,
    **grams_needed: float,
) -> float:
    """Return the total price of the ingredients needed for a recipe.

    Args:
        prices: Maps each ingredient to its price per 100 grams.
        optionals: Ingredients to skip, so we don't buy them at all.
        **grams_needed: How many grams to buy of each ingredient,
            for example chocolate=200.

    Returns:
        The total price of all the ingredients that are not skipped.

    Raises:
        ValueError: If an ingredient that isn't skipped has no amount.
    """
    skipped = set(optionals or [])
    total_price = 0.0
    for ingredient, price_per_100_grams in prices.items():
        if ingredient in skipped:
            continue
        if ingredient not in grams_needed:
            raise ValueError(f"Missing amount for ingredient '{ingredient}'.")
        grams = grams_needed[ingredient]
        total_price += price_per_100_grams * grams / GRAMS_PER_PRICE_UNIT
    return total_price


if __name__ == "__main__":
    print(piece_of_cake({"chocolate": 18, "milk": 8}, chocolate=200, milk=100))
    print(piece_of_cake(
        {"chocolate": 18, "milk": 8}, optionals=["milk"], chocolate=300
    ))
    print(piece_of_cake({}))
