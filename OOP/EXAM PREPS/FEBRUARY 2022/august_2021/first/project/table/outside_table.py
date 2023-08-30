from project.table.table import Table


class OutsideTable(Table):
    ...

    def free_table_info(self):
        if not self.is_reserved:
            return (f"Table: {self.table_number}\n"
                    f"Type: {self.__class__.__name__}\n"
                    f"Capacity: {self.capacity}\n")



