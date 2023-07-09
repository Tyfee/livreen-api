# livreen-api
json files and images for api requests. Used for the mobile app version of [livreen](https://livreen.site/)

Live at [Render](https://livreen-api.onrender.com/)

# Requesting a list with all books

The request is made to "https://livreen-api.onrender.com/books", and the returned objects will display title, author, id, cover, language, tags and level. 

Javascript:
```
fetch("https://livreen-api.onrender.com/books").then(resp => resp.json())
  .then(data => { console.log(data)})
}
```
![books](https://github.com/Tyfee/livreen-api/assets/121516618/3282c64b-b177-42cc-85dc-9afd0db40a57)


# Requesting a specific book

The request is made to "https://livreen-api.onrender.com/book?id=[BOOK_ID]", and the returned objects will display all the lines for the specific book requested.

Javascript:
```
fetch("https://livreen-api.onrender.com/book?id=mom_ja").then(resp => resp.json())
  .then(data => { console.log(data)})
}
```

![lines](https://github.com/Tyfee/livreen-api/assets/121516618/30b99167-a162-4eff-b6c5-4128db58d097)

# Requesting a specific line from a book

The request is made to "https://livreen-api.onrender.com/line?id=[BOOK_ID]&line=[number]", and the returned object will display the line from the requested book.

Javascript:
```
fetch("https://livreen-api.onrender.com/line?id=mom_ja&line=thirteen").then(resp => resp.json())
  .then(data => { console.log(data)})
}
```

![line](https://github.com/Tyfee/livreen-api/assets/121516618/fe326608-a545-4be9-8441-83e9459a4c7a)




