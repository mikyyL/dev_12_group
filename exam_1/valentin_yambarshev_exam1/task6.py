#  6. В строке “Иван Иванов” поменяйте местами слова.
#  Может быть предоставлена любая строка с именем и фамилией.
#  Например “Петр Иванов” => “Иванов Петр”

fistSecondName = "Иван Иванов"
listName = fistSecondName.split()
listName[0], listName[1] = listName[1], listName[0]
strName = " ".join(listName)
print(strName)

