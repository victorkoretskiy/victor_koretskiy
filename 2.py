list1 = input('enter the colours of the first list through the space  ').split()
list2 = input('enter the colours of the second list through the space  ').split()
answer = set(list1) - set(list2)
print(answer)
