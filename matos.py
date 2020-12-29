from big_ol_pile_of_manim_imports import *
#from manimlib.imports import *
from objectPosition import *
import os
import pyclbr

class Scenesatu(Scene):
    def  construct(self):
        aksis=Axes()
        grid = NumberPlane(secondary_color=BLACK)  #ScreenGrid(rows=10, columns=20,height=10,width=20)
        grid.add_coordinates()
        self.add(grid)
        self.add(aksis)
        self.wait(4)
        vektori=Arrow(np.array([0,0,0]),np.array([1.5,0,0]),buff=0,tip_length=0.4,width=5,color=RED)
        vektorj=Arrow(np.array([0,0,0]),np.array([0,2,0]),buff=0,tip_length=0.4,width=5,color=GREEN)
        eqi=TexMobject(r"1.5\hat{i}")
        eqi.set_color(YELLOW)
        eqi.move_to((0.1*UP)+(1.6*RIGHT))
        eqi.scale(0.7)
        eqj=TexMobject(r"2\hat{j}")
        eqj.set_color(YELLOW)
        eqj.move_to((2.1*UP)+(0.1*RIGHT))
        eqj.scale(0.7)
        self.play(FadeIn(vektori))
        self.play(FadeIn(eqi))
        self.play(FadeIn(vektorj))
        self.play(FadeIn(eqj))
        
        self.wait(10)
        vektorw=Arrow(np.array([0,0,0]),np.array([1.5,2,0]),buff=0,tip_length=0.4,width=5,color=GREY)
        eqw=TexMobject(r"""\vec{W}=\begin{bmatrix} 1.5\\ 2 \end{bmatrix}= 1.5\hat{i}+2\hat{j}""")
        eqw.set_color(YELLOW)
        eqw.move_to((2.1*UP)+(2.6*RIGHT))
        eqw.scale(0.7)
        self.play (FadeIn(vektorw))
        self.play (FadeIn(eqw))
        self.wait(23)
        
      
