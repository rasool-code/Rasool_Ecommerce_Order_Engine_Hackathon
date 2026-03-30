import mysql.connector as db
con=db.connect(user='root',password='root',host='Localhost',database='vegetablecart')
cur=con.cursor()
class VegetableSection:
    def ownerdata(self):
        cur.execute('select * from owners')
        data=cur.fetchall()
        columns=[col[0] for col in cur.description]
        print(' | '.join(columns))
        print('-'*40)

        for rows in data:
            print(' | '.join(str(i) for i in rows))
        return ('available vegetables')

    def userdata(self):
        cur.execute('select * from users')
        data=cur.fetchall()   
        coloumns=[col[0] for col in cur.description]
        print(' | '.join(coloumns))
        print('-'*40)
        for rows in data:
            print(' | '.join(str(i) for i in rows))
        return ('selected items')

    def customerdetails(self):
        cur.execute('select * from userdetails')
        data=cur.fetchall()
        colums=[col[0] for col in cur.description]
        print(' | '.join(colums))
        print('-'*50)
        for row in data:
            print(' | '.join(str(i) for i in row))
        con.commit()
    def usersqty(self):
        quants=float(input('enter how much quantity you want'))
        cur.execute('select quantity,price,cost from owners where vegetables=%s',[vegetables])
        row=cur.fetchone()
        qty,price,cost=row
        if quants<qty:
            pris=float(price)*quants
            diff=price-cost
            profit=float(diff)*quants
            cur.execute('''insert into users values (%s,%s,%s,%s)''',[vegetables,quants,pris,profit])
            qty=float(qty)-quants
            cur.execute('update owners set quantity=%s where vegetables=%s',[qty,vegetables])
            con.commit()
        else:
            print('you are selected item quantity is not available')               
                    
    def profititems(self):
        cur.execute('select vegs,profit from users')
        data=cur.fetchall()
        colums=[col[0] for col in cur.description]
        print(' | '.join(colums))
        print('-'*40)
        for row in data:
            print(' | '.join(str(i) for i in row))
        cur.execute('select profit from users')
        total=cur.fetchall()
        totalprofit=0
        for i in total:
            for j in i:
                totalprofit=totalprofit+j
        print('Total revenue itemized profit',totalprofit)
    def quantityupdate(self):
        cur.execute('select quants from users where vegs=%s',[vegetables])
        quants=cur.fetchone()[0]
        cur.execute('select quantity from owners where vegetables=%s',[vegetables])
        quantity=cur.fetchone()[0]
        quantity=quants+quantity
        cur.execute('update owners set quantity=%s where vegetables=%s',[quantity,vegetables])
        con.commit()
    class Owner:
        def __init__(self,vegetables=None,cost=None,quantity=None,price=None):
            self.vegetables=vegetables
            self.cost=cost
            self.quantity=quantity
            self.price=price
            
        @staticmethod
        def cnt(vegetables):
            cur.execute('select count(*) from owners where vegetables=%s',[vegetables])
            return cur.fetchone()[0]
        
        def addvegs(self,vegetables,cost,quantity,price):
            if self.cnt(vegetables)==0:
                cur.execute('''insert into owners values(%s,%s,%s,%s)''',[vegetables,cost,quantity,price])
                con.commit()
                print(f'your vegetable is addded')
            else:
                print(f'you are selected item is already available')
        def deletevegs(self,vegetables):
            if self.cnt(vegetables)>0:
                cur.execute('''delete from owners where vegetables=%s ''',[vegetables])
                con.commit()
                print(f'you are selected item is deleted')
            else:
                print(f'you are selected item is not available')
        def updatevegs(self,vegetables):
            if self.cnt(vegetables)>0:
                cur.execute('''update owners set cost=%s,quantity=%s,price=%s where vegetables=%s ''',[cost,quantity,price,vegetables])
                con.commit()
                print(f'you are selected item is updated')
            else:
                print(f'you are selected item is not available')
        def showvegs(self):
            cur.execute('select * from owners')
            data=cur.fetchall()
            columns=[col[0] for col in cur.description]
            print(' | '.join(columns))
            print('-'*40)

            for rows in data:
                print(' | '.join(str(i) for i in rows))
                
    class Section(Owner):
        def __init__(self,vegetables=None,quantity=None,price=None,profit=None):
            super().__init__(vegetables,quantity,price)
            self.profit=profit
        def count(self,vegetables):
            cur.execute('select count(*) from users where vegs=%s',[vegetables])
            return cur.fetchone()[0]
        def addvegs(self,vegetables):
            
            if self.cnt(vegetables)>0 and self.count(vegetables)==0:
                outer.usersqty()
                print(f'your vegetable is addded')
            elif self.count(vegetables)>0:
                outer.quantityupdate()
                cur.execute('delete from users where vegs=%s',[vegetables])
                outer.usersqty()
                print(f'your vegetable is addded')
            else:
                print(f'you are selected item is already available')
        def deletevegs(self,vegetables):
            if self.count(vegetables)>0:
                outer.quantityupdate()
                cur.execute('delete from users where vegs=%s',[vegetables])
                con.commit()
                print('you are entered item is removed')
            else:
                print('you are selected removing item is not available ')
        def updatevegs(self,vegetables):
            if self.count(vegetables)>0:
                outer.quantityupdate()
                cur.execute('delete from users where vegs=%s',[vegetables])
                outer.usersqty()
                print('you are entered Item is modified')
            else:
                print('item is not available')
        def billing(self):
            customername=input('enter customer name')
            while True:
                phnno=input('enter customer mobile number :')
                if phnno.isdigit() and len(phnno)==10 and phnno[0] in '9876':
                    break
                else:
                    print('give correct mobile number')
            cur.execute('insert into userdetails values(%s,%s) ',[customername,phnno])
            con.commit()
            cur.execute('select pris from users')
            total=0
            totalamount=cur.fetchall()
            for i in totalamount:
                total=total+i[0]
            outer.userdata()
            print("you are total bill is ",total)
        def showvegs(self):
            cur.execute('select vegs,quants,pris from users')
            data=cur.fetchall()
            colums=[col[0] for col in cur.description]
            print(' | '.join(colums))
            print('-'*40)
            for row in data:
                print(' | '.join(str(i) for i in row))

            
