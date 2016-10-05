from PIL import *
from pytesser import *

class Getnum:


    def __init__(self,img):
        try:
            ig=Image.open(img)
            self.ig=ig
            for i in range(100):
                for j in range(30):
                    pix=ig.getpixel((i,j))
                    if pix[1]<240:
                        ig.putpixel((i,j),(1,1,1))
                    else:ig.putpixel((i,j),(255,255,255,255))
        except (TypeError,IOError),e:
            print 'open image failed'

    def splide_to_dic(self,begin_pix):

        maindickey=1
        maindic={}
        for i in range(begin_pix[1],begin_pix[1]+15,3):
            for j in range(begin_pix[0],begin_pix[0]+9,3):
                sumofpiece=0
                for k in range(i,i+3):
                    for m in range(j,j+3):
                        text=self.ig.getpixel((m,k))

                        if text[1]==1:

                            sumofpiece=sumofpiece+1
                # print j,i
                maindic[maindickey]=sumofpiece
                maindickey=maindickey+1
        self.maindic=maindic
        return maindic


    def show_num(self):
        begin_pix1=(26,9)
        begin_pix2=(39,7)
        begin_pix3=(52,5)
        begin_pix4=(65,6)
        list=[]
        dic1=self.splide_to_dic(begin_pix1)
        list.insert(0,self.add_rule0(dic1))
        dic2=self.splide_to_dic(begin_pix2)
        list.insert(1,self.add_rule0(dic2))
        dic3=self.splide_to_dic(begin_pix3)
        dic4=self.splide_to_dic(begin_pix4)
        list.insert(2,self.add_rule0(dic3))
        list.insert(3,self.add_rule0(dic4))


        return list

    def add_rule0(self,dic):
        if self.add_rule77(dic):
            return '7'
        if self.add_rule66(dic):
            return '6'
        if self.add_rule55(dic):
            return '5'
        if self.add_rule44(dic):
            return '4'
        if self.add_rule33(dic):
            return '3'
        if self.add_rule8(dic):
            return '8'
        if self.add_rule9(dic):
            return '9'
        if self.add_rule1(dic):
            if  self.add_rule4(dic):
                return '1'
            elif self.add_rule7(dic):
                return '7'
            else:
                return '2'
        elif self.add_rule11(dic):
            if self.add_rule6(dic):
                return '3'
            elif self.add_rule4(dic):
                return '1'
            else:
                return '2'
        elif self.add_rule5(dic):
            return '2'



    def add_rule1(self,dic): #no idea
        value1=0

        for i in range(1,15,3):
            value1=dic[i]+value1
        return value1<19

    def add_rule11(self,dic):
        value1=0

        for i in range(1,15,3):
            value1=dic[i]+value1
        return value1>=19 and value1 <=21

    def add_rule2(self,dic):# Maybe 9 ,1,7,5,2,3. Not 6,8,0,4

        a =dic[10]+dic[11]
        if a<=11 and dic[10]<8 &dic[11]<8:
            return  True
        else:
            return False

    def add_rule3(self,dic):#line in end Maybe 9,8,6,5,3,2,0 Not 7,4,1

        a= dic[13]+dic[14]+dic[15]
        if a>= 18:
            return True
        else:
            return False

    def add_rule4(self,dic):# Maybe 1 Not 7,2

        a=dic[12]+dic[15]
        b=dic[6]-2-dic[5]

        if a >= 7 and b<0:
            return True
        else:
            return False

    def add_rule5(self,dic): # Maybe 2,

        a=dic[2]+dic[6]+dic[11]+dic[14]
        b=dic[4]+dic[5]+dic[7]+dic[12]
        c=dic[4]+dic[5]
        Bo=a >31 and (dic[6]-2)>dic[5] and b<=15 and c<=10
        return Bo

    def add_rule6(self,dic):  #Maybe 3 not 9

        a=dic[4]+dic[7]+dic[10]
        b=dic[4]+dic[10]
        c=dic[6]+dic[9]+dic[12]
        Bo=a<=12 and b<=7 and c>22
        return Bo


    def add_rule7(self,dic):  #Maybe 7 not 2,3

        a=dic[13]+dic[14]+dic[15]
        b=dic[12]+dic[15]

        return a <15 and b<=7

    def add_rule8(self,dic):

        a=dic[13]+dic[14]+dic[15]
        b=dic[7]+dic[9]
        c=dic[7]+dic[8]+dic[9]
        d=dic[4]+dic[6]+dic[10]+dic[12]

        Bo=(a>=24 and b>=15 and c>=23 and d>=31)

        return Bo

    def add_rule9(self,dic):

        a=dic[10]+dic[11]
        b=dic[7]+dic[8]+dic[9]
        c=dic[2]+dic[4]+dic[6]+dic[12]+dic[14]

        Bo= (a<=10 and b>=25 and c>=39 and dic[10]<=6)
        return Bo


    def add_rule77(self,dic):

        a=dic[1]+dic[2]+dic[3]+dic[6]
        b=dic[7]+dic[12]+dic[15]
        c=dic[4]+dic[5]+dic[7]
        d=dic[13]+dic[14]+dic[15]

        Bo=(a >=33 and b<=3 and c<=11 and d<=15)
        return  Bo

    def add_rule66(self,dic):

        a=dic[1]
        b=dic[10]+dic[12]
        c=dic[4]-dic[6]-2
        d=dic[7]+dic[9]+dic[13]+dic[15]
        Bo=(a <=3 and b>=16 and c>0 and d >=30)
        return Bo

    def add_rule55(self,dic):

        a=dic[6]+dic[10]
        b=dic[2]+dic[4]+dic[8]+dic[12]+dic[14]
        c=dic[1]+dic[4]+dic[7]
        d=dic[4]-dic[6]-2
        e=dic[12]-dic[10]-2

        Bo=(a<=8 and b>=36 and c>=22 and d>0 and e>0)
        return  Bo

    def add_rule44(self,dic):

        a=dic[5]+dic[11]
        b=dic[10]+dic[11]+dic[12]
        c=dic[1]

        Bo=(a>=16 and b>=23 and c<=3 )
        return  Bo

    def add_rule33(self,dic):

        a=dic[6]+dic[9]+dic[12]
        b=dic[8]+dic[9]
        c=dic[4]+dic[10]
        d=dic[4]+dic[5]+dic[10]+dic[11]
        e=dic[14]+dic[8]+dic[2]

        Bo=(a>=23 and b>=14 and c<=7 and d<=18 and e>=20)
        return  Bo

    def add_rule00(self,dic):

        a=dic[5]+dic[8]+dic[11]

        Bo=(a<=8)
        return  Bo









