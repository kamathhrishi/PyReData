import numpy as np
import matplotlib.pyplot as pl
from random import randint
import os.path

class App:

       def __init__(self,Name):

            self.name=Name
            
class Node:

       def __init__(self):

            self.Data=""
            self.Type=""
            self.Name=""
            self.Entity="Node"
            self.Attributes={}
            self.centerize=False

class Container:

       def __init__(self):

            self.Data=[]
            self.Name=""
            self.Type=""
            self.Entity="Container"
            self.Attributes={}
            self.centerize=False


class Page:


        def __init__(self,app,style=""):

            self.Head=[]
            self.Body=[]
            self.Plots=0
            self.style=style
            self.stylesheets=[]
            self.Scripts=[]
            self.PlotNames=0
            self.Sections=[]
            self.Components=0
            self.App=app

        def Add_StyleSheet(self,Link):

            self.stylesheets.append(Link)
            
        def Default(self,Node,Type,Class,ID,style,centerize,Bookmark,B_Ord=None,Name=''):

            Node.Type=Type
            if(ID!=''):
                   
                 Node.Attributes['id']=ID

            if(Class!=''):
                   
                 Node.Attributes['class']=Class

            if(style!=''):
                   
                 Node.Attributes['style']=style
                 
            if(Name!=''):

                 Node.Name=Name

            if(Bookmark==True):

                 L=Link()
                 L.Name=ID
                 
                 if(B_Ord==None):

                        self.Sections.append(L)

                 else:

                        for i in self.Sections:

                               if(i.Name==Name):

                                      if(i.Children==None):

                                             i.Children=L

                                      else:

                                             pass

            Node.centerize=centerize

            return Node

        def AddTitle(self,centerize=False,Text="",Div="",style="",ID="",Class="",Bookmark=False,B_Name=""):

            N=Node()
            N=self.Default(N,'h1',Class,ID,style,centerize,Bookmark,B_Name)

            if(Text!=""):

                
                N.Data=Tit

            else:

                N.Data=self.App.name

            self.Add_Component(N,Div=Div)

        def AddTOC(self,Data,ID="",Class="",Div="",style="",Item_Style="",centerize=False,B_Name=""):

            C=Container()
            C=self.Default(C,'ul',Class,ID,style,centerize,B_Name)

            for i in range(0,len(Data)):

                   C.Data.append(self.Table_Data('li',Data[i],style=Item_Style))
            
            self.Add_Component(C,Div=Div)

        def AddText(self,Text,Div="",style="",ID="",Class="",centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N.Type="p"
            N=self.Default(N,'p',Class,ID,style,centerize,Bookmark,B_Name)
            N.Data=Text
            self.Add_Component(N,Div=Div)
                              
        def AddDiv(self,Name,Div="",style="",ID="",Class="",centerize=False,Bookmark=False,B_Name=""):

            C=Container()
            C=self.Default(C,'div',Class,ID,style,centerize,Bookmark,B_Name,Name=Name)
            self.Add_Component(C,Div=Div)
 
        def AddImg(self,src,Class="",ID="",Div="",style="",height=400,width=400,centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N=self.Default(N,'img',Class,ID,style,centerize,Bookmark,B_Name)
            N.Attributes['src']=src
            N.Attributes['width']=width
            N.Attributes['height']=height
            self.Add_Component(N,Div=Div)

        def AddBreak(self,Div=''):

            C=Container()
            C=self.Default(C,'br','','','','','','',0)
            self.Add_Component(C,Div=Div)


        def AddButton(self,Text,Class="",Div="",ID="",style="",onClick="",centerize=False):

            N=Node()
            N=self.Default(N,'button',Class,ID,style,centerize,None)
            N.Attributes['onClick']=onClick
            N.Data=Text
            self.Add_Component(N,Div=Div)
            
        def AddLink(self,src,Text,Class="",ID="",Div="",style="",centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N=self.Default(N,'a',Class,ID,style,centerize,Bookmark,B_Name)
            N.Data=Text
            N.Attributes['href']=src
            self.Add_Component(N,Div=Div)

        def Table_Data(self,Type,Data,ID="",Class="",Div="",style="margin:20px;",centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N=self.Default(N,Type,Class,ID,style,centerize,Bookmark,B_Name)
            N.Data=str(Data)
            return N

        def Add_Component(self,Component,Div=""):

            if(Div==""):
                   
                      self.Body.append(Component)

            else:
                      Sucess=False
                      for i in self.Body:

                           if(i.Type=="div" and i.Name==Div):

                                i.Data.append(Component)
                                Sucess=True


                      if(Sucess==False):

                           for i in self.Body:

                                  for j in i.Data:


                                      if(j.Type=="div" and j.Name==Div):

                                            j.Data.append(Component)


        def Create_List(self,Data,ID="",Class="",Div="",style="",Item_Style="",centerize=False,Bookmark=False,B_Name=""):

            C=Container()
            C=self.Default(C,'ul',Class,ID,style,centerize,Bookmark,B_Name)

            for i in range(0,len(Data)):

                   C.Data.append(self.Table_Data('li',Data[i],style=Item_Style))
            
            self.Add_Component(C,Div=Div)

        def List_Item(self,Type,Data,ID="",Class="",Div="",style="",centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N=self.Default(N,'li',Class,ID,style,centerize,Bookmark,B_Name)
            N.Data=str(Data)
            return N

        def Header(self,Type,Text,Div="",style="",ID="",Class="",centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N.Type=Type
            N=self.Default(N,Type,Class,ID,style,centerize,Bookmark,B_Name)
            N.Data=Text
            self.Add_Component(N,Div=Div)


        def Statistics(self,Head,Data,Div="",ID="",style="",Header_Style="",Row_Style="margin:20px;",Col_Style="margin:20px;",Class="",centerize=False,Bookmark=False,B_Name=""):

            Comp=Computation()
            Row=['Count','Mean','Std','25%','50%','75%']
            Values=[]

        def CustomTag(self,Type,Text="",Attribute_Names=[],Attributes=[],Class="",ID="",Div="",style="",centerize=False,Bookmark=False,B_Name=""):

            N=Node()
            N=self.Default(N,Type,Class,ID,style,centerize,Bookmark,B_Name)
            N.Data=Text

            for i in range(0,len(Attribute_Names)):

                    N.Attributes[Attribute_Name[i]]=Attributes[i]
    
            self.Add_Component(N,Div=Div)

        def AddScript(self,src):

            N=Node()
            N=self.Default(N,'script','','','',False,'','')
            N.Attributes['src']=src
            self.Add_Component(N,Div='')

        def AddTable(self,Data,Class="",Div="",ID="",style="",Row_Style="",Col_Style="",Header_Style="",centerize=False,Bookmark=False,B_Name=False):

            C=Container()
            C=self.Default(C,'table',Class,ID,style,centerize,Bookmark,B_Name)

            H=Container()
            H=self.Default(H,'tr',Class,ID,style,centerize,Bookmark,B_Name)

            Vars=[]
            
            for i in list(Data):
                   
                   N=Node()
                   N=self.Default(N,'th',Class,ID,Header_Style,centerize,Bookmark,B_Name)
                   H.Data.append(N)
                   N.Data=i
                   Vars.append(i)         

            C.Data.append(H)

            for i in range(1,len(Data)):

                   H=Container()
                   H=self.Default(H,'tr',Class,ID,Col_Style,centerize,Bookmark,B_Name)

                   for j in Vars:

                          N=Node()
                          N=self.Default(N,'td',Class,ID,Row_Style,centerize,Bookmark,B_Name)
                          N.Data=str(Data[j][i])
                          H.Data.append(N)

                   C.Data.append(H)

            self.Add_Component(C,Div=Div)

class Components:


       def __init__(self,Page):

              self.Page=Page

       def AddTabSet(self,Tabs,Tags=[],Div="",style=""):

              Main_Div=""
              Divs=[]
              M_Div="Div"+str(self.Page.Components)
              self.Page.AddDiv(M_Div,Div=Div,Class=M_Div)

              Tab_Class="Tab"+str(self.Page.Components)

              Button_Class="Button"+str(self.Page.Components)

              Sc=Scripts(self.Page)
              Sc.OpenTab(Button_Class,Tab_Class)
              Sc.GenerateScript()

              St=Stylesheet(self.Page)

              self.Page.Components+=1
              
              for i in range(0,len(Tabs)):
                     
                     self.Page.AddButton(Tabs[i],Class=Button_Class,Div=M_Div,style=style,onClick="OpenTab(event,"+"'"+Tabs[i]+"'"+")",centerize=False)
                     self.Page.AddDiv(Tabs[i],Div=Div,Class=Tabs[i],style=style,centerize=False)
                     St.AddAttribute("display:none;",Class=Tabs[i],ID="")

              St.CreateStyleSheet()

              
class Scripts:

       def __init__(self,page):

              self.Page=page
              self.Source=""

       def OpenTab(self,Button,Tabs):

              self.Source+="function OpenTab(evt,TabName)"
              self.Source+="\n"
              self.Source+="{"
              self.Source+="\n"
              self.Source+="\n"
              self.Source+="var i, tabcontent, tablinks;"
              self.Source+="\n"
              self.Source+="tabcontent = document.getElementsByClassName("
              self.Source+="'"+Tabs+"');"
              self.Source+="\n"
              self.Source+="for (i = 0; i <tabcontent.length; i++)"
              self.Source+="\n"
              self.Source+="{"
              self.Source+="\n"
              self.Source+="tabcontent[i].style.display = 'none';"
              self.Source+="\n"
              self.Source+="}"
              self.Source+="\n"
              self.Source+="tablinks = document.getElementsByClassName('"
              self.Source+=Button+"');"
              self.Source+="\n"
              self.Source+="for (i = 0; i < tablinks.length; i++)"
              self.Source+="\n"
              self.Source+="{"
              self.Source+="\n"
              self.Source+="tablinks[i].className = tablinks[i].className.replace(' active','');"
              self.Source+="\n"
              self.Source+="}"
              self.Source+="\n"
              self.Source+="document.getElementById("
              self.Source+="TabName"+").style.display = 'block';"
              self.Source+="evt.currentTarget.className +='active';"
              self.Source+="\n"
              self.Source+="\n"
              self.Source+="}"
              self.Source+="\n"

       def GenerateScript(self):

              Gen=Generator("",self.Page)
              Link=Gen.GenerateScript(self.Source,"Components")
              self.Page.AddScript(Link)

       
class Computation:


        def Mean(self,Data):

             Sum=0

             for i in range(len(Data)):

                    Sum+=float(Data[i])

             return(Sum/len(Data))

        def Count(self,Data):

             return(len(Data))

        def Std(self,Data):

             return(np.std(Data))

        def percentile(self,Data,alloc):

             return(np.percentile(Data,alloc))

        def Compute_Column(self,Data):

             Row=[]

             for i in range(0,Data[0]):

                    for j in range(0,len(Data)):

                               pass

        def Compute_Counts(self,Data,initial,Final,Step):


              Values=[]
              Counts=[]

              Min=None
              Max=None

              for i in Data:

                     if(i>Max):

                            Max=i

                     if(i<Min):

                            Min=i


              for i in range(initial,Final+Step,Step):

                     Values.append(i)
                     Counts.append(0)

              for i in Data:

                     Counts[self.Search(i,Values)]+=1


              return Values,Counts

        def Normalize(self,Data):

              Mean=self.Mean(Data)
              
              Low=self.Min(Data)
              High=self.Max(Data)
              
              New_Stat=[Low]
              d=len(New_Stat)-1
              while(New_Stat[d]<(High)):

                     k=New_Stat[d]+((self.Mean(Data))/10.0)
                     New_Stat.append(k)
                     d=len(New_Stat)-1

              return New_Stat


        def Search(self,Val,List):

              for i in range(0,len(List)):

                     if(Val>=List[i] and Val<List[i+1]):

                            return i

        def Frequency(self,Data,Range):

               Freq=[]

               for i in range(0,len(Range)):

                      Freq.append(0)

               for i in range(0,len(Data)):

                      k=self.Search(Data[i],Range)
                      Freq[k]+=1

               return Freq
                      
                      
        def Max(self,Data):

               Max=None

               for i in Data:

                      if(i>Max):

                             Max=i

               return Max

        def Min(self,Data):

               Min=Data[0]

               for i in Data:

                      if(i<Min):

                             Min=i

               return Min
       

class Plots:

            def __init__(self,Page):
                   
                  self.Plots=[]
                  self.Page=Page
                  
            def RenderPlot(self,Plot,Div="",height=300,width=300):
                   
                  fileName=(str((self.Page.PlotNames))+'.png')
                  self.Page.PlotNames+=1
                  Plot.savefig(fileName)
                  self.Page.AddImg(fileName,Class="",ID="",Div=Div,style="",centerize=False,Bookmark=False,B_Name="",height=height,width=width)
                  

class Stylesheet:


           def __init__(self,Page):

                  self.Page=Page
                  self.Source=""

           def CreateStyleSheet(self):

                  Gen=Generator("",self.Page)
                  Link=Gen.GenerateStyleSheet(self.Source,"Components")
                  self.Page.Add_StyleSheet(Link)

           def Style_Tab(self):

                  pass

           def AddAttribute(self,Style,Class="",ID=""):

                  self.Source+="\n"

                  if(Class=="" and ID==""):

                         pass

                  elif(ID!=""):

                         self.Source+="#"+ID+"{"+Style+"}"

                  elif(Class!=""):

                         self.Source+="."+Class+"{"+Style+"}"

                  self.Source+="\n"


            
class Generator:


        def __init__(self,app,page):

            if(app!=""): 

                    self.app=app
                    self.Page=page
                    self.Source=""
                    self.Head()
                    self.Body()
            
        def Generate_Body(self,Node):

            if(Node.centerize):

                   self.Source+="<center>"

            self.Source+="<"
            self.Source+=Node.Type
            for j in Node.Attributes:

                     self.Source+=" "
                     self.Source+=j
                     self.Source+="="
                     self.Source+='"'
                     self.Source+=str(Node.Attributes[j])
                     self.Source+='"'

            self.Source+=">"
            
            if(Node.Entity=="Container"):

                     for k in Node.Data:
                            
                            self.Generate_Body(k)


            else:

                     self.Source+=Node.Data

            self.Source+="</"
            self.Source+=Node.Type
            self.Source+=">"
            self.Source+="\n"

            if(Node.centerize):

                   self.Source+="</center>"


        def Head(self):

            self.Source+="<html>"
            
            self.Source+="\n"
            self.Source+="\n"
            self.Source+="\n"
            
            self.Source+="<head>"
            
            self.Source+="\n"
            
            self.Source+="<title>"+self.app.name+"</title>"

            if(self.Page.stylesheets!=[]):

                   for i in self.Page.stylesheets:

                          self.Source+="<link href='"
                          self.Source+=str(i)
                          self.Source+="' rel='stylesheet'"
                          self.Source+=">"
            
            self.Source+="\n"
            
            self.Source+="</head>"
            
            self.Source+="\n"
            self.Source+="\n"

        def Body(self):

            self.Source+="<body "
            
            if(self.Page.style!=""):
                   
                  self.Source+="style="+'"'+self.Page.style+'"'
                  
            self.Source+=">"

            self.Source+="\n"
            self.Source+="\n"
            
            for i in self.Page.Body:

                   self.Generate_Body(i)


            self.Source+="\n"
            self.Source+="\n"
            self.Source+="</body>"
            self.Source+="\n"
            self.Source+="\n"
            self.Source+="\n"
            self.Source+="</html>"


        def SourceCode(self):

            print(self.Source)

        def CreateFile(self,Name):

            fo=open(Name+".html","w")
            fo.write(self.Source)
            fo.close()

        def GenerateStyleSheet(self,Source,Name):

            fo=open(Name+".css","w")
            fo.write(Source)
            fo.close()
            return Name+".css"

        def GenerateScript(self,Source,Name):
       
            fo=open(Name+".js","w")
            fo.write(Source)
            fo.close()
            return Name+".js"

            
            

