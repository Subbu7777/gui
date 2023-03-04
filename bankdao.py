import prjtdatabase as b #importing the database connection file
import winsound         #importing the winsound module
import pandas as pd     #importing pandas

FRE_QUENCY = 1000
DUA_RATION = 2000
class tables:  #class for tables creation
    def __init__(self):
        self.conn=b.db()  #assing connection 
        self.trid=0      #taking variable for transfering transaction id
        self.transfered=0  #variable for transfer amount
        self.oldbal=0  #connection creating for database
        self.q=self.conn
    def databasecreation(self):
        with self.conn.cursor() as self.w:
            self.w.execute('create  database if not exists sub');
            self.w.execute('use sub');
            self.w.execute('create table  if not exists detail(id int,  name varchar(20) not null,accbalance  Decimal(10,3),deposit Decimal(10,3) null,withdraw Decimal(10,3) null,transfer_amnt Decimal(10,3) null,transfer_to_id int null)'); 
            self.w.execute('create table if not exists acc(Id int,Name varchar(20),Phone int(10),Place varchar(10))');
            print('i am running')
            self.conn.commit()
    def calling(self,id): #function for assigning the values for variables
        with self.conn.cursor() as self.w:
            print('enterd')
            self.I_D=id
            self.name = ''
            self.nme = ''
            self.w.execute(f"select * from acc where id={self.I_D}")
            self.name = self.w.fetchone()[1]    #taking name from database by id
            print(self.name)
            try:
                self.w.execute(f"SELECT * FROM detail where id={self.I_D}")
                results = self.w.fetchall()
                for row in results:      #taking the account balance by id
                    self.accbal= row[2]
                self.accbal=float(self.accbal)
            except :
                self.accbal = 0    #if not avail the acc bal is 0
                self.accbal=float(self.accbal)
            finally:
                self.withdrawn = 0
                self.oldbal=0
                self.amount = 0
            self.conn.commit()  #commiting
    def register(self,I_D,name,phone,place):  #method for registration purpose
        with self.conn.cursor() as self.w:
            self.I_D=I_D
            self.name=name
            self.phone=phone
            self.place=place
            W_E= "insert into acc(ID,Name,Phone,Place) values(%s,%s,%s,%s)"
            em=[(I_D,name,phone,place)]
            self.w.executemany(W_E,em)
            self.conn.commit()
            winsound.Beep(FRE_QUENCY, DUA_RATION)
    def deposit(self,amount):  #method for depositing the money
            """ it is deposited"""
            with self.conn.cursor() as self.w:
                self.amount = float(amount)
                self.accbal = self.accbal+self.amount
                self.info() #commit to changes to database
                self.conn.commit()
            winsound.Beep(FRE_QUENCY, DUA_RATION)
            print('your amount has successfully deposited')

    def w_d(self,withdrawamount):   #code for withdraw the amount
                """it is with"""
                self.withdrawn = float(withdrawamount)
                if self.accbal < self.withdrawn:
                    print('not enough bln')
                else:
                    self.accbal = self.accbal-self.withdrawn  
                    print('your amount is withdrawn',self.withdrawn)
                    self.info()
                    self.withdrawn = 0
                winsound.Beep(FRE_QUENCY, DUA_RATION)           
    def trans(self,trid,transfered):  #method for transfering the amount 
        with self.conn.cursor() as self.w: #establising the connection
            self.trid =int(trid)
            self.transfered =float(transfered)
            self.calling(self.I_D)    #taking the default values
            if self.accbal < self.transfered: 
                print('not enough bln') #for balance is less
            else:
                self.accbal = self.accbal-self.transfered
                try:
                    with self.conn.cursor() as self.w:
                        self.w.execute(f"SELECT * FROM acc where Id={self.trid}") #taking name of transfered person
                        results = self.w.fetchall()
                        for rows in results:
                            self.nme = rows[1]
                        self.w.execute(f"SELECT * FROM detail where id={self.trid}")
                        results =self.w.fetchall()
                        for rows in results:
                            self.oldbal = rows[2]  #taking balance for transfered person for updating balance
                            self.oldbal=float(self.oldbal)
                        accbala = self.oldbal+self.transfered
                        w_e = 'insert into detail(id,name,accbalance) values(%s,%s,%s)'
                        k_e = [(self.trid, self.nme, accbala)]
                        self.w.executemany(w_e, k_e)
                        self.conn.commit()
                        print('Amount has transfered from your account')
                        winsound.Beep(FRE_QUENCY, DUA_RATION)
                except ImportError:  #if user not found in db then take not old balance
                        accbala = self.transfered
                        w_e = 'insert into detail(id,name,accbalance) values(%s,%s,%s)'
                        k_e = [(self.trid, self.nme, accbala)]
                        self.w.executemany(w_e, k_e)
                        self.conn.commit()
                        print('Amount has transfered from your account')
                        winsound.Beep(FRE_QUENCY, DUA_RATION)
            self.info()

    def info(self):  #updating information from user input into db every  time using this method
        with self.conn.cursor() as self.w:
            listt = [(self.I_D, self.name, self.accbal, self.amount,
            self.withdrawn, self.transfered, self.trid)]
            e_e = 'INSERT INTO DETAIL\
                (id,name,accbalance,deposit,withdraw,\
                transfer_amnt,transfer_to_id)\
                VALUES(%s,%s,%s,%s,%s,%s,%s)'
            self.w.executemany(e_e, listt)
            self.conn.commit()
                #self.amount = 0
                #self.withdrawn = 0
                #self.transfered = 0
                #self.trid = 0
    def checktrans(self):   #method for checking the transcation
        o_d = pd.read_sql_query('select * from detail', self.q)
        o_d = pd.DataFrame(o_d)
        i = [self.I_D]
        fi_l = o_d['id'].isin(i)
        m_r = o_d.loc[fi_l]
        print(m_r)
        winsound.Beep(FRE_QUENCY, DUA_RATION)


    def chbln(self): #method for checking the balance
        """ chck balnc"""
        print('your account balance : ', self.accbal)
        winsound.Beep(FRE_QUENCY, DUA_RATION)
