import pytest
from tree import Tree

@pytest.fixture
def sample_tree():
    tree = Tree()
    for value in [10, 5, 15, 3, 7]:
        tree.add(value)
    return tree

def test_find_existing_node(sample_tree):
    node = sample_tree.find(7)
    assert node is not None
    assert node.data == 7


#pentru a da commit testare
#incercare 2 de testare
def test_find_non_existing_node(sample_tree):
    node = sample_tree.find(20)
    assert node is None
