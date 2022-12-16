from avl_template_new import AVLTreeList

"""
IN ORDER TO USE THE INTERACTIVE TREE TOU NEED TO HAVE A PRINT METHOD IN YOUR AVLTreeList CLASS AND NAME IT
printt. ALTERNATIVELY, YOU CAN CHANGE THE CODE OF THIS FILE TO FIT WITH THE NAME OF YOUR PRINT METHOD.
IF YOU DON'T HAVE A PRINT METHOD IN YOUR AVLTreeList CLASS, COPY THE FOLLOWING CODE TO YOUR CLASS:

### PRINT TREE FUNCTIONS ###

def printt(self):
    out = ""
    for row in self.printree(self.root):  # need printree.py file
        out = out + row + "\n"
    print(out)

def printree(self, t, bykey=True):
    # for row in trepr(t, bykey):
    #        print(row)
    return self.trepr(t, False)

def trepr(self, t, bykey=False):
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.getValue())

    return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

def conc(self, left, root, right):

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid+1)*" " + root + (rwid+1)*" "]

    ls = self.leftspace(left[0])
    rs = self.rightspace(right[0])
    result.append(ls*" " + (lwid-ls)*"_" + "/" + rootwid *
                    " " + "\\" + rs*"_" + (rwid-rs)*" ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid*" "

        row += (rootwid+2)*" "

        if i < len(right):
            row += right[i]
        else:
            row += rwid*" "

        result.append(row)

    return result

def leftspace(self, row):
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row)-1
    while row[i] == " ":
        i -= 1
    return i+1

def rightspace(self, row):
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i

"""


def interactive_tree():
    T = AVLTreeList()
    while True:
        choice = input("choose an operation you want to do with your AVLTreeList from the following: \n \
            empty(), retrieve(i), insert(i,val) delete(i),\n\
            first(), last(), listToArray(), length(),\n\
            split(i), concat, search(val) .\n\
            if you want to exit enter 'exit'\n\
            enter your choice here:  ")
        if choice == "exit":
            print("bye bye")
            break
        elif choice == "empty()":
            if T.empty():
                print("your AVLTreeList is empty")
            else:
                print("your AVLTreeList is not empty")
        elif choice[:8] == "retrieve":
            print("the value in index " +
                  str(choice[9:-1]) + " is: " + str(T.retrieve(int(choice[9:-1]))))
        elif choice[:6] == "insert":
            lst = choice.split(",")
            index = int(lst[0][7:])
            val = lst[1][:-1]
            T.insert(index, val)
            print("if '" + str(index) + "' was a valid index, the " +
                  str(index) + "'th item in the list is now '" + val+"'")

        elif choice[:6] == "delete":
            index = int(choice[7:-1])
            T.delete(index)
            print("if '" + str(index) + "' was a valid index, the " +
                  str(index) + "'th item in the list had been deleted")
        elif choice == "first()":
            print("the first item in the list is: " + str(T.first()))
        elif choice == "last()":
            print("the last item in the list is: " + str(T.last()))
        elif choice == "listToArray()":
            print("your list as an array: ")
            print(T.listToArray())
        elif choice == "length()":
            print("the length of your list is: " + str(T.length()))
        elif choice[:5] == "split":
            index = int(choice[6:-1])
            res = T.split(index)
            T1 = res[0]
            val = res[1]
            T2 = res[2]
            ans = input(
                "if you want to print the tree representing the first list enter 'yes'\n\
                    enter your choice here:  ")
            if ans == "yes":
                T1.printt()
                print(T1.listToArray())
            ans = input("if you want to print the value of the " +
                        str(index) + "'th index enter 'yes'\n\
                            enter your choice here:  ")
            if ans == "yes":
                print(val)
            ans = input(
                "if you want to print the tree representing the second list enter 'yes'\n\
                enter your choice here:  ")
            if ans == "yes":
                T2.printt()
                print(T2.listToArray())
            while True:
                ans = input(
                    "enter '1' if you want to keep working with the first list \n\
                    enter '2' if you want to keep working with the second list \n\
                    enter 'exit' if you want to exit\n\
                    enter your choice here:  ")
                if ans == "1":
                    T = T1
                    break
                elif ans == "2":
                    T = T2
                    break
                elif ans == "exit":
                    print("bye bye")
                    return
                else:
                    print("please enter a valid input")
        elif choice == "concat":
            lst = input(
                "enter a sequence of values you want to create a new AVLTreeList that will be concatenated to \n\
                your tree in the following format: \n\
                val1,val2,val3,....,valn\n\
                enter your sequence here: \n").split(",")
            L = AVLTreeList()
            for val in lst:
                L.insert(L.length(), val)
            print("the avlTreeList that had been concatenated to your list is: ")
            L.printt()
            print(L.listToArray())
            T.concat(L)
        elif choice[:6] == "search":
            val = choice[7:-1]
            index = T.search(val)
            if index == -1:
                print(val + " is not in your list")
            else:
                print(val + " is in the " + str(index) +
                      "'th index in your list")
        else:
            print("please enter a valid input")
        ans = input(
            "enter 'yes' if you want to print your AVLTreeList\n\
            enter your choice here:  ")
        if ans == "yes":
            T.printt()
            print(T.listToArray())


interactive_tree()