running=True
while running:
    print('1.owner')
    print('2.user')
    print('3.Exit')
    section=input('please select any option')
    while True:
        if section=='owner' or section =='1' or section==1:
            outer=VegetableSection() 
            vegs=VegetableSection.Owner()
            print("1.add")
            print("2.remove")
            print("3.update")
            print("4.view inventary")
            print("5.View users details")
            print("6.total revenue itemized profit")
            print("7.Report")
            print("8.Exit")
            inventory=input("enter your option")
            if inventory==1 or inventory=='add' or inventory=='1':
                vegetables=input('which vegetable is entered :')
                cost=float(input("enter your vegetable cost :"))
                quantity=float(input("enter your quantity  :"))
                price=float(input("enter your price :"))
                vegs.addvegs(vegetables,cost,quantity,price)
                
            elif inventory==2 or inventory=='remove' or inventory=='2':
                vegetables=input('which vegetable is entered :')
                vegs.deletevegs(vegetables)

            elif inventory==3 or inventory=='update' or inventory=='3':
                vegetables=input('which vegetable is entered :')
                cost=float(input('enter updated cost :'))
                quantity=float(input('enter updated quantity :'))
                price=float(input('enter updated price :'))
                vegs.updatevegs(vegetables,cost,quantity,price)
                
            elif inventory==4 or inventory=='view inventary' or inventory=='4':
                vegs.showvegs()
            elif inventory==5 or inventory=='View users details' or inventory=='5':
                outer.customerdetails()
                outer.userdata()
            elif inventory==6 or inventory=='total revenue itemized profit' or inventory=='6':
                outer.profititems()
            elif inventory==7 or inventory=='Report' or inventory=='7':
                print('Today Report \n Today sold items is :')
                outer.userdata()
                print()
                print('Today profit items is :')
                outer.profititems()
                print()
                print('The balance stock is available is shown below :')
                outer.ownerdata()
                
            elif inventory==8 or inventory=='Exit' or inventory=='8':
                break
            else:
                print("select correct option")
                continue
        elif section=='user' or section=='2' or section==2:
            outer=VegetableSection() 
            print("1.add cart")
            print("2.remove cart")
            print("3.modify cart")
            print("4.view cart")
            print("5.Billing")
            print("6.Exit")
            vegs=VegetableSection.Section()
            cart=input('please select your optionn')
            if cart=='1' or cart=='add' or cart==1:
                vegetables=input('What you want vegetable :')
                vegs.addvegs(vegetables)    
            elif cart=='2' or cart=='remove' or cart==2:
                vegetables=input('What you want vegetable :')
                vegs.deletevegs(vegetables)
            elif cart=='3' or cart=='modify' or cart==3:
                vegetables=input('enter which vegetable is modifying :')
                vegs.updatevegs(vegetables)
            elif cart=='4' or cart=='view cart' or cart==4:
                vegs.showvegs()
            elif cart=='5' or cart=='billing' or cart==5:
                vegs.billing()
            elif cart=='6' or cart=='exit' or cart==6:
                break
                print("exiting...")
            else:
                print('select correct option ')
                continue
        elif section==3 or section=='exit' or section=='3':
            running=False
            break
        else:
            print('please select correct option')
            break
cur.close()
con.close()
