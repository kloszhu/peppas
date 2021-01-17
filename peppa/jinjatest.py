import jinja2
msg="""select * from person where 1=1  {% if dict_table_data %} 
and id=1  
{% endif %}"""
msg+="hellow world"
temp=jinja2.Template(msg)
result=temp.render({'dict_table_data':True})
print(result)