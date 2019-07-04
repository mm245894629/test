import webbrowser
import time
import xlrd
book=xlrd.open_workbook('kks.xlsx')
sheet=book.sheet_by_index(0)
print(sheet.cell(0,0).value)
print(sheet.get_rows(),book.sheet_names())
p=[]
Data_sheet = book.sheets()[0]
rowNum=Data_sheet.nrows
colNum=Data_sheet.ncols

for i in range(1,rowNum):
    rowlist=[]
    for j in range(colNum):
        rowlist.append(Data_sheet.cell_value(i,j))
        p.append(rowlist)

print(p)
from pyecharts import options as opts
from pyecharts.charts import Page, ThemeRiver,Polar,Grid,Timeline,Pie
from example.commons import Faker

data=p
def th_base():
    c = (
        ThemeRiver()
            .add(
            ["休息", "锻炼", "自学", "玩或看剧", "虚空时间", "思考或琐事"],
            data,
            singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="ThemeRiver"))
    )
    return c
def po_base():
    d = (
        Polar()
        .add_schema(
            radiusaxis_opts=opts.RadiusAxisOpts(data=Faker.week, type_="category")
        )
        .add("休息时间", [9, 9, 9, 9, 10, 5, 10], type_="bar", stack="stack0")
        .add("有效提升时间", [2, 2, 3, 1, 2, 1, 2], type_="bar", stack="stack0")
        .add("浪费时间", [3, 2, 3, 4, 6, 8, 5], type_="bar", stack="stack0")
        .set_global_opts(title_opts=opts.TitleOpts(title="Polar-RadiusAxis"))
    )
    return  d
value1=[70,60,24,29,28,53,40]
value2=[43,80,56,43,8,29,60]
value3=[9,10,34,33,1,49,80]
value4=[170,20,71,48,2,37,26]
value5=[197,33,56,24,14,57,16]
def timeline_pie() :
    attr = ['b站','知乎','微信','QQ','网易音乐','safari','其它APP']
    pie0 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, value1)],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("周一"))
    )
    pie1 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, value2)],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("周二"))
    )
    pie2 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, value3)],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("周三"))
    )
    pie3 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, value4)],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("周四"))
    )
    pie4 = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, value5)],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("周五"))
    )
    tl = (
        Timeline()
        .add(pie0, "周一")
        .add(pie1, "周二")
        .add(pie2, "周三")
        .add(pie3, "周四")
        .add(pie4, "周五")
    )
    return tl
page=Page()
page.add(th_base(),po_base(),timeline_pie())
page.render('tt.html')
webbrowser.open('file:///F:/code_small_projects/tt.html')


