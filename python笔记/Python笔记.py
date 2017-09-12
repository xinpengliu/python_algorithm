======================================================================
1.【列表VS数组】
列表没有行与列的概念
直接使用赋值方式，如a=[[1,2,3],[4,5,6]],则a是列表，并不是数组
>>>a=[[1,2,3],[4,5,6]]
>>>type(a)	# <class 'list'>

>>>import numpy as np
>>>a=np.array([[1,2,3],[4,5,6]])
>>>type(a)	# <class 'numpy.ndarray'>
======================================================================
2.【格式化多个字符串】
当需要格式化多个字符串时，使用元组形式
name=jack
age=25
print('我叫%s,今年%d岁'%(name,age))

======================================================================
3.【input】
使用input函数由键盘输入的默认是字符串类型，
所以由键盘输入数字需要用int转换为整型，或者float转换为浮点型
>>>input()	#输入字符串没啥不妥，直接输入数字会把数字变成字符串
>>>int(input())	#当需要使用数字时就得这么使用
假如需要把键盘输入的数字赋给某变量
>>>a=int(input())
======================================================================
4.【只取数组的某行或某列时，得到的是一个维度的数组，既不是行向量，也不是列向量】
只有数组使用行与列的提取，列表没有行与列的概念
只有数组类型可使用行与列的提取，如x=data[:,0:-1],而列表不能这么做
当只取数组的某行或某列时，得到的是一个维度的数组，既不是行向量，也不是列向量，虽然得到的维
度以一维行向量显示，但是将他转置后还是不变，还是以行向量的形式显示，但是使用x.reshape(-1,1)后
可变为列向量。
x.shape    数组x的每个维度的大小，因为x可能不止二维的情况，比如RGB图像
x.shape[0] 数组x的行数，即第一维度
x.shape[1] 数组x的列数，即第二维度
x.shape[2] 数组x的第三维度大小，比如RGB图像第三维度大小为3
np.transpose(x)		求x的转置

=========================================================================
5.【python中的几种取整的方法】
fix 朝0方向取整   			>>>numpy.fix(3.4)   # 3.0	>>>numpy.fix(-3.4)    # -3.0
floor 朝负无穷方向取整		>>>numpy.floor(3.4) # 3.0	>>>numpy.floor(-3.4)  # -4.0
ceil朝正无穷方向取整		>>>numpy.ceil(3.4)  # 4.0	>>>numpy.floor(-3.4)  # -3.0
round 四舍五入取整			>>>round(3.4)		# 3		>>>round(3.5)		  #4.0	(有无numpy都可以)

===========================================================================
6.【数组分片】
python中对数组或者range等，只能取到头，取不到尾（冒号后面的叫尾，即取不到冒号后面的）
range(4)  	#0,1,2,3
range(3,6)	#3,4,5

数组分片操作：设x是n*m的数组
x[0:3,:]	#取第0,1,2行的所有列元素，取不到第三行的
x[:-1,:]	#取第0到倒数第1行(但是取不到倒数第一行)的所有列
x[:,-1]		#取最后一列
-1	表示取的最后一行或者列，
0:-1表示取第0到最后一行或列但是取不到最后一行或列(因为只取头，取不到尾)

x[-1]和x[n-1]都表示去问最后一行
x[2:]表示取第二行到最后一行
x[:n]表示取第0行到第n-1行(取不到n)
x[-3:]表示取倒数第三行到最后一行(共取3行)
x[:-3]表示取第0行到倒数第三行(取不到-3即0到倒数第四行)
x[::2]表示从第0行开始，以步长为取行
x[3::2]表示从第3行开始，以步长为取行

================================================================================
7.【原始字符串：在字符串前边加一个英文字母r即可】
>>>str1=r'c:\now'	#如果不加r,字符串中的\n会被解释为换行符
>>>str		#'c:\\now'
>>>print(str1)	#c:\now

===============================================================================
8.【sys.argv[]的使用方法】：
比如某路径下有个文件test.py
必须在该路径下的命令行下执行 Python test.py 123  
会输出test.py   123
不能直接在python环境下运行，这样会报错，因为后面需要街上命令行参数，这参数需要人从键盘敲进去，
即sys.argv[0]表示文件本身，sys.argv[1]表示命令行参数的第一个参数，以此类推
test.py文件有以下内容：
import sys
a=sys.argv[0]
b=sys.argv[1]
print(a)
print(b)

