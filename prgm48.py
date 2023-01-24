class bank:
    __acc_name=&quot; &quot;
    __acc_no=&quot; &quot;
    __acc_type=&quot; &quot;
    __acc_balancce=0
    def __init__(self,a_name,a_no,a_type,a_balance):
       self.__acc_name=a_name
       self.__acc_no=a_no
       self.__acc_type=a_type
       self.__acc_balance=a_balance
    def deposit(self,a_deposit):
       print(&quot;initial balance is:&quot;,self.__acc_balance)
       print(&quot;deposit is:&quot;,a_deposit)
       self.__acc_balance+=a_deposit
       print(&quot;current balance is:&quot;,self.__acc_balance)
    def withdraw(self):
       print(&quot;current balance is:&quot;,self.__acc_balance)
       self.amount=int(input(&quot;how much amount need to withdraw:&quot;))
       if self.amount&gt;self.__acc_balance:
         print(&quot;you don&#39;t have enough balance to withdraw&quot;)
         print(&quot;current balance is:&quot;,self.__acc_balance)
       else:

         print(self.amount,&quot;is withdrawed&quot;)
         self.__acc_balance-=self.amount
         print(&quot;current balance is:&quot;,self.__acc_balance)
    def acc_info(self):
       print(&quot;\n \n&quot;)
       print(&quot;account holder name:&quot;,self.__acc_name)
       print(&quot;account number:&quot;,self.__acc_no)
       print(&quot;account balance is:&quot;,self.__acc_balance)
       print(&quot;\n \n&quot;)
def main():
       name=input(&quot;enter account holder name:&quot;)
       no=input(&quot;enter account number:&quot;)
       atype=input(&quot;enter account type:&quot;)
       bal=int(input(&quot;enter account initial balance:&quot;))
       holder=bank(name,no,atype,bal)
       while(True):
           opt=int(input(&quot;1. deposit \n 2.withdraw \n 3. accounnt info \n 0. exit \n choose your
option:&quot;))
           if opt==1:
              amount=int(input(&quot;deposit account:&quot;))
              holder.deposit(amount)
           elif opt==2:
              holder.withdraw()
           elif opt==3:
              holder.acc_info()
           elif opt==0:
              break
           else:
              print(&quot;invalid option&quot;)
if __name__==&quot;__main__&quot;:
     while(True):
          main()
