import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from test_receipts_input_data import RECEIPT_TEST_CASES


class TestBurger:

    def test_init_bun_is_correct(self, empty_burger):
        assert empty_burger.bun is None
        assert empty_burger.ingredients == []

    def test_set_buns(self, empty_burger, default_bun):
        empty_burger.set_buns(default_bun)
        assert empty_burger.bun == default_bun

    def test_add_one_ingredient(self, empty_burger, default_filling):
        empty_burger.add_ingredient(default_filling)
        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == default_filling

    def test_add_multiple_ingredients(
        self, empty_burger, default_sauce, default_filling
    ):
        empty_burger.add_ingredient(default_sauce)
        empty_burger.add_ingredient(default_filling)
        assert empty_burger.ingredients == [default_sauce, default_filling]

    def test_remove_ingredient_by_index(
        self, empty_burger, default_sauce, default_filling
    ):
        empty_burger.add_ingredient(default_sauce)
        empty_burger.add_ingredient(default_filling)

        empty_burger.remove_ingredient(0)

        assert len(empty_burger.ingredients) == 1
        assert empty_burger.ingredients[0] == default_filling

    def test_remove_last_ingredient(self, empty_burger, default_filling):
        empty_burger.add_ingredient(default_filling)
        empty_burger.remove_ingredient(0)
        assert empty_burger.ingredients == []

    def test_move_ingredient_from_first_to_last(
        self, empty_burger, default_sauce, default_filling, cheese_filling
    ):
        empty_burger.add_ingredient(default_sauce)
        empty_burger.add_ingredient(default_filling)
        empty_burger.add_ingredient(cheese_filling)

        empty_burger.move_ingredient(0, 2)

        assert empty_burger.ingredients == [
            default_filling,
            cheese_filling,
            default_sauce,
        ]

    def test_move_ingredient_from_last_to_first(
        self, empty_burger, default_sauce, default_filling, cheese_filling
    ):
        empty_burger.add_ingredient(default_sauce)
        empty_burger.add_ingredient(default_filling)
        empty_burger.add_ingredient(cheese_filling)

        empty_burger.move_ingredient(2, 0)

        assert empty_burger.ingredients == [
            cheese_filling,
            default_sauce,
            default_filling,
        ]

    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected_total",
        [
            (197.1, [], 394.2),
            (0.0, [10.7], 10.7),
            (100.0, [50.0, 25.0, 30.0], 305.0),
            (99.99, [0.01], 199.99),
        ],
    )
    def test_get_price_correct(
        self, empty_burger, bun_price, ingredient_prices, expected_total
    ):
        empty_burger.set_buns(Bun("Bun", bun_price))
        for price in ingredient_prices:
            empty_burger.add_ingredient(
                Ingredient(INGREDIENT_TYPE_FILLING, "some_filling_name", price)
            )
        assert empty_burger.get_price() == pytest.approx(expected_total, abs=0.01)

    @pytest.mark.parametrize(
        "receipt_case",
        RECEIPT_TEST_CASES,
    )
    def test_get_receipt(self, empty_burger, receipt_case):
        empty_burger.set_buns(receipt_case.bun)

        for ingredient in receipt_case.ingredients:
            empty_burger.add_ingredient(ingredient)

        assert empty_burger.get_receipt() == receipt_case.expected_receipt
