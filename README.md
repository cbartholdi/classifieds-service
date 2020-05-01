# Classifieds service
A small Django appllication with a GraphQL API for placing classifieds ads.

## Developers

```
docker-compose up 
```

## The API

Find the API at http://localhost:8000/graphql


**Create**
```
mutation {
  createClassified(subject: "Awesome thing", body: "Plz buy!", email: "foo@bar.com", price: {amount: 50.5, currency: "SEK" }) {
    ok
    errorCode
    classified {
      id
      email
      subject
      body
      price {
        amount
        currency
      }
    }
  }
}
```

**Delete**
```
mutation {
  deleteClassified(classifiedId: 6) {
    ok
    errorCode
  }
}
```

**List**
```
query {
  allClassifieds(orderBy: "price", ordering: "desc") {
    id
    subject
  }
}
```