===================================================================================
9.【func(*args,**kargs)】
python中，什么是*args和**kargs,例如func(*args,**kargs)        
答：他俩是python中的可变参数。*args表示任意个无名参数，他是一个tuple;**kargs表示关键字参数，
他是一个dict.并且当同时使用他俩时，必须*args参数列要在**kargs前，像func(a=1,b='2',1,None)会报错，
因为这里a=1,b='2'是给关键字赋值了
当定义func(*args,**kargs)的形式之后，即必须先这么定义func()之后：         
func(1,2,3,4)  (1,2,3,4)是属于*args参数列的元组     
func(a=1,b=2)	( )空列表对应args,{'a':1,'b':2}对应kargs       
func(1,2,a=1)	(1,2)对应args, {'a':1}       
func('a',1,None,a=1,b='2')  ('a',1,,None)对应args;{'a':1'b':'2'}对应kargs      

=====================================================================================
10.【关于imread()】
在python版的opencv中，无论imread()读取的是什么格式图像(RGB,GRAY,...),imread()读取后都会变成三
个通道。因为imread()默认读取RGB格式，即使原图是灰度图，读取后也会变成三个通道。因此，
需要在imread()参数中添加一个可选参数0。例如imread('a.jpg',0)表示读取原图像格式     

利用cv2读取图像和使用matlab读取图像在每个通道的顺序不同，cv2读入的形式是BGR,matlab读入的形式为RGB

======================================================================================
11.【 关于 cv2.waitKey() 】
python版opencv中，使用imshow()显示图片时，后面必须配合使用cv2.waitKey()和cv2.destroyAllWindow(),
否则会出现未响应一类的情况。     
cv2.waitKey()在任意窗口下使用。一般用于显示图片后等待输入按键来销毁窗口。     
cv2.waitKey()的参数为等待键盘触发的时间，单位为ms，函数有返回值。  
当没有按键按下时，返回-1；当某键例如('q')被按下时，返回该键ASCII码。在一些系统中，cv2.waitKey()的返
回值可能比ASCII码的值更大。在所有系统中，可以通过读取返回值的最后一个字节来保证只提取ASCII码。
具体代码如下：     
keycode=cv2.waitKey()      
'''if keycode!=-1      
	keycode&=0xff		#&是按位与运算
'''    
if cv2.waitKey()&0xff==ord('q')			#这里与oxff运算是为了提取ASCII码，因为不同系统可能不一样 #ord('q')返回113
	break		#若按下的键的ASCII与q的ASCII码相等，就执行break语句
	
'''ord()函数是以单个字符为参数，返回其对应的ASCII码；与ord()对应的chr()和unichr()[它与chr()不同
的是返回unicode字符]以0到255整数做参数，返回对应字符。如chr(113)返回'q'。'''
&是按位与运算，and是逻辑运算
cv2.waitKey(5)表示等待5 毫秒，但是只要按了键，就不必等待5毫秒。要和time.sleep(5)分清楚
==============================================================================================

12.【关于time.localtime(), time.sleep(t),time.ctime(),time.time()】
time.sleep(t) 该函数没有返回值,t表示推迟的秒数。该函数推迟调用线程的运行，可通
过参数secs指秒数，表示进程挂起的时间
''' print ("Start : %s" % time.ctime())
	time.sleep( 5 )
	print ("End : %s" % time.ctime())
	以上实例输出结果为：
	Start : Tue Feb 17 10:19:18 2013
	End : Tue Feb 17 10:19:23 2013
'''
time.ctime(sec)以秒为单位的时间转换为表示本地时间的字符串.  一般不这么用，没啥意义，如下：
>>> time.ctime(10)	#从1970年8:00:00开始计数10秒
'Thu Jan  1 08:00:10 1970'

即一般不给该函数参数，如下
>>>import time
>>>print ("ctime : ", time.ctime()) #ctime :  Sat Sep  9 10:32:32 2017


如果不给参数，直接time.ctime()，则返回当前时间
time.localtime() #返回当前时间：time.struct_time(tm_year=2017, tm_mon=9, tm_mday=9, tm_hour=10, tm_min=41, tm_sec=1, tm_wday=5, tm_yday=252, tm_isdst=0)
如果两次本地时间相减，例如a=time.localtime(),b=time.localtime()后，
需要使用索引来相减，不能直接使用a-b,应使用a[0]-a[0]形式对应相减。

