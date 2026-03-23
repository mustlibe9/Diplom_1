from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from dataclasses import dataclass
from typing import List
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@dataclass
class ReceiptTestCase:
    bun: Bun
    ingredients: List[Ingredient]
    expected_receipt: str


_RECEIPT_BUN_ONLY = (
    "(==== White Bun ====)\n" "(==== White Bun ====)\n" "\n" "Price: 200.0"
)

_RECEIPT_WITH_SAUCE_AND_FILLING = (
    "(==== White Bun ====)\n"
    "= sauce hot sauce =\n"
    "= filling cutlet =\n"
    "(==== White Bun ====)\n"
    "\n"
    "Price: 350.0"
)

_RECEIPT_WITH_BEEF = (
    "(==== White Bun ====)\n"
    "= filling beef =\n"
    "(==== White Bun ====)\n"
    "\n"
    "Price: 230.0"
)


RECEIPT_TEST_CASES = (
    ReceiptTestCase(
        bun=Bun("White Bun", 100.0),
        ingredients=(),
        expected_receipt=_RECEIPT_BUN_ONLY,
    ),
    ReceiptTestCase(
        bun=Bun("White Bun", 100.0),
        ingredients=(
            Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 50.0),
        ),
        expected_receipt=_RECEIPT_WITH_SAUCE_AND_FILLING,
    ),
    ReceiptTestCase(
        bun=Bun("White Bun", 100.0),
        ingredients=(Ingredient(INGREDIENT_TYPE_FILLING, "beef", 30.0),),
        expected_receipt=_RECEIPT_WITH_BEEF,
    ),
)