class Scenedua(Scene):
    def  construct(self):
        aksis=Axes()
        grid = NumberPlane(secondary_color=BLACK)  #ScreenGrid(rows=10, columns=20,height=10,width=20)
        grid.add_coordinates()
        self.add(grid)
        self.add(aksis)
        vektoru1=Arrow(np.array([0,0,0]),np.array([4,1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        vektoru2=Arrow(np.array([0,0,0]),np.array([-1,3,0]),buff=0,tip_length=0.4,width=5,color=GREEN)
        equ1=TexMobject(r"""\vec{u1}=\begin{bmatrix} 4\\ 1 \end{bmatrix}= 4\hat{i}+1\hat{j}""")
        equ1.set_color(YELLOW)
        equ1.move_to((2*UP)+(4*RIGHT))
        equ1.scale(0.7)
        equ2=TexMobject(r"""\vec{u2}=\begin{bmatrix} -1\\ 3 \end{bmatrix}= -1\hat{i}+3\hat{j}""")
        equ2.set_color(YELLOW)
        equ2.move_to((3*UP)+(-3*RIGHT))
        equ2.scale(0.7)
        self.play(FadeIn(vektoru1))
        self.play(FadeIn(equ1))
        self.play(FadeIn(vektoru2))
        self.play(FadeIn(equ2))
        self.wait(1)
        vektorw=Arrow(np.array([0,0,0]),np.array([1.5,1,0]),buff=0,tip_length=0.4,width=5,color=GREY)
        eqw=TexMobject(r"""\vec{W}""")
        eqw.set_color(YELLOW)
        eqw.move_to((1*UP)+(2*RIGHT))
        self.play (FadeIn(vektorw))
        self.play (FadeIn(eqw))
        self.wait(34)
 
 
 
class Scenetiga(Scene):
    def  construct(self):
        aksis=Axes()
        grid = NumberPlane(secondary_color=BLACK)  #ScreenGrid(rows=10, columns=20,height=10,width=20)
        grid.add_coordinates()
        self.add(grid)
        self.add(aksis)
        vektoru1=Arrow(np.array([0,0,0]),np.array([4,1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        vektoru2=Arrow(np.array([0,0,0]),np.array([-1,3,0]),buff=0,tip_length=0.4,width=5,color=GREEN)
        equ1=TexMobject(r"""\vec{u1}=\begin{bmatrix} 4\\ 1 \end{bmatrix}= 4\hat{i}+1\hat{j}""")
        equ1.set_color(YELLOW)
        equ1.move_to((1.5*UP)+(3.6*RIGHT))
        equ1.scale(0.5)
        equ2=TexMobject(r"""\vec{u2}=\begin{bmatrix} -1\\ 3 \end{bmatrix}= -1\hat{i}+3\hat{j}""")
        equ2.set_color(YELLOW)
        equ2.move_to((2.5*UP)+(-2.5*RIGHT))
        equ2.scale(0.5)
        self.play(FadeIn(vektoru1),FadeIn(vektoru2))
        self.play(FadeIn(equ1),FadeIn(equ2))
        self.wait(1)
        vektorw=Arrow(np.array([0,0,0]),np.array([1.5,1,0]),buff=0,tip_length=0.4,width=5,color=GREY)
        eqw=TexMobject(r"\alpha u1 + \beta u2")
        eqw.set_color(YELLOW)
        eqw.move_to((1.2*UP)+(2*RIGHT))
        eqw.scale(0.5)
        self.play (FadeIn(vektorw))
        self.play (FadeIn(eqw))
        vektorA=Arrow(np.array([0,0,0]),np.array([1.8,0.5,0]),buff=0,tip_length=0.4,width=5,color=PURPLE)
        vektorB=Arrow(np.array([0,0,0]),np.array([-0.1,0.3,0]),buff=0,tip_length=0.4,width=5,color=PURPLE)
        eqA=TexMobject(r"\alpha U1")
        eqA.set_color(YELLOW)
        eqA.move_to((0.3*UP)+(1*RIGHT))
        eqA.scale(0.5)
        eqB=TexMobject(r"\beta U2")
        eqB.set_color(YELLOW)
        eqB.move_to((0.5*UP)+(-0.2*RIGHT))
        eqB.scale(0.5)
        self.play(FadeIn(vektorA),FadeIn(vektorB))
        self.play(FadeIn(eqA),FadeIn(eqB))
        
        
        garisA=Line(np.array([1.8,0.5,0]),np.array([1.5,1,0]),buff=0,tip_length=0.4,width=5,color=YELLOW)
        garisB=Line(np.array([-0.1,0.3,0]),np.array([1.5,1,0]),buff=0,tip_length=0.4,width=5,color=YELLOW)
        self.play(FadeIn(garisA),FadeIn(garisB))
        self.wait(31)
        
   
        
class Sceneempat(Scene):
    def  construct(self): 
        line1=TexMobject(r"\left [ W \right ]_{B} = \begin{bmatrix} 1\\2 \end{bmatrix}")
        line1.shift(UP)
        line2=TextMobject("Vektor Basis Awal",color=RED)
        g1=VGroup(line1,line2)
        self.play(ShowCreation(g1))
        self.play(g1.to_edge,UP+LEFT)  
        panah1=Arrow(np.array([-1,0,0]),np.array([1,0,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah1.next_to(g1,6*RIGHT)
        self.play(FadeIn(panah1))
        line3=TexMobject(r"\left [ W \right ]_{B'} = \begin{bmatrix} \alpha\\ \beta\end{bmatrix}")
        line3.shift(UP)
        line4=TextMobject("Vektor Basis Baru",color=RED)
        g2=VGroup(line3,line4)
        self.play(ShowCreation(g2))
        self.play(g2.to_edge,UP+RIGHT)
        
        line5=TextMobject("W")
        line5.next_to(g1,DOWN)
        panah2=Arrow(np.array([0,1,0]),np.array([0,-1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah2.next_to(line5,2*DOWN)
        line6=TexMobject(r"\left [ W \right ]_{B}")
        line6.next_to(panah2,2*DOWN)
        g3=VGroup(line5,panah2,line6)
      
        panah4=Arrow(np.array([-3,0,0]),np.array([2,0,0]),buff=0,tip_length=0.4,width=10,color=BLUE)
        panah4.next_to(line6,6*RIGHT)
        
        line7=TextMobject("W")
        line7.next_to(g2,DOWN)
        panah3=Arrow(np.array([0,1,0]),np.array([0,-1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah3.next_to(line7,2*DOWN)
        line8=TexMobject(r"\left [ W \right ]_{B'}")
        line8.next_to(panah3,2*DOWN)
        g4=VGroup(line7,panah3,line8)
        
        line9=TextMobject("?")
        line9.shift(1.5*DOWN)
        
        line10=TexMobject(r"A\left [ W \right ]_{B} = \left [ W \right ]_{B'}")
        line10.shift(3*DOWN)
        
        self.play(FadeIn(g3))
        self.play(FadeIn (panah4))
        self.play(FadeIn(g4))
        self.play(FadeIn(line9))
        self.play(FadeIn(line10))
        self.wait(36)
        
class Scenelima(Scene):
    def  construct(self): 
        line1=TexMobject(r"\textup{Misalkan}\,B=\left \{ b_1,b_2 \right \} \text{dan}\,B'=\left \{ b_1',b_2' \right \}\textup{basis untuk}\,V\textup{dan}\,v\,\epsilon\,V \\")
        line1.shift(3*UP)
        line1.scale(0.8)
        
        line2=TexMobject(r"\textup{Misalkan} \left [ b_{1} \right ]_{B'} = \begin{bmatrix}\alpha_{1}\\ \alpha_{2}\end{bmatrix} \textup{dan} \left [ b_{2} \right ]_{B'} = \begin{bmatrix}\beta _{1}\\ \beta _{2}\end{bmatrix}")
        line2.shift(2*UP)
        line2.scale(0.8)
        
        line3=TexMobject(r"\textup{Misalkan} \left [ V \right ]_{B} = \begin{bmatrix}\gamma_{1}\\ \gamma_{2}\end{bmatrix}")
        line3.shift(UP)
        line3.scale(0.8)
        
        line4=TexMobject(r"v=\gamma _{1}b_{1}+\gamma _{2}b_{2}")
        #line4.shift(DOWN)
        line4.scale(0.8)
        
        line5=TexMobject(r"\textup{Substitusikan menjadi}:v=\gamma_1\left ( \alpha_1b_1'+\alpha_2b_2' \right )+\gamma_2\left ( \beta_1b_1'+\beta_2b_2' \right )")
        line5.next_to(line4,1*DOWN)
        line5.scale(0.8)
        
        
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))
        self.wait(50)
        
        
class Sceneenam(Scene):
    def  construct(self): 
        line1=TexMobject(r"v=\gamma_1\left ( \alpha_1b_1'+\alpha_2b_2' \right )+\gamma_2\left ( \beta_1b_1'+\beta_2b_2' \right )")
        line1.shift(3*UP)
        line1.scale(0.8)
        
        line2=TexMobject(r"v=(\gamma _{1}\alpha _{1} + \gamma _{2}\beta_{1})b'_{1}+(\gamma _{1}\alpha _{2} + \gamma _{2}\beta _{2})b'_{2}")
        line2.shift(2*UP)
        line2.scale(0.8)
        
        line3=TexMobject(r"\left [ V \right ]_{B'}= \begin{bmatrix}\gamma _{1}\alpha _{1} + \gamma _{2}\beta_{1}\\ \gamma _{1}\alpha _{2} + \gamma _{2}\beta_{2}\end{bmatrix}= \begin{bmatrix}\alpha _{1}& \beta_{1}\\ \alpha _{2}& \beta_{2}\end{bmatrix} \begin{bmatrix}\gamma _{1}\\ \gamma _{2}\end{bmatrix}")
        line3.shift(1*UP)
        line3.scale(0.8)
        
        line4=TexMobject(r"\left [ V \right ]_{B'}=\begin{bmatrix}\left [ b_{1} \right ]_{B'}\left [ b_{2} \right ]_{B'}\end{bmatrix}\cdot \left [ V \right ]_{B}")
        line4.shift(0.5*DOWN)
        line4.scale(0.8)
        
        line5=TexMobject(r"\left [ V \right ]_{B'}= P _{B\rightarrow B'}\cdot \left [ V \right ]_{B}")
        line5.next_to(line4,1*DOWN)
        line5.scale(0.8)
        
        framebox1 = SurroundingRectangle(line5[8], buff = .45)
        panah=Arrow(np.array([0,0,0]),np.array([0,-1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah.next_to(framebox1,1*DOWN)
        
        line6=TextMobject("Matriks Transisi dari B ke B'")
        line6.next_to(panah,1*DOWN)
        line6.scale(0.8)
        
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Write(line4))
        self.play(Write(line5))
        self.play(ShowCreation(framebox1),)
        self.play(FadeIn (panah))
        self.play(Write(line6))
        self.wait(50)
        
        
class Scenetujuh(Scene):
    def  construct(self): 
        line1=TexMobject(r"\left [ W \right ]_{B} = \begin{bmatrix} 1\\2 \end{bmatrix}")
        line1.shift(UP)
        line2=TextMobject("Vektor Basis Awal",color=RED)
        g1=VGroup(line1,line2)
        self.play(ShowCreation(g1))
        self.play(g1.to_edge,UP+LEFT)  
        panah1=Arrow(np.array([-1,0,0]),np.array([1,0,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah1.next_to(g1,6*RIGHT)
        self.play(FadeIn(panah1))
        line3=TexMobject(r"\left [ W \right ]_{B'} = \begin{bmatrix} \alpha\\ \beta\end{bmatrix}")
        line3.shift(UP)
        line4=TextMobject("Vektor Basis Baru",color=RED)
        g2=VGroup(line3,line4)
        self.play(ShowCreation(g2))
        self.play(g2.to_edge,UP+RIGHT)
        
        line5=TextMobject("W")
        line5.next_to(g1,DOWN)
        panah2=Arrow(np.array([0,0,0]),np.array([0,-1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah2.next_to(line5,2*DOWN)
        line6=TexMobject(r"\left [ W \right ]_{B}")
        line6.next_to(panah2,2*DOWN)
        g3=VGroup(line5,panah2,line6)
      
        panah4=Arrow(np.array([-3,0,0]),np.array([2,0,0]),buff=0,tip_length=0.4,width=10,color=BLUE)
        panah4.next_to(line6,6*RIGHT)
        
        line7=TextMobject("W")
        line7.next_to(g2,DOWN)
        panah3=Arrow(np.array([0,0,0]),np.array([0,-1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah3.next_to(line7,2*DOWN)
        line8=TexMobject(r"\left [ W \right ]_{B'}")
        line8.next_to(panah3,2*DOWN)
        g4=VGroup(line7,panah3,line8)
        
        line9=TextMobject("?")
        line9.shift(0.8*DOWN)
        
        line10=TexMobject(r"A\left [ W \right ]_{B} = \left [ W \right ]_{B'}")
        line10.shift(1.8*DOWN)
        line10.scale(0.75)
        panah5=Arrow(np.array([0,0.5,0]),np.array([0,-0.1,0]),buff=0,tip_length=0.4,width=5,color=RED)
        panah5.next_to(line10,0.5*DOWN)
        line11=TexMobject(r"P_{B\rightarrow B'}\left [ W \right ]_{B} = \left [ W \right ]_{B'}")
        line11.next_to(panah5,1.5*DOWN)
        line11.scale(0.85)
        
        
        self.play(FadeIn(g3))
        self.play(FadeIn (panah4))
        self.play(FadeIn(g4))
        self.play(FadeIn(line9))
        self.play(FadeIn(line10))
        self.play(FadeIn (panah5))
        self.play(FadeIn(line11))
        self.wait(25)
        
        
        
class Scenedelapan(Scene):
    def construct(self):
        title = TextMobject("CATATAN",color=RED)
        basel = TexMobject(r"\textup{Jika P adalah Matriks Transisi dari B ke B' maka P mempunyai invers yaitu} P^{-1}")
        basel2=TexMobject(r"\textup{Maka} P^{-1} \textup{adalah matriks transisi dari B' ke B}")
        basel.scale(0.5)
        basel2.scale(0.5)
        basel2.next_to(basel,1.5*DOWN)
        bb=VGroup(basel,basel2)
        bb.next_to(title,2*DOWN)
        bb.set_color_by_gradient(BLUE,GREEN)
        aa=VGroup(title, bb)
        self.play(Write(title),FadeInFrom(bb,UP),)
        self.wait(19)
        self.play(FadeOut(title),FadeOut(bb))
        
        

      
        grid_title = TextMobject("PERUBAHAN BASIS", color=RED)
        grid_title.scale(2)
        grid_title.move_to(aa)

        self.add(grid_title)  # Make sure title is on top of grid
        self.play(FadeInFrom(grid_title, direction=DOWN))
        self.wait()

        grid_transform_title = TextMobject("Mengambil vektor yang ditulis di satu basis\\\\" "dan menulis di basis lain")
        grid_transform_title.set_color_by_gradient(BLUE,GREEN)
        grid_transform_title.move_to(grid_title, UL)
        grid_transform_title.scale(0.8)
        self.play(Transform(grid_title, grid_transform_title))
        self.wait(12)