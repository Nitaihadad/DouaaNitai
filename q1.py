from avl_template_new import AVLNode
from avl_template_new import AVLTreeList
import pandas as pd

# generate a list of strings to insert of size 2^10 * 1500
def create_strings_to_insert(index):
    for i in range(index):
        str = 'a' + str(i)
        empty_lst.append(str)
    return empty_lst

def run_insertions(AVLTree, list_strings):

    d = {'Arrangement Number i': [i for i in range (1,11)], 'Insertion Experiment': res}
    df = pd.DataFrame(data=d)