

Questions:

Read multiple files into session?
spark.

Read XML Files?
spark.read.format('xml').schema(schema).load(filePath);

Parse XML columns?
spark-xml library

[spark-xm](https://github.com/databricks/spark-xml#spark-notes)

```python
from spark.sql.column import Column, _to_java_column
from spark.sql.types import _parse_datatype_json_string
import pyspark.sql.functions as F

def ext_from_xml(xml_column, schema, options={}):
    java_column = _to_java_column(xml_column.cast('string'))
    java_schema = spark._jsparkSession.parseDataType(schema.json)
    scala_map = spark._jvm.org.apache.spark.api.python.PythonUtils.toScalaMap(options)
    jc = spark._jvm.com.databricks.spark.xml.functions.from_xml(
        java_column, java_schema, scala_map
    )
    return Column(jc)

def ext_schema_of_xml_df(df, options={}):
    assert len(df.columns==1)

    scala_options = spark._jvm.PythonUtils.toScalaMap(options)
    java_xml_module = getattr(
        getAttr(spark._jvm.com.databricks.spark.xml, "package$"),
        "MODULE$"
    )
    java_schema = java_xml_module.schema_of_xml(df._jdf, scala_options)
    return _parse_datatype_json_string(java_schema.json())


xml = '<?xml version="1.0" encoding="utf-8"><visitors><visitor id="123" age="68" sex="M"/></visitors>'
```


### Set uop dataframe
```python
df = spark.createDataFrame([('1', xml)], ['id', 'visitors'])
df.show()
```


### get xml schema and parse xml column
```python
payloadSchema = ext_schema_of_xml_df(df.select("visitors"))
parsed = df.withColumn("parsed", 
                       ext_from_xml(F.col("visitors"), payloadSchema)
                       )
parsed.show()
```

### extract 'visitor' field from StructType
```python
df2 = parsed.select(*parsed.columns[:-1], F.explode(F.col('parsed').getItem('visitor')))
df2.show()
```

### get field names, which will become new columns
```python
new_col_names = [s.split(':')[0]] for s in payloadSchema['visitor'].simpleString().split('<')[-1].strip('>>').split(',')]

new_col_names
```
### Create new columns
```python
for c in new_col_names:
    df2 = df2.withColumn(c, F.col('col').getItem(c))

df2 = df2.drop('col', '_VALUE')
df2.show()
```