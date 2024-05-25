# class Telegramm:
#     def __init__(self):
#         self.telegramm = {}
#     def name_age(self,telegramm_id,name,age):
#         self.telegramm[telegramm_id] = 'name', name
#         self.telegramm[telegramm_id] += 'age', age
#     def pri(self,telegramm_id):
#         return self.telegramm[telegramm_id]
# class Instagramm(Telegramm):
#     def __init__(self):
#         super().__init__()
#     def data_fname(self,telegramm_id,data,fname,name,age):
#         Telegramm.name_age(self,telegramm_id,name,age)
#         self.telegramm[telegramm_id] += "fname",fname,"data",data

# a = Telegramm()
# a.name_age(1, "Tom",24)
# print(a.pri(1))

# b = Instagramm()
# b.data_fname(1,2024,"ted","Greg", 25)
# print(b.pri(1))