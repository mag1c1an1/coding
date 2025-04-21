xa,ya,xb,yb,xc,yc = map(int, input().split())
xd,yd,xe,ye,xc,yc = map(int, input().split())

class Triangle:
    def __init__(self,xa,ya,xb,yb,xc,yc):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.xc = xc
        self.yc = yc
# 完全覆盖两个三角形的最小圆半径        
def min_circle_radius(t1,t2):
    # 计算三角形的外接圆半径
    def radius(xa,ya,xb,yb,xc,yc):
        a = ((xa-xb)**2 + (ya-yb)**2)**0.5
        b = ((xb-xc)**2 + (yb-yc)**2)**0.5
        c = ((xa-xc)**2 + (ya-yc)**2)**0.5
        s = (a+b+c)/2           
        return a*b*c/(4*s**2)   
    # 计算三角形的内心坐标
    def center(xa,ya,xb,yb,xc,yc):
        a = ((xa-xb)**2 + (ya-yb)**2)**0.5
        b = ((xb-xc)**2 + (yb-yc)**2)**0.5
        c = ((xa-xc)**2 + (ya-yc)**2)**0.5
        x = (xa*a + xb*b + xc*c)/(a+b+c)    
        y = (ya*a + yb*b + yc*c)/(a+b+c)    
        return x,y
    # 计算三角形的内心到顶点的距离
    def distance(xa,ya,xb,yb,xc,yc):
        x,y = center(xa,ya,xb,yb,xc,yc)
        return ((x-xa)**2 + (y-ya)**2)**0.5
    # 计算三角形的外接圆半径
    r1 = radius(xa,ya,xb,yb,xc,yc)      
    r2 = radius(xd,yd,xe,ye,xc,yc)  
    # 计算三角形的内心到顶点的距离
    d1 = distance(xa,ya,xb,yb,xc,yc)
    d2 = distance(xd,yd,xe,ye,xc,yc)    
    # 计算最小圆半径
    r = max(r1,r2)  
    if d1 > r or d2 > r:
        r = max(r,d1,d2)    
    return r
t1 = Triangle(xa,ya,xb,yb,xc,yc)
t2 = Triangle(xd,yd,xe,ye,xc,yc)
print(min_circle_radius(t1,t2))