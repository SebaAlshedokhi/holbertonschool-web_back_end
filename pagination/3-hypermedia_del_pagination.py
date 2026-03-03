#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return deletion-resilient pagination details starting at a given index."""
        indexed = self.indexed_dataset()

        # Assert index is in a valid range
        assert isinstance(index, int) and 0 <= index < len(indexed)

        data: List[List] = []
        current = index

        while len(data) < page_size:
            # Stop if we've gone past the max possible index
            if current > max(indexed.keys()):
                break
            if current in indexed:
                data.append(indexed[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }
