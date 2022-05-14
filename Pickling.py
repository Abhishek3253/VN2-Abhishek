import pickle
lst1 = ["A","B","C","D","E"]
file_obj = open("Myfile","wb")
pickle.dump(lst1,file_obj)
print("File has been stored ")
file_obj.close()
file_obj = open("Myfile","rb")
obj=pickle.load(lst1,file_obj)
print(obj)