class person:
      def __init__(self,n, o):
          print("hey i am harry")
          self.name = n
          self.occ = o
  
      def info(self):
          print(f"{self.name} is a {self.occ}")
  
a = person("harry", "manager")
b = person("ved", "developer")
# a.name = "Harry"
# a.occ = "Manager"
a.info()
b.info()
    
    