>>>tic=time.time()		#time.time()显示的形式为1505095164.431292
>>>toc=time.time()
>>>toc-tic的间隔单位是秒
==============================================================================================
13.【assert】
assert 这个关键字称为断言，当assert后面的条件为假时，程序自动崩溃并抛出AssertionError的异常
>>>assert 3>4	#  AssertionError
一般来说，我们可以使用它在程序中置入检查点，当需要确保程序中的某个条件一定为真才能让程序正常工作的
话，就可以使用assert

==================================================================================================
14.【列表添加、删除以及插入元素】【append,extend,insert】【remove(),del,pop()】【insert】
python中列表是比数组更强大的集合，列表可存放多种数据类型
【1】向列表中添加元素可使用append,extend,insert
append()每次只能添加一个元素到列表末尾，该元素可以是字符串，但不能是列表
extend()每次添加一个可迭代的参数到列表末尾,该参数可以是字符串和列表，append却不能这么传列表。例如：
>>>a=[]
>>>a.append(3)
>>>a.append(3,4)
----------------------------------
>>>b=[]
>>>b.extend(2)	 #报错，TypeError: 'int' object is not iterable
>>>b.extend('2') #正确，也就是说必须是字符串形式，因为字符串可迭代
>>>b.extend('6987')	# b为['2','6', '9', '8', '7']
>>>b=[]
>>>b.extend([1,2,'333'])	# [1, 2, '333']  参数只传字符串与只传列表是不一样的。
							# 但是传字符串和传列表都是因为他们可迭代
-----------------------------------
insert方法有两个参数，第一个参数表示在列表中的位置，第二个参数表示在该位置插入的元素，如：
>>>a=[1,2,3]
>>>a.insert(1,'a')	# a为[1, 'a', 2, 3]
>>>a.insert(2,[33,25])	# a为[1, 'a', [33, 25], 2, 3]
看起来好像insert在某位置插入元素好像没多大作用，当多维情况下：
>>>b=[[1,2,3],[3,4,5],[4,5,6]]
>>>b.insert(1,[2,3,4])
------------------------------------
【2】向列表中删除元素有3种方法：remove(),del,pop()
>>>a=[1,2,3]
>>>a.remove(2)	#remove()中的参数是列表中元素，不是索引
------------------------------------
>>>a=[1,2,3]
>>>del a[0]		#这是按索引删除的
>>>del a 		#删除整个列表
------------------------------------
pop()弹出(返回)列表中最后一个元素，该操作后，最后一个元素从列表中删除了
pop(n)	n为列表元素索引
>>>a=[1,0,1,2,3,4]
>>>b=a.pop()		#a为[1,0,1,2,3],b为4
>>>a.pop(2)			#a为[1,0,2,3]
=================================================================================
15.【对列表进行翻转，排序操作】
1,对列表进行翻转，排序
翻转：reverse
>>>a=[4,2,3]
>>>a.reverse()	#a为[3,2,4]
-------------------------------------
2,列表元素排序：sort  从小到大排序
>>>a=[4,2,3]
>>>a.sort()		#a为[2,3,4]
3,对列表进行由大到小排序：
>>>a=[4,2,3]
>>>a.sort(reverse=True)	#a=[4,3,2]
=================================================================================

16.【引用和拷贝】  www.jb51.net/article/57723.htm
	可变类型： 如list,set,自定义类型		（等价于C#中的引用类型）
	不可变类型：如string，number，tuple等	（等价于C#中的值类型）
	当程序中使用'='赋值操作符时，例如a=b
【1】对于不可变对象，a作为b的一个拷贝被创建，a和b将指向不同内存地址，a和b相互独立
	如：a=10,b=a,a=20   b依旧是10
【2】对于可变对象，a作为b的一个引用被创建，a和b的元素公用相同的内存地址，a和b的元素共享。
	如：a=[1,2,3,4],b=a,print(b is a) #True
		b[2]=-100,b为[1,2,-100,4],a为[1,2,-100,4]
		使用b[2]=-100这种方法修改元素可以，但是不能对a和b重新全部赋值，如a=[3,6,9]后，
		代表又重新开辟了一块内存。
