# Datacollect

I'm a tiny Flask app that silently collects and dumps data. ;-)

Request:
```json
{
  "source": "foo",
  "data": "user_1,greeting,Hello world!"
}
```

Dumps to file foo.csv:
```csv
user,intent,text
user_1,greeting,Hello world!
```

