# MongoDB shell commands

## Secondary OK

```
rs.slaveOk()
rs.secondaryOk()
```

## List all collections and corresponding number of documents

```
db.getCollectionNames().map(function(name) { 
    return { "name": name, "count": db[name].count() } 
})
```

## Search for the document with a particular field

```
db.test.find( { $where: function() {
   function hasProp(obj, prop) {
    for (var p in obj) {
        if (obj.hasOwnProperty(p)) {
            if (p === prop && obj[p] !== "" && obj[p] !== undefined && obj[p] !== null) {
                return obj;
            } else if (obj[p] instanceof Object && hasProp(obj[p], prop)) {
                return obj[p];
            }
        }
    }
    return null;
   }
   return hasProp(this, "staffNumber");
} } );
```

## Find all the collections with a particular field

```
db.getCollectionNames().forEach(function(myCollectionName) {
	var frequency = db[myCollectionName].find({"SomeFieldToFind": {$exists: true}}).count();
		if (frequency > 0) {
	print(myCollectionName);
	}
});
```



