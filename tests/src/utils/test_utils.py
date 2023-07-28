from ...src.utils import utils
from utils import get_dataset, split_dataset

def test_get_dataset():
  df = get_dataset()
  assert (len(df) > 0)

def test_split_dataset_by_random(df):
  split_results = split_dataset(df, 'random', 5)
  assert len(list(split_results)) == 5

def test_split_dataset_by_catalyst(df):
  split_results = split_dataset(df, 'catalyst', 5)
  assert len(list(split_results)) == 5 