可使用id()函数来查询地址是否一样，如id(a),id(b)
------------------------------------------------
对列表进行复制时，要用切片形式，不能省略[:]
a=[3,2,4]
b=a[:]
a.reverse()		#a为[4,2,3],b为[3,2,4],b并没有改变，因为b=a[:]把a的所有
				#元素赋给了b，并没有执行引用b=a

a=[3,2,4]
b=a
a.reverse()		#a为[4,2,3],b为[4,2,3]	,因为a列表是可变对象，所以b=a是引用，
				#所以a和b的内存地址是一处.对于不可变对象，如：a=10,b=a,a=20   b依旧是10
=============================================================================================
17.【创建空字典、集合，空列表，空元组】
创建空字典用a={}
创建空集合用a=set()		set中的元素是 无序不重复 的，可以利用这个特点去除列表中的重复元素。
>>>a=[2,2,2,0,1,2,0,1,2,0,0,1]
>>>b=set(a)
创建空列表用a=[]
创建空元组用a=()
但是元组并不需要(),逗号才是关键，如
b=2,3,4
type(b)		#<class 'tuple'>
c=1,
type(c)		#<class 'tuple'>
d=1
type(d)		#<class 'int'>
==============================================================================================
18.【递归vs迭代】：使用递归解决某些问题更容易，代码实现更简洁，但是递归比迭代运算速率慢
==============================================================================================
19.字符串操作
【1】str1[::-1]表示对字符串进行翻转,简单的步长为-1, 即字符串的翻转(常用)
	注意列表的翻转是a.reverse(),字符串没有属性reverse
------------------------------------------------------------
【2】去掉两端字符串： strip(), rstrip(),lstrip()
s = '  -----abc123++++       '

# 删除两边空字符
s.strip()		#s.strip()后字符串s并没变，因为不是就地操作
s.rstrip()	# 删除右边空字符
s.lstrip()  # 删除左边空字符


s.strip().strip('-+')	# 删除两边某字符和空字符
s.strip().strip('ab')	#删除两边a,b和空字符
s.strip('ab')		    #删除两边a和b或
s.lstrip('asd')  # 删除左边字符a或s或d
 
【3】删除单个固定位置字符： 切片 + 拼接。不推荐
s = 'abc:123'
new_s = s[:3] + s[4:]	# 字符串拼接方式去除冒号
print(new_s)

【4】删除任意位置字符同时删除多种不同字符：replace(), re.sub()
# 去除字符串中相同的字符
s = '\tabc\t123\tisk'
print(s.replace('\t', '')) #即 把字符用''替换，注意''不是空格,' '才是空格，两个引号之间什么也没有

import re
# 去除\r\n\t字符
s = '\r\nabc\t123\nxyz'
print(re.sub('[\r\n\t]', '', s))

【5】删除最后一个字符,还是切片形式
s='123345'
s=s[:(len(s)-1)]
# 以下注释可不看
'''
同时删除多种不同字符：translate()        py3中为str.maketrans()做映射
s = 'abc123xyz'
# a _> x, b_> y, c_> z，字符映射加密
print(str.maketrans('abcxyz', 'xyzabc'))	#打印{97: 120, 98: 121, 99: 122, 120: 97, 121: 98, 122: 99}
# translate把其转换成字符串
print(s.translate(str.maketrans('abcxyz', 'xyzabc')))	#打印xyz123abc

去掉unicode字符中音调
import sys
import unicodedata
s = "Zhào Qián Sūn Lǐ Zhōu Wú Zhèng Wáng"
remap = {
    # ord返回ascii值
    ord('\t'): '',
    ord('\f'): '',
    ord('\r'): None
    }
# 去除\t, \f, \r
a = s.translate(remap)

　　通过使用dict.fromkeys() 方法构造一个字典，每个Unicode 和音符作为键，对于的值全部为None
　　然后使用unicodedata.normalize() 将原始输入标准化为分解形式字符
　　sys.maxunicode : 给出最大Unicode代码点的值的整数，即1114111（十六进制的0x10FFFF）。
　　unicodedata.combining:将分配给字符chr的规范组合类作为整数返回。 如果未定义组合类，则返回0。

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))) #此部分建议拆分开来理解
b = unicodedata.normalize('NFD', a)

调用translate 函数删除所有重音符
print(b.translate(cmb_chrs))
'''

