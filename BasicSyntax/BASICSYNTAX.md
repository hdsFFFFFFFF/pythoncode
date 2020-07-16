标识符：
	1.由字母，数字，和下划线组成。不能以数字开头。
	2.不能以数字开头
	3.标识符区分大小写
	4.下划线开头的标识符有特殊意义：
		！单下划线开头_foo代表不能直接访问的类属性，需要
		  通过类提供的接口进行访问，不能用from xxx import *导入
		！双下划线开头的__foo代表类的私有成员
		！以双下划线开头和结尾的__foo__代表Python里特殊方法专用
		  的标识，如__init__()代表类的构造函数
	5.多行语句：
		！total = item_one +	\
			  item_two +	\
			  item_three
		！语句中有[]，{}或[]括号就不需要使用续行符
		  days = ['Monday', 'Tuesday', 'Wednesday',
		  		'Thursday', 'Friday']
	6.python引号：
		！可以使用单引号('),双引号("),三引号(''')表示字符串
		！三引号(''')可以由多行组成
		  text = '''
			first  line
			second line
			third  line
		  '''
	7.多行注释：
		！使用三个单引号(''')或者三个双引号(""")
		  textA = '''
			first  line
			second line
		  '''

		  testB = """
		  	first  line
			second line
		  """
	8.代码块(组)：
		！缩进相同的一组语句构成一个代码块
		！像while,if,def,class这样的复合语句，首行以关键字开始
		  以冒号(:)结束，该行之后的一行或多行代码构成代码组。
		  将首行及后面的代码组称为一个子句(clause)

python命令行参数
	1.getopt模块
		！python提供getopt模块来获取命令行参数
			$ python test.py arg1 arg2 arg3
	2.python也可以使用sys的sys.argv来获取命令行参数：
		！sys.argv是命令行参数列表
		！len(sys.argv)是命令行参数个数
		！sys.argv[0]表示脚本名
