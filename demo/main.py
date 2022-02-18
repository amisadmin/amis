from amis.components import Page, TableCRUD

page = Page(title='标题', body='Hello World!')
# 输出为Json
print(page.amis_json())
# 输出页面html
print(page.amis_html())


page = Page(title='标题',
            body=TableCRUD(api="https://3xsw4ap8wah59.cfc-execute.bj.baidubce.com/api/amis-mock/mock2/sample",
                           columns=[{"name": "id","label": "ID"},{"name": "name","label": "name"}]))
# 输出页面html
print(page.amis_html())

# 输出为Json
print(page.amis_json())
