import math 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import pyplot
from matplotlib import numpy
x=numpy.arange(-1,1,0.05)
y=numpy.arange(-1,1,0.05)
v=[]
detv=10000
end_detv=1e-5*len(x)

def update_v():
	global detv
	detv=0
	for i in xrange(1,len(x),-1):
		for j in xrange(1,len(y),-1):
			if (i==len(x)/3or i==len(x)*2/3) and len(y)/3<j<len(y)*2/3:
				continue
			tmp=(v[i-1][j]+v[i+1][j]+v[i][j-1]+v[i][j+1])/4
			detv+=numpy.abs(tmp-v[i][j])
			v[i][j]=tmp
v.append([0. for i in xrange (len(x))])
for i in xrange (1,len(x)-1):
	tmp=[0.]
	for j in range(1,len(y)-1):
		if i==len(x)/3 and len(y)/3<j<len(y)*2/3:
			tmp.append(1.)
		elif i==len(x)*2/3 and len(y)/3<j<len(y)*2/3:
			tmp.append(-1.)
		else:
			tmp.append(0.)
		tmp.append(0.)
		v.append(tmp)
v.append([0. for i in xrange (len(x))])
while detv>end_detv:
	update_v()
x, y = numpy.meshgrid(x, y)

fig = pyplot.figure()
ax = fig.gca(projection='3d')
ax.set_title(r"Electric potential near two metal plates")
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$V$')
surf = ax.plot_surface(x, y, v, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
pyplot.show()