#你是个数学老师，你在登记成绩时发现，有两位学生（lily和tony）的成绩登反了，请你帮他修改过来吧！
#开始情况是这样
score = {"lily":97, "qiqi":93, "tony":78, "fenfen":88}
#为了转换需要一个虚拟参数,命名为exchange

#exchange的值为lily的值
exchange = score["lily"]

#再将tony的值赋值给lily
score["lily"] = score["tony"]

#最后将exchange赋值给tong
score["tony"] = exchange

#再循环打印
for i in score:
    print(i,score[i])