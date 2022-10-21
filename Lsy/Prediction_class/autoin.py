import csv
def combination_k(s, k):

    # recursive basis
    if k == 0: return ['']
    # recursive chain
    subletters = []
    # 此处涉及到一个 python 遍历循环的特点：当遍历的对象为空（列表，字符串...）时，循环不会被执行，range(0) 也是一样
    for i in range(len(s)):
        for letter in combination_k(s[i + 1:], k - 1):
            if k==1:
                subletters += [s[i]]
            else:
                subletters += [s[i] + ',' + letter]
    return subletters

def combination_all(s,x):

    comb_list = []
    # 通过 for 循环调用 combination_k(s, k) 获取不同 k 值下的所有组合
    for i in range(1, x+1):
        comb_list += combination_k(s, i)
    return comb_list

def dynloop_rcsn(step ,lens, rem, cur_y_idx = 0, lst_rst = [], lst_tmp = []):
    max_y_idx = lens -1  # 获取Y 轴最大索引值

    for i in range(step ,rem , step):  # 遍历当前位置的所有的成分占比

        lst_tmp.append(i/100)  # 将当前层所含比例元素追加到lst_tmp 中

        if cur_y_idx == max_y_idx:  # 如果当前层是最底层则将lst_tmp 作为元素追加到lst_rst 中
            lst_tmp[max_y_idx] = rem/100
            lst_rst.append([*lst_tmp])
            lst_tmp.pop()
            break

        else:  # 如果当前还不是最底层则Y 轴+1 继续往下递归，所以递归最大层数就是Y 轴的最大值
               # lst_rst 和lst_tmp 的地址也传到下次递归中，这样不论在哪一层中修改的都是同一个list 对象
            dynloop_rcsn(step,lens ,rem - i,  cur_y_idx+1, lst_rst, lst_tmp)
        lst_tmp.pop()  # 在本次循环最后，不管是递归回来的，还是最底层循环的，都要将lst_tmp 最后一个元素移除

    return lst_rst

def mix(a,b,c,step):
    whole = [['A1','A2','A3','a1','a2','a3','B1','B2','b1','b2','C1','C2','c1','c2']]
    path1 = 'output.csv'
    with open(path1, 'w', newline="") as f:

        csv_write = csv.writer(f)

        step = int(step * 100)

        for i in a:
            for j in b:
                for k in c:

                    aelement = i.split(',')
                    belement = j.split(',')
                    celement = k.split(',')

                    haha = []
                    hehe = []  # 这俩是防止数组复制出错的，无实际使用意义。
                    adis = dynloop_rcsn(step,len(aelement), 100, 0,  haha, hehe)
                    haha = []
                    hehe = []
                    bdis = dynloop_rcsn(step,len(belement), 100, 0, haha, hehe)
                    haha = []
                    hehe = []
                    cdis = dynloop_rcsn(step,len(celement), 400, 0,  haha, hehe)

                    for l in adis:
                        for m in bdis:
                            for n in cdis:
                                ab = i.split(',')
                                ab = ab + [0] * (3 - len(ab))
                                ac = j.split(',')
                                ac = ac + [0] * (2 - len(ac))
                                ad = k.split(',')
                                ad = ad + [0] * (2 - len(ad))

                                al = l + [0] * (3 - len(l))
                                am = m + [0] * (2 - len(m))
                                an = n + [0] * (2 - len(n))

                                temp = ab + al + ac + am + ad + an

                                #print(temp)
                                #input()


                                csv_write.writerow(temp)

                                whole.append(temp)

    return whole



def predictioinclass(a,b,c,step,filename):


    spaceA = a
    print('A位组合总样本：', spaceA )
    #length = eval(input('请输入组合元素样本的长度:'))
    length = 3
    c_a = combination_all(spaceA,length)
    print('A位样本总数为：',c_a)

    spaceB = b
    print('B位组合总样本：', spaceB)
    # length = eval(input('请输入组合元素样本的长度:'))
    length = 2
    c_b = combination_all(spaceB, length)
    print('B位样本总数为：', c_b)

    spaceC = c
    print('C位组合总样本：', spaceC)
    # length = eval(input('请输入组合元素样本的长度:'))
    length = 2
    c_c = combination_all(spaceC, length)
    print('C位样本总数为：', c_c)

    #test = c_c[5].split(',')
    #print(distribution(len(test),4))
    all = mix(c_a,c_b,c_c, step)

    path1 = filename

    with open(path1, 'w', newline="") as f:
        csv_write = csv.writer(f)

        csv_write.writerows(all)




