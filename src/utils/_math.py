import math


class _math:
    @staticmethod
    def int_ceil(num: float) -> int:
        """
        >>> _math.int_ceil(10 / 3)
        4

        Args:
            num:

        Returns:

        """
        return math.ceil(num)

    @staticmethod
    def decimal_ceil(
            num: float,
            places: int = 2
    ) -> float:
        """
        >>> _math.decimal_ceil(3.14159)
        3.15

        Args:
            num:
            places:

        Returns:

        """
        if places >= 0:
            scale = 10.0 ** places
            return math.ceil(num * scale) / scale
        else:
            raise ValueError(
                f"Invalid value for 'places': "
                f"Expected `int` and >= 0, "
                f"but got value: {places!r}"
            )

    @staticmethod
    def format_number(
            number: int | float | str,
            places: int = 2
    ) -> str:
        """
        >>> _math.format_number(3.1)
        '3.10'

        Args:
            number:
            places:

        Returns:

        """
        integer_str, decimal_str = str(float(number)).split(".")
        decimal_str = (decimal_str + "0" * (places - len(decimal_str)))[:places]
        number_str = ".".join([integer_str, decimal_str])
        return number_str


__all__ = [
    "_math"
]
