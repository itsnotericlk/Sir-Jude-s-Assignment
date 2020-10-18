#def is_member(val, value_list):
    #for i in range(len(value_list)):
       # if value_list[i] == val:
          #  return True
        #return False

    
#print(is_member(3,[1,2,3])

def is_member(x, a):
    if len(a) == 0:
        return False
    return x == a[0] or is_member(x, a[1:])


if __name__ == "__main__":
    print is_member(1, [1, 2])
    print is_member('a', ['a'])
    print is_member('b', [1, 2, 'a'])
