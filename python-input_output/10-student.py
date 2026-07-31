#!/usr/bin/python3
"""Module that defines a Student class with a filterable to_json
method."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to
                retrieve. If not a list of strings, all attributes
                are retrieved.
        """
        is_valid_list = isinstance(attrs, list)
        if is_valid_list:
            is_valid_list = all(isinstance(a, str) for a in attrs)
        if is_valid_list:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
