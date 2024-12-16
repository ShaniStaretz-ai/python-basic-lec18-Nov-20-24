# python-basic-lec18-Nov-20-24

## subjects learned:

* Comprehension in dictionary:
    * create dictionary:
      ``` 
      dict={x:x**3 for x in range(1,11)}
      ```
    * update dictionary:
      ```
      dict={key:value.capitalize() for key,value in dict.items()}
      ``` 
    * create the new_dic and then print it in 1 line:
      ```
      print(new_dic:={key:value.capitalize() for key,value in dict.items()})
      ```
* scopes in dictionary:
    * since the dictionary and lists are complex structures ,they will change within the functions, unlike primitive
      parameters (int,float,bool,str...), therefore when sending dictionary and list to a function, you send it by
      REFERENCE and NOT by VALUE.
    * if there is a constructor in the function, it will create a new list and will not change the input list, that was
      sent to the function.
      ```
      def function(ls1:list):
      ls1=list()
      ls1.append(100)
      ```
      therefore the solution, return the changed new list and return it to the same sent input list
    * to clean the list in a function:
      ```
      def clear_list(l1:list)->None:
          l1.clear()
      ```
      the list itself will be empty and its pointer will not change
    * same in dictionary:
      ```
      def add(dic1):
        dic1.setdefault("new_key",10)
      add({})# will change to {new_key:10}
      ```
* tuple:  a collection like list, but can't change it *at all*.
  * tuple is faster in performance and less in the memory.
  * always start with tuple and then change if needed.
  * knowing this parameter will never change (best practice) 
  * create tuple:
     ```
     tup:tuple[int,int,int,int]=(1,3,5,4) #declear each type of the values
     tup1:tuple[int]=(1,)#of 1 value
     ```
  * access content of tuple:
    ```
    print(tup[0])#print: 1
    ```
  * to change a tuple content, then have a tuple of complex collection and change it within the tuple.
    ```
    tup2:tuple[list[int],int]=([1,2,3],3)
    tup2[0].clear()
    print(tup2) #prints ([], 3)
    ```
  * comprehension: 
  ```
  print(tuple(x for x in range(10)))
  #print : (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
  ```
  * functions:
    * count()- like in list
    * index(value)- return the index of the value in the tuple
    * min/max/mean/sum
    * any/all
    * sorted(tuple)-tuple(sorted(numbers,key lambda pair))- create a new sorted list then convert to tuple,not changing the origin
    * join tuples:tuple1+tuple2= returns new tuple in the same sort=(...tuple1,...tuple2)
    * multiple t*3= returns new tuple= (...t,...t,...t)
    * 3 in tuple - returns boolean value.
    * convert tuple to list/dictionary tuple()
    * zip(l1/tuple,l2/tuple)- zip from each couple of values, the zip combine then to 1 couple -need to surround it with the final structure:
      ```
      tuple(zip(tuple1,tuple2))
      list(zip(tuple1,tuple2))
      dictionary(zip(tuple1,tuple2))
      ```
      if there is only if the there is a value:
      ```
      l1=[1,2,3,4]
      l2= [1,2,3]
      tuple1=tuple(zip(l1,l2))#((1,1),(2,2),(3,3)) #4 dont have a mate to join in the zip
      ```
  * each item in dict.items() is a tuple.
  
  * reference: https://www.geeksforgeeks.org/python-tuple-function/

## extra subjects:
 * mutable/immutable - can be changed/cannot be changed.

* if the dictionary is a dictionary of functions, it is custom that most of the functions will be with the same signature.
