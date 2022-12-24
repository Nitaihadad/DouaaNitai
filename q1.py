import random2

from avl_template_new import AVLNode
from avl_template_new import AVLTreeList
import pandas as pd
import random2 as rd

# generate a list of strings to insert of size 2^10 * 1500
def create_strings_to_insert(index):
    empty_lst=[]
    for i in range(index):
        str =  str(i)
        empty_lst.append(str)
    return empty_lst

def run_insertions():
    res=[]
    for i in range(1,11):
        T = AVLTreeList()
        list_string = create_strings_to_insert(i)
        total = 0
        for j in range(len(list_string)):
            num = rd.randrange(len(list_string))
            output = AVLTreeList.insert(j, list_string[num])
            list_string.remove(list_string[num])
            total += output
        res.append(total)
    return res
def create_AVLTress_for_deletions():
    lst=[]
    for i in range (1,11):
        T=AVLTreeList()
        list_string = create_strings_to_insert(i)
        for j in range(len(list_string)):
            num = rd.randrange(len(list_string))
            AVLTreeList.insert(j, list_string[num])
            list_string.remove(list_string[num])
        lst.append(T)
    return lst

def run_deletions():
    res=[]
    AVLTrees= create_AVLTress_for_deletions()
    for i in range(1,11):
        T = AVLTrees[i]
        options=[i for i in range(T.size())]
        total=0
        for j in range(T.size()):
            num= rd.randrange(T.size())
            output=AVLTreeList.delete(num)
            total+=output
        res.append(total)
    return res
def insertions_by_n(n):
    string_lst = []
    for i in range(n):
        str = str(i)
        string_lst.append(str)
    T = AVLTreeList()
    total = 0
    for i in range(len(string_lst)):
        num = rd.randrange(len(string_lst))
        output = AVLTreeList.insert(i, string_lst[num])
        string_lst.remove(string_lst[num])
        total += output
    return output
def deletions_by_n(n):
    num_lst= [i for i in range (n)]
    string_lst = []
    T = AVLTreeList()
    total = 0
    for i in range(n):
        str = str(i)
        string_lst.append(str)
    for i in range(len(string_lst)):
        num = rd.randrange(len(string_lst))
        output = AVLTreeList.insert(i, string_lst[num])
        string_lst.remove(string_lst[num])
    for i in range(T.size()):
        num = rd.randrange(num_lst)
        res = T.delete(num)
        num_lst.remove(num)
        output += res
    return output

def run_insertions_deletions_alternately():
    lst_res=[]
    for i in range(1,11):
        total=0
        n= 1500* (2**i)
        # insert n/2 items
        total += insertions_by_n(n/2)
        total+= deletions_by_n(n/4)
        total+= insertions_by_n(n/2)
        total += deletions_by_n(n/4)
        total += insertions_by_n(n/2)
        lst_res.append(total)
    return lst_res


def create_excel_file(insertion_lst, deletion_lst, alternate_insertion_deletion_lst):
    d1 = {'Arrangement Number i': [i for i in range (1,11)], 'Insertion Experiment': insertion_lst}
    d2={'Arrangement Number i': [i for i in range (1,11)], 'Deletion Experiment': deletion_lst}
    d3={'Insertion/Deletion Experiment':alternate_insertion_deletion_lst  }
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    df3 = pd.DataFrame(data=d3)
    with pd.ExcelWriter('Results.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Insertion Experiment')
        df2.to_excel(writer, sheet_name='Deletion Experiment')
        df2.to_excel(writer, sheet_name='Insertion/Deletion Experiment')


def main():
    create_excel_file(insertion_lst=run_insertions(), deletion_lst=run_deletions(),
                      alternate_insertion_deletion_lst=run_insertions_deletions_alternately())
    pass


if __name__ == '__main__':
    main()