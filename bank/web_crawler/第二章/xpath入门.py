#xpath 是在XML文档中搜索内容的一门语言
#html是xml的一个子集
from lxml import etree

# xml = """
# <book>
#     <id>1</id>
#     <name>野花遍地香</name>
#     <price>1.23</price>
#     <nick>臭豆腐</nick>
#     <author>
#         <nick id="10086">周大强</nick>
#         <nick id="10010">周芷若</nick>
#         <nick class="joy">周杰伦</nick>
#         <nick class="jolin">蔡依林</nick>
#         <div>
#             <nick>惹了</nick>
#         </div>
#         <span>
#             <nick>我爱吃火锅</nick>
#         </span>
#     </author>
# </book>
# """
#
# tree = etree.XML(xml)#将文本加载为etree对象
# #result = tree.xpath("/book")#/表示层级关系
# #result = tree.xpath("/book/name/text()")#text()表示拿文本
# #result = tree.xpath("/book/author//nick/text()")#//表示拿到所有
# #result = tree.xpath("/book/author/*/nick/text()")#*表示任意的节点
# result = tree.xpath("/book//nick/text()")
# print(result)

tree = etree.parse("b.html")
#1.etree.parse直接接受一个文档，按照文档结构解析（本地文件）
#2.etree.html可以解析html文件：（服务器上返回的html数据）

#result = tree.xpath('/html/body/ul//a/text()')
#result = tree.xpath('/html/body/ul/li[1]/a/text()')#取第一个li
#result = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')#[@=""]对属性进行筛选
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    #从每个li中提取到文字信息
    result = li.xpath("./a/text()") #在li中继续去寻找，相对查找
    print(result)
    result2 = li.xpath("./a/@href")
    print(result2)

print(tree.xpath("/html/body/ul/li/a/@href"))
