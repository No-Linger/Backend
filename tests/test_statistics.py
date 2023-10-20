import pytest
from unittest.mock import Mock
from pymongo.collection import Collection
from app.models.statistics import Statistics  # Reemplaza 'your_module' con el nombre de tu módulo

@pytest.fixture
def mock_stats_collection():
    return Mock(spec=Collection)

@pytest.fixture
def stats_instance(mock_stats_collection):
    return Statistics("2023-10-19", "12:30", "90%", "5%", mock_stats_collection)

def test_to_dict(stats_instance: Statistics):
    expected_dict = {
        'date': "2023-10-19",
        'time': "12:30",
        'model_percentage': "90%",
        'error_percentage': "5%",
    }
    assert stats_instance.to_dic() == expected_dict

def test_insert(stats_instance, mock_stats_collection):
    mock_stats_collection.insert_one.return_value = "Some result"
    result = stats_instance.insert()
    assert result is True
    mock_stats_collection.insert_one.assert_called_with(stats_instance.to_dic())

def test_insert_with_exception(stats_instance, mock_stats_collection):
    mock_stats_collection.insert_one.side_effect = Exception("An error occurred")
    result = stats_instance.insert()
    assert result is False

def test_insert_many(stats_instance, mock_stats_collection):
    stats_list = [
        {
            'date': "2023-10-20",
            'time': "13:00",
            'model_percentage': "85%",
            'error_percentage': "7%",
        },
        {
            'date': "2023-10-21",
            'time': "14:00",
            'model_percentage': "92%",
            'error_percentage': "4%",
        }
    ]

    mock_stats_collection.insert_many.return_value = "Some result"
    stats_instance.insert_many(stats_list)
    mock_stats_collection.insert_many.assert_called_with(stats_list)

def test_insert_many_with_exception(stats_instance, mock_stats_collection):
    stats_list = [
        {
            'date': "2023-10-20",
            'time': "13:00",
            'model_percentage': "85%",
            'error_percentage': "7%",
        },
        {
            'date': "2023-10-21",
            'time': "14:00",
            'model_percentage': "92%",
            'error_percentage': "4%",
        }
    ]

    mock_stats_collection.insert_many.side_effect = Exception("An error occurred")
    with pytest.raises(ValueError):
        stats_instance.insert_many(stats_list)