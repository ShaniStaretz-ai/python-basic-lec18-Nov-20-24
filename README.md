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

## extra subjects:

* if the dictionary is a dictionary of functions, it is custom that most of the functions will be with the same
  signature.
