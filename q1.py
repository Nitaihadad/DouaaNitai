from avl_template_new import AVLTreeList
import pandas as pd
import random as rd

def run_insertions():
    res = []
    trees = []
    for i in range(1, 11):

        T = AVLTreeList()  # create a tree object
        total = 0
        curr = 0
        for j in reversed(range(1, 1500 * (2 ** i))):
            num = rd.randrange(0, j)
            output = T.insert(curr, num)
            total += output
            curr += 1
        res.append(total)
        trees.append(T)
    return [res, trees]


def run_deletions(tree_lst):
    res = []
    for i in range(len(tree_lst)):
        total = 0
        T = tree_lst[i]
        maximum = T.length()
        for j in reversed(range(1, maximum)):
            num = rd.randint(1, j)
            output = T.delete(num)
            total += output
        res.append(total)
    return res


def insert_by_n(tree, n):
    total = 0
    curr = 0
    for i in reversed(range(0, n)):
        num = rd.randint(1, int(n))
        output = tree.insert(curr, num)
        total += output
        curr += 1
    return [total, tree]


def delete_by_n(tree, n):
    total = 0
    for i in reversed(range(0, n)):
        num = rd.randint(1, n)
        output = tree.delete(num)
        total += output

    return [total, tree]


def insert_delete(n):
    # insert n//2
    insert1 = insert_by_n(AVLTreeList(), int(n / 2))  # return list with curr, total, string list
    delete1 = delete_by_n(insert1[1], int(n / 4))  # return list with total and curr
    insert2 = insert_by_n(delete1[1], int(n / 2))
    delete2 = delete_by_n(insert2[1], int(n / 4))
    insert3 = insert_by_n(delete2[1], int(n / 2))
    total = insert1[0] + delete1[0] + insert2[0] + delete2[0] + insert3[0]
    return total


def run_insertions_deletions_alternately():
    lst_res = []
    for i in range(1, 11):
        n = 1500 * (2 ** i)
        total = insert_delete(n)
        lst_res.append(total)
    return lst_res


def create_excel_file(insertion_lst, deletion_lst, alternate_insertion_deletion_lst):
    d1 = {'Arrangement Number i': [i for i in range(1, 11)], 'Insertion Experiment': insertion_lst}
    d2 = {'Arrangement Number i': [i for i in range(1, 11)], 'Deletion Experiment': deletion_lst}
    d3 = {'Arrangement Number i': [i for i in range(1, 11)],
          'Insertion/Deletion Experiment': alternate_insertion_deletion_lst}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    df3 = pd.DataFrame(data=d3)
    with pd.ExcelWriter('Q1 Results.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Insertion Experiment')
        df2.to_excel(writer, sheet_name='Deletion Experiment')
        df3.to_excel(writer, sheet_name='Insertion_Deletion Experiment')


def main():
    insertion_lst = run_insertions()

    deletion_lst = run_deletions(insertion_lst[1])

    alternate_insertion_deletion_lst = run_insertions_deletions_alternately()

    create_excel_file(insertion_lst, deletion_lst, alternate_insertion_deletion_lst)
    pass


if __name__ == '__main__':
    main()
