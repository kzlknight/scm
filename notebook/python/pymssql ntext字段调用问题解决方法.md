下面是调用方式：

[ ** Example script - pymssql module (DB API 2.0)  **
](http://pymssql.sourceforge.net/example_pymssql.html)

[ ** Example script - _mssql module (lower level DB access)  **
](http://pymssql.sourceforge.net/example_mssql.html)

不过，在我使用过程中，发现，如果表中包含了ntext字段，就会出错，提示

```python

    不能用 DB-Library（如 ISQL）或 ODBC 3.7 或更早版本将 ntext 数据或仅使用  
      
    Unicode排序规则的 Unicode 数据发送到客户端。
```

查了一下，发现官方网站有解释:

> _**Q: What means "Unicode data in a Unicode-only collation or ntext data
> cannot be sent to clients using DB-Library"?** _
>
> **_A:_ ** If you connect to a SQL Server 2000 SP4 or SQL Server 2005, and if
> you make a SELECT query on a table that contains a column of type NTEXT, you
> may encounter the following error:  
>  ` _mssql.error: SQL Server message 4004, severity 16, state 1, line 1:  
>  Unicode data in a Unicode-only collation or ntext data cannot be sent to
> clients using DB-Library (such as ISQL) or ODBC version 3.7 or earlier. `  
>  It's the SQL Server complaining that it doesn't support pure Unicode via
> TDS or older versions of ODBC. There's no fix for this error. Microsoft has
> deprecated DB-Library a long ago, in favor of ODBC, OLE DB, or SQL Native
> Client. Many new features of SQL 2005 aren't accessible via DB-Library so if
> you need them, you have to switch away from pymssql or other tools based on
> TDS and DB-Library.
>
> A workaround is to change the column type to NVARCHAR (it doesn't exhibit
> this behaviour), or TEXT.

大概意思是,这是因为我们的pymssql使用早期的ODBC函数集来获取数据。后来微软才引入了ntext和nvarchar类型，但Microsoft并没有更新他们的
C-library，所以就没办法支持了。建议：将ntext修改为nvarchar或text.

显然，这不是个好的解决方法，那么是否就没有其他办法了呢?

还好，不用绝望，既然不支持ntext但支持text，那么我们只需要在输出时将ntext转换为text就好了，方法很简单：

```python

    SELECT cast ( field_name AS TEXT ) AS field_name
```

唯一的问题，可能是ntext和text字段所支持的长度不一样，所以也许你还需要设置一下TEXTSIZE

```python

    SET TEXTSIZE 65536
```

当然，你还可以将字段设置的大一点，这个就看你的需要了。

