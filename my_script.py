mars_file = open('mars.txt','a')

# print(mars_file.read())

mars_file.write('\nEarth loves Mars, too')

numbers = [1,2,3]
for i in numbers:
    mars_file.write("\n{}".format(i))

# file_items = mars_file.readlines()
# for item in range(len(file_items)):
#     print(file_items[item])

mars_file.close()
