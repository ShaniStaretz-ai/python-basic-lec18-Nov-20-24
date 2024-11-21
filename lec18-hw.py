# ex1
# a
tup1: tuple[int] = (99,)
# b
tup2: tuple[int, int, int] = (99, 88, 77)


# c
def tuple_length(tuple1: tuple[int]) -> int:
    return len(tuple1)


# d
def join_2_tuples(tuple1: tuple[int], tuple2: tuple[int]) -> tuple[int, int]:
    return tuple1 + tuple2


# e
def join_shared_tuples(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple[int, ...]:
    result: tuple = tuple()
    for t in tuple1:
        if t in tuple2:
            result += (t,)
    for t in tuple2:
        if t in tuple1 and not t in result:
            result += (t,)
    return result


# f
def join_unique_tuples(tuple1: tuple[int, ...], tuple2: tuple[int, ...]) -> tuple[int, ...]:
    shared_t: tuple[int, ...] = join_shared_tuples(tuple1, tuple2)
    result: tuple = tuple()
    for t in tuple1:
        if not t in shared_t:
            result += (t,)
    for t in tuple2:
        if not t in shared_t:
            result += (t,)
    return result


print(
    f"the shared items of the tuples:{(6, 5, 4, 3)} and {(4, 3, 2, 1)} are: {join_shared_tuples((6, 5, 4, 3), (4, 3, 2, 1))}")
print(
    f"the unique items of the tuples: {(6, 5, 4, 3)} and {(4, 3, 2, 1,)} are: {join_unique_tuples((6, 5, 4, 3,), (4, 3, 2, 1,))}")


# g
def get_tuple_value_by_index(tuple1: tuple[int, ...], index: int) -> int | None:
    if not 0 < index < len(tuple1):
        return None
    return tuple1[index]


print(f"in index {2} the value in tuple {(1, 2, 3)} is :{get_tuple_value_by_index((1, 2, 3), 2)}")
print(f"in index {5} the value in tuple {(1, 2, 3)} is :{get_tuple_value_by_index((1, 2, 3), 5)}")


# h
def reverse_tuple(tuple1: tuple[int, ...]) -> tuple[int, ...]:
    return tuple1[::-1]


print(f"reversed tuple of {(1, 2, 3)} is: {reverse_tuple((1, 2, 3))}")


# i
def multiple_tuple(t: tuple[int, ...], times: int) -> tuple[int, ...]:
    return t * times


print(f"the multiple of tuple {(1, 2)},  {2} times is:", multiple_tuple((1, 2), 2))


# j
def remove_tuple_value(t: tuple[int, ...], value):
    return tuple(x for x in t if x != value)


print(f"tuple {(1, 2, 3, 1)} without the value {1} is:{remove_tuple_value((1, 2, 3, 1), 1)}")


# k
def remove_duplicates(t1: tuple[int, ...]) -> tuple[int, ...]:
    result = tuple()
    for t in t1:
        if not t in result:
            result += (t,)
    return result


print(
    f"the tuple {(40, 30, 10, 50, 2, 3, 5, 5, 8, 10)} without duplicates:{remove_duplicates((40, 30, 10, 50, 2, 3, 5, 5, 8, 10))}")


# l
def tuple_indexes_of_value(t1: tuple[int, ...], value: int) -> list[int]:
    return [i for i in range(len(t1)) if t1[i] == value]


print(
    f"the indexes of the value {5} in tuple {(40, 30, 10, 5, 2, 3, 5, 5, 8, 10)} are:{tuple_indexes_of_value((40, 30, 10, 5, 2, 3, 5, 5, 8, 10), 5)}")

# m
names: list[str] = []
grades: list[int] = []
while True:
    name = input("enter name:")
    if name == 'done':
        break;
    names.append(name)

while True:
    grade = int(input("enter grade:"))
    if grade == -999:
        break;
    grades.append(grade)

print(tuple(zip(names, grades)))

# 2:
# the difference between tuple and list is that tuple's size and values cannot be changed.
# tuple works faster in performance

# the code doesn't have errors because you can change a complex data(the dictionary) within the tuple and not the tuple itself
