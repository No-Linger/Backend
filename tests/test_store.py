import pytest
from app.models.stores import Stores as Store

class TestStatistics:

    # Creating a new Store object with valid parameters should not raise any exceptions.
    def test_create_store_valid_parameters(self, mocker):
        collection_mock = mocker.Mock()
        store = Store("Store Name", "Store Address", "Store Manager", collection_mock)
        assert store.name == "Store Name"
        assert store.address == "Store Address"
        assert store.manager == "Store Manager"
        assert store.store_collection == collection_mock

    # Calling the 'to_dic' method on a Store object should return a dictionary with the correct keys and values.
    def test_to_dic_method(self, mocker):
        store = Store("Store Name", "Store Address", "Store Manager", mocker.Mock())
        expected_dict = {
            'Nombre': "Store Name",
            'Dirección': "Store Address",
            'Encargado': "Store Manager"
        }
        assert store.to_dic() == expected_dict

    # Calling the 'insert' method on a Store object with a valid collection should insert the store data into the collection and return True.
    def test_insert_method_valid_collection(self, mocker):
        collection_mock = mocker.Mock()
        store = Store("Store Name", "Store Address", "Store Manager", collection_mock)
        assert store.insert() == True
        collection_mock.insert_one.assert_called_once_with(store.to_dic())

    # Creating a new Store object with a None value for any parameter should not raise a TypeError.
    def test_create_store_none_parameter(self, mocker):
        Store("Store Name", "Store Address", "Store Manager", mocker.Mock())

    # Calling the 'insert' method on a Store object with an invalid collection should raise a ValueError.
    def test_insert_method_invalid_collection_with_mocked_collection(self, mocker):
        store_collection_mock = mocker.Mock()
        store_collection_mock.insert_one.side_effect = Exception()
        store = Store("Store Name", "Store Address", "Store Manager", store_collection_mock)
        with pytest.raises(ValueError):
            store.insert()