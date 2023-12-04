from app.models.planograms import Planograms
import pytest

class TestPlanograms:

    # Creating an instance of Planograms with valid arguments should initialize the object with the correct attributes.
       # Creating an instance of Planograms with valid arguments should initialize the object with the correct attributes.
    def test_valid_arguments_initialization(self, mocker):
        # Arrange
        name = "Planogram 1"
        store = "Store 1"
        date = "2022-01-01"
        img = "planogram1.jpg"
        collection_mock = mocker.Mock()

        # Act
        planogram = Planograms(name, store, date, img, collection_mock)

        # Assert
        assert planogram.name == name
        assert planogram.store == store
        assert planogram.date == date
        assert planogram.img_path == img
        assert planogram._collection == collection_mock

    # Calling the to_dic method should return a dictionary with the correct keys and values.
    def test_to_dic_method(self, mocker):
        # Arrange
        name = "Planogram 1"
        store = "Store 1"
        date = "2022-01-01"
        img = "planogram1.jpg"
        collection_mock = mocker.Mock()
        planogram = Planograms(name, store, date, img, collection_mock)

        # Act
        result = planogram.to_dic()

        # Assert
        assert result == {
            'Nombre': name,
            'Tienda': store,
            'Fecha': date,
            'Ver': img
        }

    # Calling the insert method with valid arguments should insert a document into the collection and return True.
    def test_insert_method_valid_arguments(self, mocker):
        # Arrange
        name = "Planogram 1"
        store = "Store 1"
        date = "2022-01-01"
        img = "planogram1.jpg"
        collection_mock = mocker.Mock()
        planogram = Planograms(name, store, date, img, collection_mock)

        # Act
        result = planogram.insert()

        # Assert
        assert result is True
        collection_mock.insert_one.assert_called_once_with({
            'Nombre': name,
            'Tienda': store,
            'Fecha': date,
            'Ver': img
        })

    # Calling the to_dic method when some attributes are missing should return a dictionary with None values for those attributes.
    def test_to_dic_method_missing_attributes(self, mocker):
        # Arrange
        name = "Planogram 1"
        store = "Store 1"
        date = "2022-01-01"
        img = None
        collection_mock = mocker.Mock()
        planogram = Planograms(name, store, date, img, collection_mock)

        # Act
        result = planogram.to_dic()

        # Assert
        assert result == {
            'Nombre': name,
            'Tienda': store,
            'Fecha': date,
            'Ver': img
        }
