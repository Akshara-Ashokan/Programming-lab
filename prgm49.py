class publisher:
    def __init__(self,publisherId,publisherName):
       self.publisherId=publisherId
       self.publisherName=publisherName
    def show1(self):
       print(&quot;Publisher is {self.publisherName}&quot;)
class book:
    def __init__(self,publisherId,publisherName,title,author):
        publisher.__init__(self,publisherId,publisherName)
        self.title=title
        self.author=author
    def display(self):
        print(&quot;Book title is&quot;,self.title, &quot;and author is&quot;,self.author)
class python(book):
    def __init__(self,publisherId,publisherName,title,author,price,no_of_pages):
       book.__init__(self,publisherId,publisherName,title,author)
       self.price=price
       self.no_of_pages=no_of_pages
    def display(self):
       print(&quot;Book price:&quot;,self.price)
       print(&quot;Book total pages:&quot;,self.no_of_pages)
       print(&quot;Book title is&quot;,self.title, &quot;and author is&quot;,self.author)

def main():
    while True:
         print(&quot;____menu____&quot;)
         print(&quot;1. Create new book \n&quot;)
         print(&quot;2. Display book \n&quot;)
         print(&quot;0. Exit&quot;)
         choice=int(input(&quot;Enter your choice:&quot;))
         if choice==0:
            break
         elif choice==1:
             print(&quot;Enter book details&quot;)
             title=input(&quot;Name:&quot;)
             author=input(&quot;Author:&quot;)
             publisherId=input(&quot;Publisher Id:&quot;)
             publisherName=input(&quot;Publisher name:&quot;)
             price=input(&quot;Price:&quot;)
             no_of_pages=input(&quot;Mo.of pages&quot;)
             python1=python(publisherId,publisherName,title,author,price,no_of_pages)
         elif choice==2:
             python1.display()
main()
