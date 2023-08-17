from unittest import TestCase, main
from hash_table import HashTable


class TestHashTable(TestCase):
    def setUp(self) -> None:
        self.table = HashTable()

    def test_correct_initialization(self):
        self.assertEqual(4, self.table._HashTable__max_capacity)
        self.assertEqual([None] * 4, self.table._HashTable__keys)
        self.assertEqual([None] * 4, self.table._HashTable__values)
        self.assertEqual(0, self.table._HashTable__length)

    def test_add_expect_correct_addition_of_key_value_pair(self):
        self.table.add("name", "Gosho")
        self.assertEqual("Gosho", self.table["name"])

    def test_get_method_without_message_returns_none_on_non_existing_el(self):
        result = self.table.get("non existing")
        self.assertEqual(None, result)

    def test_get_method_raises(self):
        result = self.table.get("no key", "key does not exist")
        self.assertEqual("key does not exist", result)

    def test_get_method_correctly(self):
        self.table.add("name", "Gosho")

        self.assertEqual("Gosho", self.table.get("name"))

    def test__get_item(self):
        self.table["name"] = "Pesho"

        self.assertEqual("Pesho", self.table["name"])

    def test__get_item__invalid_key_raises(self):
        with self.assertRaises(KeyError) as ke:
            result = self.table["not existing"]
        self.assertEqual("'not existing is not in the hash table'", str(ke.exception))

    def test_correct_override_value(self):
        self.table["name"] = "peter"
        self.table["name"] = "pesho"
        self.assertEqual("pesho", self.table["name"])
        self.assertEqual(1, len(self.table))

    def test_resize_when_table_is_fill(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25
        self.table["is_pet_owner"] = True
        self.table["is_driver"] = False
        self.assertEqual(4, len(self.table))
        self.assertEqual(4, self.table._HashTable__max_capacity)

        self.table["is_single"] = False
        self.assertEqual(5, len(self.table))
        self.assertEqual(8, self.table._HashTable__max_capacity)

    #
    def test_index_creation_on_collision_when_index_if_out_of_range_expect_success(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25
        self.table["is_pet_owner"] = True

        result = self.table._HashTable__calc_index("is_driver")

        self.assertEqual(0, result)

    def test__str__(self):
        self.table["name"] = "Peter"
        self.table["age"] = 25
        expected = "{name: Peter, age: 25}"
        result = str(self.table)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
