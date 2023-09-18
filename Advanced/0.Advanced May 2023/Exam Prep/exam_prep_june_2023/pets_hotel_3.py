def accommodate_new_pets(capacity, weight_max, *pets):
    pets_count = {}
    shame = False
    for pet in pets:
        if capacity <=0:
            shame = True
            break
        if pet[1] > weight_max:
            continue

        pets_count[pet[0]] = pets_count.get(pet[0], 0) + 1
        capacity -= 1
    res=[f"{pet}: {number}\n" for pet,number in sorted(pets_count.items())]



    if not shame:  # Check if there are no pets
        return (f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:\n"
                f"{''.join(res)}")
    if shame:
        return f"You did not manage to accommodate all pets!\nAccommodated pets:\n{''.join(res)}"

from unittest import TestCase, main


class Test(TestCase):
    def test_accommodate_pets(self):
        result = accommodate_new_pets(
            10,
            10.0,
            ("cat", 5.8),
            ("dog", 10.5),
            ("parrot", 0.8),
            ("cat", 3.1),
        )

        self.assertEqual(
            result.strip(),
            """All pets are accommodated! Available capacity: 7.
Accommodated pets:
cat: 2
parrot: 1""")


if __name__ == '__main__':
    main()