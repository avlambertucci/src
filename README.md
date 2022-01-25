
# Chalenge

## 1) 
### a-

#### It was used Factory pattern to create a factory that was shared by File and Web classes that are inheriting abstract methods from Interface IMedia, it could be different factories with specific methods too. The benefits from factory pattert is that we can decouple code from different blocks, and if we have to add an feature or another media type we don't need to modify our core code, we just create another class with the methods and arguments regarding that new flow linking with the factory that will be a kind of a 'middleware' distrubuiting the responsability to the right block
#### I have used '.startwith()' python built in method to filter the locations

### b- 

#### If had to use something to test the code I would use definetly pytest, but that would change the way the project would be created, because I would use the test driven principles and create the project first with the testing, I would create a test for every method, and I will expect the right response type, I would make it simple at the first just to make sure that I am receiving the right payload and returning it right to the API.

--------------------------------------------

## 2) In your opinion, when writing software what are the most important considerations to  writing quality code? (1 or 2 short paragraphs) 

### A: In my opinion we all must follow clean code principles in order to achieve a better software organization, with that beeing said the code must have understandable methods, classes, and the more important, the porpouse, we have to know what is this piece of code porpouse, because most of the times, is very likely that other developers will reafactorate your code, or even extending it creating other features, another important consideration is that the code must be very well prepared ato be escallable, very often  we have to escale our project, for example changing a database, using an external library, microservices. we have to be prepared to consider this questions in a mid or long-term cenario.

--------------------------------------------

## 3) Your team needs to choose an ecommerce platform to run your online web shop selling  artisan coffee. So far eligible options have been narrowed down to Shopify (https://www.shopify.ca/ ), Square (https://squareup.com/ca/en), or Solidus (https://solidus.io/). 
## What kind of arguments for/against each platform do you see for your store, and  ultimately which platform would you prefer and why? 


### A: Of course shopify would be the safest and rellyable choice here, if we have a safe and traditional business model, not only because of the tradition but it offers a 24/7 support which is very good for a company that would be lauching its services with several types of payment and sometimes it could be tricky in the first moment, but I have supposed that the coffee artisan shop is a local company that not only needs to be accesible and have to offer several types of payment, but also needs to have an affordable solution because that is what the business model was created, assuming that it has a very attractive POS, Square and Solidius would be more affordable to a business that is brand new and should have affordable fees, for a business that relly on affordability it would be very expensive to get the same features that Square and Solidius offer in Shopify, because the shopify model is offers the customer several integrations, plugins etc... but you have to pay extra to have them limiting our budget. I would suppose too that the owners of the coffee shop would be very creative and DIY adepts, considering this, they would have an IT team, due to that I would choose solidius right a way, because is an open source solution, that gives us access do solidius APIS which would be a great asset because we can make a very specific demand and create a customize workflow of our solution, and the github repo is very well rated and very updated